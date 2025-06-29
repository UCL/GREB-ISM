"""Module for handling file operations."""

import os

from dataclasses import dataclass, field
from warnings import warn


@dataclass
class File:
    """A class to represent a file with its path, directory, filename, stem, and extension."""

    path: str
    to_be_created: bool = False
    directory: str = field(init=False)
    filename: str = field(init=False)
    stem: str = field(init=False)
    extension: str = field(init=False)

    def __post_init__(self):
        """Initialize the file object with stem and extension."""

        self.path = self.path.strip()
        if not self.path:
            raise ValueError("File path cannot be empty.")

        if self.to_be_created:

            if not os.path.exists(self.path):
                try:
                    os.makedirs(os.path.dirname(self.path), exist_ok=True)
                    open(self.path, "a", encoding="utf-8").close()
                except OSError as e:
                    raise OSError(f"Could not create file: {self.path}.") from e

            else:
                warn(f"File already exists: {self.path}. No action taken.")

        if not os.path.exists(self.path):
            raise FileNotFoundError(f"File not found: {self.path}")

        self.directory, self.filename = os.path.split(self.path)
        self.stem, self.extension = os.path.splitext(self.filename)
        self.extension = self.extension.lstrip(".")

    def __str__(self):
        """Return the string representation of the file."""
        return self.path

    def __repr__(self):
        """Return the string representation of the file."""
        return f"File(path={self.path})"
