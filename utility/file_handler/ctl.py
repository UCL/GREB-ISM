"""Module for handling CTL file operations."""

from dataclasses import dataclass, field

from utility.file_handler.base import File
from utility.metadata import Metadata


@dataclass
class CTLFile(File):
    """A class to represent a CTL file with additional metadata parsing."""

    metadata: Metadata = field(init=False)

    def __post_init__(self):
        """Initialize the CTL file object and parse metadata."""
        super().__post_init__()

        if self.extension.lower() != "ctl":
            raise ValueError(f"Expected a .ctl file, but got: {self.extension}")

        self.metadata = Metadata(file_path=self.path)
