import os
import glob

def check_customlogic_downloads(customlogic_download_dir):
    """
    Check for CustomLogic downloads in the specified directory.
    Raises FileNotFoundError if no CustomLogic downloads are found.
    Raises ValueError if more than one CustomLogic download is found or if the version is too old.
    """

    # Check for CustomLogic downloads
    customlogic_files = glob.glob(f"{customlogic_download_dir}/coaxlink-customlogic-*.zip")
    if not customlogic_files:
        raise FileNotFoundError("Error: No CustomLogic downloads found")
    else:
        valid_files = []
        for file in customlogic_files:
            base_name = os.path.basename(file)
            version_no = base_name[len("coaxlink-customlogic-"):].split('.')[0] 

            # Check version number
            if version_no.isdigit() and int(version_no) >= 24:
                valid_files.append(file)

        if len(valid_files) > 1:
            raise ValueError("Error: More than one CustomLogic download found. Please ensure only one CustomLogic download exists in the target directory.")    
        elif not valid_files:
            raise ValueError("Error: Your CustomLogic download is too old or another error occurred. Ensure you have CustomLogic version 24 or higher.")
        
    return valid_files 

def get_camera_model(board_type):
    """
    Returns the camera model based on the board type.

    Args:
        board_type (str): The type of board.

    Returns:
        str: The camera model corresponding to the board type.

    Raises:
        ValueError: If the board type is not one of the specified options.
    """

    # Mapping of board type to camera model
    board_to_model = {
        'octo': 'CoaxlinkOcto_1cam',
        'quad': 'CoaxlinkQuadCxp12_1cam',
        'qsfp': 'CoaxlinkQsfp_1cam'
    }

    if board_type in board_to_model:
        return board_to_model[board_type]
    else:
        raise ValueError("Error: please specify one of the following boards: \"octo\", \"quad\", \"qsfp\"")