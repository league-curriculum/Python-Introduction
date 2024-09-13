
import re
import urllib 
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def replace_python(source: str, base_name: str = None, replacement_f=None):
    """ Regex pattern to find python.run blocks with optional height and width
    Args:
        source (str): Markdown source
        base_name (str):
        replacement_f ():

    Returns:

    """

    pattern = re.compile(r"```python\.run([^\n]*)\n(.*?)```", re.DOTALL)


    counter = [1]
    code = {}

    # Function to replace matched objects
    def replacer(match):
        args = match.group(1)
        code = match.group(2)

        py_code = code
        hw = {}
        width = height = None
        
        if ':' in args:
            _, spec = args.split(':')
            spec = spec.strip()
            parts = spec.split(',')
            for part in parts:
                key, value = part.split('=')
                hw[key] = value.strip()
            
            height = int(hw.get('height', None)) if 'height' in hw else None
            width = int(hw.get('width', None)) if 'width' in hw else None
            
       
        # Calc height from number of lines of code
        height = height or (len(py_code.split('\n')) * 17) + 110
        width = width or 700

        replacement = replacement_f(py_code, height, width)

        counter[0] += 1

        return replacement

    # Replace matched blocks in the source with the template string
    modified_source = pattern.sub(replacer, source)

    return modified_source, code



def generate_trinket_iframe(code, width='300', height='500', embed_type='python'):
    """
    Generates an HTML iframe for a Trinket.io embed.

    Parameters:
    - code (str): The code to be executed within the Trinket embed.
    - width (str): The width of the iframe (default is '300', can be specified in pixels or percentage).
    - height (str): The height of the iframe (default is '500').
    - embed_type (str): The type of Trinket embed (e.g., 'python').

    Returns:
    - str: An HTML iframe element as a string.
    """
    # Corrected base URL
    base_url = 'https://trinket.io/tools/1.0/jekyll/embed/'
    # Ensure the code is URL-encoded to be safely included in the URL
    encoded_code = urllib.parse.quote(code)

    # Construct the src URL
    src_url = f'{base_url}{embed_type}#code={encoded_code}'

    # Construct and return the iframe HTML string
    iframe_html = f'<div class="iframe-container"><iframe width="{width}" height="{height}" src="{src_url}" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe></div>'

    return iframe_html


# Testing
if __name__ == '__main__':
    
    def f(content, height, width):
        return f"|height={height} width={width}|{content.strip()}|"
    
    code = """
```python.run
program
```
foobar
"""
    v = replace_python(code, 'python', f)
    assert v[0] =='\n|height=144 width=700|program|\nfoobar\n', v[0]
    
    code = """
```python.run:height=300
program
```
foobar
"""
    v = replace_python(code, 'python', f)
    assert v[0] =='\n|height=300 width=700|program|\nfoobar\n', v[0]
    
    code = """
```python.run:height=300,width=500
program
```
foobar
"""
    v = replace_python(code, 'python', f)
    assert v[0] =='\n|height=300 width=500|program|\nfoobar\n', v[0]
    
    code = """
```python.run:width=500
program
```
foobar
"""
    v = replace_python(code, 'python', f)
    assert v[0] =='\n|height=144 width=500|program|\nfoobar\n', v[0]