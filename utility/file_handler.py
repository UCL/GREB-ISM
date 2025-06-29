"""Module for handling file operations."""

import os

from dataclasses import dataclass, field
from warnings import warn

from tabulate import tabulate

from utility.metadata import Metadata


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


def summarize_all_ctl_files(folder):
    """Summarize all .ctl files in a given folder."""

    rows = []
    for file in os.listdir(folder):
        if file.endswith(".ctl"):

            ff = CTLFile(os.path.join(folder, file))
            meta = ff.metadata
            rows.append(
                [
                    meta.file,
                    meta.title,
                    meta.xdef,
                    meta.ydef,
                    meta.zdef,
                    meta.tdef,
                    meta.var_count,
                    ", ".join(
                        [
                            f"{var} ({desc})"
                            for var, desc in zip(
                                meta.variables,
                                meta.variables_description,
                            )
                        ]
                    ),
                    meta.data_file,
                ]
            )
    headers = [
        "File",
        "Title",
        "XDEF",
        "YDEF",
        "ZDEF",
        "TDEF",
        "VAR Count",
        "Variables",
        "Data File",
    ]
    return tabulate(rows, headers, tablefmt="rst")


if __name__ == "__main__":

    FOLDER = "input/"
    input_table = summarize_all_ctl_files(FOLDER)
    print(input_table)

    FOLDER = "experiments/benchmark_pictrl/"
    output_table = summarize_all_ctl_files(FOLDER)
    print(output_table)

    # Save the markdown table to a file
    MARKDOWN_FILE = "ctl_summary.rst"
    with open(MARKDOWN_FILE, "w", encoding="utf-8") as f:
        f.write("# Input Summary\n\n")
        f.write(input_table)
        f.write("\n\n# Output Summary\n\n")
        f.write(output_table)
