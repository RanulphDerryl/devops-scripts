import os
import json
import logging
from typing import Dict, List

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config_file(file_path: str) -> Dict:
    """
    Load configuration from a JSON file.

    Args:
        file_path (str): Path to the configuration file.

    Returns:
        Dict: Loaded configuration.
    """
    with open(file_path, 'r') as f:
        return json.load(f)

def save_config_file(file_path: str, data: Dict) -> None:
    """
    Save configuration to a JSON file.

    Args:
        file_path (str): Path to the configuration file.
        data (Dict): Configuration data to save.
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def get_config_file_path() -> str:
    """
    Get the path to the configuration file.

    Returns:
        str: Path to the configuration file.
    """
    return os.path.join(os.path.dirname(__file__), 'config.json')

def get_config() -> Dict:
    """
    Get the configuration.

    Returns:
        Dict: Loaded configuration.
    """
    return load_config_file(get_config_file_path())

def save_config(config: Dict) -> None:
    """
    Save the configuration to a file.

    Args:
        config (Dict): Configuration data to save.
    """
    save_config_file(get_config_file_path(), config)