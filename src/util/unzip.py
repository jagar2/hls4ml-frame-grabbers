import zipfile
import os

def unzip_file(zip_file_path, extract_to=None):
    """
    Unzips a zip file to the specified directory.

    Args:
        zip_file_path (str): The path to the zip file.
        extract_to (str, optional): The directory to extract the files to. If not provided, the files will be extracted to the same directory as the zip file.

    Returns:
        str: The directory where the files were extracted to.
    """
    try:
        # if extract_to is None:
        #     extract_to = os.path.dirname(zip_file_path)

        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

        return extract_to
    
    except Exception as e:
        print(f"Error occurred while unzipping file: {str(e)}")
        return None
