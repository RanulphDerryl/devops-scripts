# utils.py

import os
import logging
from typing import List

# Define a logger for the module
logger = logging.getLogger(__name__)

def get_environment_variables() -> dict:
    """
    Returns a dictionary containing environment variables.
    """
    env_variables = {
        key: os.environ.get(key)
        for key in os.environ
    }
    return env_variables

def load_yaml_file(file_path: str) -> dict:
    """
    Loads a YAML file into a dictionary.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        dict: A dictionary containing the YAML file contents.
    """
    import yaml
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML file: {e}")
        raise

def validate_yaml_structure(data: dict) -> None:
    """
    Validates the structure of a YAML file.

    Args:
        data (dict): The YAML file contents as a dictionary.
    """
    required_keys = ['key1', 'key2']  # Define required keys here
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")

def list_files(directory: str, extension: str = '') -> List[str]:
    """
    Returns a list of files in a directory with a specified extension.

    Args:
        directory (str): Directory path.
        extension (str): File extension (optional).

    Returns:
        List[str]: A list of file paths.
    """
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"{directory} is not a directory")
    if extension:
        return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(extension)]
    return [os.path.join(directory, file) for file in os.listdir(directory)]