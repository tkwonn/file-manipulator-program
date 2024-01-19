import sys
import os

print("Argument list: ", str(sys.argv))

class ValidationError(Exception):
    pass

def is_positive_integer(value):
    try:
        return int(value) > 0
    except ValueError:
        raise ValidationError("Count must be an integer and greater than 0.")


# Define a structure for commands and their validation rules
command_rules = {
    'reverse': {'arg_count': 4, 'file_checks': [2,3]},
    'copy': {'arg_count': 4, 'file_checks': [2,3]},
    'duplicate-contents': {'arg_count': 4, 'file_checks': [2], 'additional_checks': [(3, is_positive_integer)]},
    'replace-string': {'arg_count': 5, 'file_checks': [2]}
}

def input_validator(args):
    command = args[1]
    command_info = command_rules[command]

    # Check if the correct number of arguments are provided for each command
    if len(args) != command_info['arg_count']:
        raise ValidationError(f"{command} requires exactly {command_info['arg_count'] - 1} arguments.")
    
    # Validate that the file paths refer to existing files
    for index in command_info.get('file_checks', []):
        if os.path.isfile(args[index]) == False:
            raise ValidationError(f"Argument {index} is not a valid file path.")
    
    # Check for any additional rules
    for index, func in command_info.get('additional_checks', []):
        if not func(args[index]):
            pass
    
    return True


def reverse_file_contents(args):
    try:
        input_validator(args)
    
        inputpath = args[2]
        outputpath = args[3]
        contents = ''

        with open(inputpath) as f:
            contents = f.read()
            
        with open(outputpath, 'w') as f:
            f.write(contents[::-1])

    except ValidationError as err:
        print(f"Error: {err}")
        return False
    
    return True
        

def copy_file_to_path(args):
    try:
        input_validator(args)

        inputpath = args[2]
        outputpath = args[3]

        with open(inputpath, 'r') as firstfile, open(outputpath, 'w') as secondfile:
            for line in firstfile:
                secondfile.write(line)

    except ValidationError as err:
        print(f"Error: {err}")
        return False
    
    return True


def duplicate_file_contents(args):
    try:
        input_validator(args)
    
        inputpath = args[2]
        count = args[3]
        contents = ''

        with open(inputpath, 'r') as f:
            contents = f.read()
            
        with open(inputpath, 'a') as f:
            for _ in range(int(count)):
                f.write(contents)

    except ValidationError as err:
        print(f"Error: {err}")
        return False
    
    return True


def replace_string_in_file(args):
    try:
        input_validator(args)
    
        inputpath = args[2]
        oldstring = args[3]
        newstring = args[4]
        contents = ''

        with open(inputpath, 'r') as f:
            contents = f.read()
            
        with open(inputpath, 'w') as f:
            f.write(contents.replace(oldstring, newstring))

    except ValidationError as err:
        print(f"Error: {err}")
        return False
    
    return True


if sys.argv[1] == 'reverse':
    reverse_file_contents(sys.argv)
elif sys.argv[1] == 'copy':
    copy_file_to_path(sys.argv)
elif sys.argv[1] == 'duplicate-contents':
    duplicate_file_contents(sys.argv)
elif sys.argv[1] == 'replace-string':
    replace_string_in_file(sys.argv)
else:
    print("We do not support argument {" + sys.argv[1] + "} at the moment.")

