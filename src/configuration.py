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