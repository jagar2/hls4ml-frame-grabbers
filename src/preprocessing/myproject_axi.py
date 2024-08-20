from ..util.textedit import replace_line, multiline_replace_line

def replace_model_out_depth(file_path, value):
    """
    Replaces the specific line in myproject_axi.h that contains the placeholder comment with the new stripe order array.

    Args:
        file_path (str): The path to the myproject_axi.h file.
    """
    
    # Define the start of the line and the new line to replace it with
    line_start = "    static const unsigned MODEL_OUT_DEPTH ="
    new_line = f"    static const unsigned MODEL_OUT_DEPTH = {value};"
    
    replace_line(file_path, line_start, new_line)
    
def generate_pragma_lines(NUM_STRIPES, verbose=False):
    """
    Generates a list of HLS STREAM pragmas for network split array.
    Args:
        NUM_STRIPES (int): The number of stripes.
        verbose (bool, optional): Whether to print the generated pragma lines. Defaults to False.
    Returns:
        list: A list of HLS STREAM pragma lines for network split array.
    """
    string = []
    
    # adds started string
    string.append('/* START CustomLogic: INSERT NETWORK SPLIT ARRAY HLS STREAM PRAGMAS HERE (from jupyter notebook) */')
    
    for i in range(NUM_STRIPES):
        
        string_ = f'    #pragma HLS STREAM variable=input_arr_split_reordered[{i}] depth=PACKETS_PER_STRIPE'
        string.append(string_)
        if verbose:
            print(string_)
    
    # add finished string        
    string.append('/* END CustomLogic: INSERT NETWORK SPLIT ARRAY HLS STREAM PRAGMAS HERE (from jupyter notebook) */')
    
    return string


def replace_pragma_lines(file_path, NUM_STRIPES, verbose=False):
    """
    Replaces the specific line in myproject_axi.h that contains the placeholder comment with the new stripe order array.

    Args:
        file_path (str): The path to the myproject_axi.h file.
    """
    
    # Define the start of the line and the new line to replace it with
    
    line_start = "/* CustomLogic: INSERT NETWORK SPLIT ARRAY HLS STREAM PRAGMAS HERE (from jupyter notebook) */"
    new_lines = generate_pragma_lines(NUM_STRIPES, verbose)
    
    multiline_replace_line(file_path, line_start, new_lines)