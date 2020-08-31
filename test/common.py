from typing import Dict
from pathlib import Path
import json


def read_json_fixture(filename: str) -> Dict[str, str]:
    """Read a JSON file from the "fixtures" directory.
    
    :param filename: A file name including the JSON extension.
    :return: The file contents deserialized into a dictionary.
    """
    fixture_path = Path(__file__).resolve().parents[0] / f"fixtures/{filename}"
    with open(fixture_path, mode="r") as f:
        data = json.load(f)
    return data
