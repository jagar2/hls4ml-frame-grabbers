def gen_stripe_pattern(NUM_STRIPES):
    """
    Generate a stripe pattern based on the number of stripes.

    Args:
        NUM_STRIPES (int): The number of stripes in the pattern.

    Returns:
        list: A list representing the order of the stripes.

    Raises:
        None

    """
    if NUM_STRIPES % 2 != 0:
        print("NUM_STRIPES must be even")
        return None
    
    stripe_order = []
    for i in range(NUM_STRIPES):
        if i % 2 == 0:
            # Calculate the index for even stripes
            stripe_order.append(((NUM_STRIPES // 2) - (i // 2)) - 1)
        else:
            # Calculate the index for odd stripes
            stripe_order.append(((NUM_STRIPES // 2) + ((i + 1) // 2)) - 1)
    
    return stripe_order

def replace_stripe_order(file_path, stripe_order):
    """
    Replaces the specific line in CustomLogic.h that contains the placeholder comment with the new stripe order array.

    Args:
        file_path (str): The path to the CustomLogic.h file.
    """
    
    # Define the start of the line and the new line to replace it with
    line_start = "static const unsigned stripe_order[NUM_STRIPES]"
    new_line = f"static const unsigned stripe_order[NUM_STRIPES] = {stripe_order};"

    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Replace the line
    with open(file_path, 'w') as file:
        for line in lines:
            if line.startswith(line_start):
                file.write(new_line + "\n")
                print(f"{line} replaced with {new_line}")
            else:
                file.write(line)