"""Utility script to parse .ctl files and summarize their metadata."""

import os
from tabulate import tabulate


def parse_ctl_summary(filepath):
    """Parse a .ctl file and extract metadata for summary."""

    metadata = {
        "file": os.path.basename(filepath),
        "title": "",
        "xdef": 0,
        "ydef": 0,
        "zdef": 0,
        "tdef": 0,
        "var_count": 0,
        "variables": [],
        "variables_description": [],
        "data file": "",
    }

    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()

    in_vars_block = False
    for line_number, line in enumerate(lines):
        line = line.strip()

        metadata["S.No."] = line_number + 1

        if line.lower().startswith("title"):
            metadata["title"] = line.split(None, 1)[1]
        elif line.lower().startswith("xdef"):
            metadata["xdef"] = int(line.split()[1])
        elif line.lower().startswith("ydef"):
            metadata["ydef"] = int(line.split()[1])
        elif line.lower().startswith("zdef"):
            metadata["zdef"] = int(line.split()[1])
        elif line.lower().startswith("tdef"):
            metadata["tdef"] = int(line.split()[1])
        elif line.lower().startswith("vars"):
            in_vars_block = True
            continue
        elif line.lower().startswith("endvars"):
            in_vars_block = False
            continue
        elif in_vars_block:
            parts = line.split()
            if len(parts) >= 4:
                var_name = parts[0]
                var_description = " ".join(parts[3:])
                metadata["variables"].append(var_name)
                metadata["variables_description"].append(var_description)

        elif line.lower().startswith("dset"):
            parts = line.split()
            if len(parts) > 1:
                metadata["data file"] = parts[1][1:]  # Remove leading '^'

    metadata["var_count"] = len(metadata["variables"])
    return metadata


def summarize_all_ctl_files(folder):
    """Summarize all .ctl files in a given folder."""

    rows = []
    for file in os.listdir(folder):
        if file.endswith(".ctl"):
            path = os.path.join(folder, file)
            meta = parse_ctl_summary(path)
            rows.append(
                [
                    meta["file"],
                    meta["title"],
                    meta["xdef"],
                    meta["ydef"],
                    meta["zdef"],
                    meta["tdef"],
                    meta["var_count"],
                    ", ".join(
                        [
                            f"{var} ({desc})"
                            for var, desc in zip(
                                meta["variables"],
                                meta["variables_description"],
                            )
                        ]
                    ),
                    meta["data file"],
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
    return tabulate(rows, headers, tablefmt="github")


# Example usage
FOLDER = "input/"
input_table = summarize_all_ctl_files(FOLDER)
print(input_table)

FOLDER = "experiments/benchmark_pictrl/"
output_table = summarize_all_ctl_files(FOLDER)
print(output_table)

# Save the markdown table to a file
MARKDOWN_FILE = "ctl_summary.md"
with open(MARKDOWN_FILE, "w", encoding="utf-8") as f:
    f.write("# Input Summary\n\n")
    f.write(input_table)
    f.write("\n\n# Output Summary\n\n")
    f.write(output_table)
