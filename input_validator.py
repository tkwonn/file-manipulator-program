import os


class ValidationError(Exception):
    pass


def is_positive_integer(value):
    try:
        return int(value) > 0
    except ValueError:
        raise ValidationError("Number must be an integer and greater than 0.")
    

def validate_command(args, command_rules):
    if len(args) < 2:
        raise ValidationError(f"It must include a command.")
    if args[1] not in command_rules:
        raise ValidationError(f"{args[1]} is not supported.")

    return True


def validate_arguments(args, command_rules):    
    command = args[1]

    # Check if the correct number of arguments are provided for each command
    if len(args) != command_rules[command]['arg_count']:
        raise ValidationError(f"{command} requires exactly {command_rules[command]['arg_count'] - 1} arguments.")
    
    # Check if file paths provided in the command arguments are valid
    for index in command_rules[command].get('file_checks', []):
        if os.path.isfile(args[index]) == False:
            raise ValidationError(f"Argument {index-1} is not a valid file path.")
    
    # Check for any additional rules
    for index, func in command_rules[command].get('additional_checks', []):
        if not func(args[index]):
            pass
    
    return True