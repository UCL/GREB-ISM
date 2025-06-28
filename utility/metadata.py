"""Module to handle metadata operations for CTL files."""

from dataclasses import dataclass, field


@dataclass
class Metadata:
    """A class to represent metadata extracted from a CTL file."""

    file: str
    title: str = ""
    xdef: int = 0
    ydef: int = 0
    zdef: int = 0
    tdef: int = 0
    var_count: int = 0
    variables: list[str] = field(default_factory=list)
    variables_description: list[str] = field(default_factory=list)
    data_file: str = ""

    def __post_init__(self):
        """Initialize the metadata with the file name."""
        self.file = self.file.strip()
