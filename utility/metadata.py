"""Module to handle metadata operations for CTL files."""

import os
from dataclasses import dataclass, field


@dataclass
class Metadata:
    """A class to represent metadata extracted from a CTL file."""

    file_path: str
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
        self.file_path = self.file_path.strip()

        with open(self.file_path, "r", encoding="utf-8") as ctl_file:
            lines = ctl_file.readlines()
        self.parse_ctl_summary(lines)

    @property
    def file(self) -> str:
        """Return the file name from the file path."""
        return os.path.basename(self.file_path)

    @property
    def directory(self) -> str:
        """Return the directory of the file."""
        return os.path.dirname(self.file_path)

    def parse_ctl_summary(self, lines: list[str]) -> None:
        """Parse a list of lines from a CTL file and extract metadata for summary."""
        in_vars_block = False

        for line in lines:
            line = line.strip()

            if line.lower().startswith("title"):
                self.title = line.split(None, 1)[1]
            elif line.lower().startswith("xdef"):
                self.xdef = int(line.split()[1])
            elif line.lower().startswith("ydef"):
                self.ydef = int(line.split()[1])
            elif line.lower().startswith("zdef"):
                self.zdef = int(line.split()[1])
            elif line.lower().startswith("tdef"):
                self.tdef = int(line.split()[1])
            elif line.lower().startswith("vars"):
                in_vars_block = True
            elif in_vars_block and not line.startswith("#") and not line == "":
                parts = line.split()
                if len(parts) >= 4:
                    var_name = parts[0]
                    var_desc = " ".join(parts[3:])
                    self.variables.append(var_name)
                    self.variables_description.append(var_desc)
                    self.var_count += 1
            elif in_vars_block and line.startswith("endvars"):
                in_vars_block = False
            elif line.lower().startswith("dset"):

                if len(line.split()) > 1:
                    if line.split()[1].startswith("^"):
                        self.data_file = line.split()[1][1:]
                    else:
                        self.data_file = line.split()[1]
                else:
                    self.data_file = "Unknown"

                self.data_file = self.data_file.strip()
