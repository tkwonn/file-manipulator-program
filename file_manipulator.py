import sys
from input_validator import ValidationError, is_positive_integer, validate_command, validate_arguments


def get_paths(args):
    inputpath = args[0]
    outputpath = args[1]
    return inputpath, outputpath


def reverse_file_contents(args):
    inputpath, outputpath = get_paths(args)
    contents = ''

    with open(inputpath) as f:
        contents = f.read()
        
    with open(outputpath, 'w') as f:
        f.write(contents[::-1])
        

def copy_file_to_path(args):
    inputpath, outputpath = get_paths(args)

    with open(inputpath, 'r') as firstfile, open(outputpath, 'w') as secondfile:
        for line in firstfile:
            secondfile.write(line)


def duplicate_file_contents(args):
    inputpath, _ = get_paths(args)
    count = args[3]
    contents = ''

    with open(inputpath, 'r') as f:
        contents = f.read()
        
    with open(inputpath, 'a') as f:
        for _ in range(int(count)):
            f.write(contents)


def replace_string_in_file(args):
    inputpath = args[0]
    oldstring = args[1]
    newstring = args[2]
    contents = ''

    with open(inputpath, 'r') as f:
        contents = f.read()
        
    if contents.find(oldstring) == -1:
        raise ValidationError(f'{oldstring} is not included in the file.')
    
    with open(inputpath, 'w') as f:
        f.write(contents.replace(oldstring, newstring))


# Define a structure for commands and their validation rules
command_rules = {
    'reverse': {'arg_count': 4, 'file_checks': [2,3], 'function': reverse_file_contents},
    'copy': {'arg_count': 4, 'file_checks': [2,3], 'function': copy_file_to_path},
    'duplicate-contents': {'arg_count': 4, 'file_checks': [2], 'additional_checks': [(3, is_positive_integer)], 'function': duplicate_file_contents},
    'replace-string': {'arg_count': 5, 'file_checks': [2], 'function': replace_string_in_file}
}


if __name__ == '__main__':

    try:
        validate_command(sys.argv, command_rules)
        validate_arguments(sys.argv, command_rules)

        command = sys.argv[1]
        command_args = sys.argv[2:]
        print(command_args)
        command_function = command_rules[command]['function']
        command_function(command_args)

    except ValidationError as err:
        sys.stderr.buffer.write(b'Error: ' + str(err).encode() + b'\n')
        sys.stderr.flush()
        sys.exit(1)

