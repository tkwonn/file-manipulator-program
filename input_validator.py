import os


class ValidationError(Exception):
    """Exception raised for errors in the input."""
    pass


def is_positive_integer(value):
    """
    Checks if the value is a positive integer.

    Args:
        value (str): The value to be checked.

    Returns:
        bool: True if the value is a positive integer, otherwise raises a ValidationError.
    """
    try:
        return int(value) > 0
    except ValueError:
        raise ValidationError("Number must be an integer and greater than 0.")
    

def validate_command(args, command_rules):
    """
    Validate the command.

    Args:
        args (list): The list of arguments provided in the command line.
        command_rules (dict): The rules for each command.

    Returns:
        bool: True if the command is valid, otherwise raises a ValidationError.
    """
    COMMAND_INDEX = 1
    if len(args) < 2:
        raise ValidationError(f"The command is missing. Please provide a command as the second argument.")
    if args[1] not in command_rules:
        raise ValidationError(f"{args[COMMAND_INDEX]} is not supported.")

    return True


def validate_arguments(args, command_rules):
    """
    Validate the command arguments.

    Args:
        args (list): The list of arguments provided in the command line.
        command_rules (dict): The rules for each command.

    Returns:
        bool: True if the arguments are valid, otherwise raises a ValidationError.
    """
    COMMAND_INDEX = 1
    command = args[COMMAND_INDEX]

    # Check if the correct number of arguments are provided for each command
    if len(args) != command_rules[command]['arg_count']:
        raise ValidationError(f"{command} requires exactly {command_rules[command]['arg_count'] - COMMAND_INDEX} arguments.")
    
    # Check if file paths provided in the command arguments are valid
    for index in command_rules[command].get('file_checks', []):
        if not os.path.isfile(args[index]):
            raise ValidationError(f"{args[index]} is not a valid file path.")
    
    # Check for any additional rules
    for index, func in enumerate(command_rules[command].get('additional_checks', [])):
        if not func(args[index]):
            pass
    
    return True