"""Module to summarize .ctl files in a directory and generate a variable table."""

import os


from tabulate import tabulate

from utility.file_handler.ctl import CTLFile


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


def main():
    """Main function to summarize input and output .ctl files."""

    folder = "input/"
    input_table = summarize_all_ctl_files(folder)

    folder = "experiments/benchmark_pictrl/"
    output_table = summarize_all_ctl_files(folder)

    # Save the markdown table to a file
    output_file = "ctl_summary.rst"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Input Summary\n\n")
        f.write(input_table)
        f.write("\n\n# Output Summary\n\n")
        f.write(output_table)


if __name__ == "__main__":
    main()
