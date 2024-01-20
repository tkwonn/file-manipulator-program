import sys
import markdown
from input_validator import ValidationError, validate_command, validate_arguments

def convert_markdown_to_html(args):
    inputpath = args[0]
    outputpath = args[1]

    with open(inputpath, 'r') as f:
        markdown_content = f.read()

    html_content = markdown.markdown(markdown_content)

    with open(outputpath, 'w') as f:
        f.write(html_content)


# Define a structure for commands and their validation rules
command_rules = {
    'markdown': {'arg_count': 4, 'file_checks': [2], 'function': convert_markdown_to_html},
}

if __name__ == '__main__':
    try:
        validate_command(sys.argv, command_rules)
        validate_arguments(sys.argv, command_rules)

        command = sys.argv[1]
        command_args = sys.argv[2:]
        command_function = command_rules[command]['function']
        command_function(command_args)

    except ValidationError as err:
        sys.stderr.buffer.write(b'Error: ' + str(err).encode() + b'\n')
        sys.stderr.flush()
        sys.exit(1)
