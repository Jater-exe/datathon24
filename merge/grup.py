import json
import pathlib
import uuid
from dataclasses import dataclass
from typing import Dict, List, Literal


@dataclass
class Grup:
    id: uuid.UUID  # Unique identifier

    #Group info
    group_size: 1
    #group_UID: str
    group_members: List[str]
    full_group: bool

def load_groups(path: str) -> List[Grup]:
    if not pathlib.Path(path).exists():
        raise FileNotFoundError(
            f"The file {path} does not exist, are you sure you're using the correct path?"
        )
    if not pathlib.Path(path).suffix == ".json":
        raise ValueError(
            f"The file {path} is not a JSON file, are you sure you're using the correct file?"
        )

    return [Grup(**grup) for grup in json.load(open(path))]

