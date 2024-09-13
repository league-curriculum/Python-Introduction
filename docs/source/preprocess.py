
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
    pattern = re.compile(r"```python\.run(?:\:\s*height='?(\d+)'?)?(?:,width='?(\d+)%?'?)?\n(.*?)```",
                         re.DOTALL)

    counter = [1]
    code = {}

    # Function to replace matched objects
    def replacer(match):
        m = match.group(0).strip('```')

        lines = m.split('\n')
        first = lines[0]
        py_code = '\n'.join(lines[1:])
        if ':' in first:
            _, spec = first.split(':')
            spec = spec.strip()
            _, height = spec.split('=')
            height = int(height.strip("'"))
        else:
            height = (len(py_code.split('\n')) * 17) + 110

        replacement = replacement_f(py_code, height)

        assert isinstance(replacement, str), f"Replacement must be a string, got {type(replacement)}"

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
    iframe_html = f'<iframe width="{width}" height="{height}" src="{src_url}" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>'

    print("!!!!!", src_url)

    return iframe_html