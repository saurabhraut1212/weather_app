import re

class TemplateEngine:
    @staticmethod
    def render(template_path, **context):
        """Simple template engine that handles basic templating"""
        with open(template_path, 'r') as f:
            template = f.read()
            
        # Handle extends
        extends_match = re.search(r'{%\s*extends\s+"([^"]+)"\s*%}', template)
        if extends_match:
            base_template_path = f"src/templates/{extends_match.group(1)}"
            with open(base_template_path, 'r') as f:
                base_template = f.read()
            
            # Extract blocks from child template
            blocks = {}
            for block_match in re.finditer(r'{%\s*block\s+(\w+)\s*%}(.*?){%\s*endblock\s*%}', template, re.DOTALL):
                blocks[block_match.group(1)] = block_match.group(2).strip()
            
            # Replace blocks in base template
            template = base_template
            for block_name, content in blocks.items():
                template = re.sub(
                    r'{%\s*block\s+' + block_name + r'\s*%}.*?{%\s*endblock\s*%}',
                    content,
                    template,
                    flags=re.DOTALL
                )
        
        # Replace variables
        for key, value in context.items():
            if isinstance(value, dict):
                for subkey, subvalue in value.items():
                    template = template.replace('{{ ' + f'{key}.{subkey}' + ' }}', str(subvalue))
            else:
                template = template.replace('{{ ' + key + ' }}', str(value))
        
        # Clean up any remaining template tags
        template = re.sub(r'{%.*?%}', '', template)
        template = re.sub(r'{{.*?}}', '', template)
        
        return template