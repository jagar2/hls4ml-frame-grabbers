def print_dict(d, indent=0):
    """
    Recursively prints the key-value pairs of a dictionary with proper indentation.

    Args:
        d (dict): The dictionary to be printed.
        indent (int): The current level of indentation (default is 0).
    """
    align = 20
    for key, value in d.items():
        # Print the key with appropriate indentation
        print('  ' * indent + str(key), end='')

        if isinstance(value, dict):
            # If the value is a dictionary, print it on a new line with increased indentation
            print()
            print_dict(value, indent+1)
        else:
            # If the value is not a dictionary, print it with proper alignment
            print(':' + ' ' * (20 - len(key) - 2 * indent) + str(value))