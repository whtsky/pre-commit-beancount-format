import argparse

from beancount.scripts.format import align_beancount


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-w",
        "--prefix-width",
        type=int,
        help="Use this prefix width instead of determining an optimal value automatically",
    )
    parser.add_argument(
        "-W",
        "--num-width",
        type=int,
        help="Use this width to render numbers instead of determining an optimal value",
    )
    parser.add_argument(
        "-c", "--currency-column", type=int, help="Align currencies in this column."
    )
    parser.add_argument("filename", nargs="*")
    args = parser.parse_args()

    for filename in args.filename:
        with open(filename, "r") as f:
            content = f.read()
        formatted_contents = align_beancount(
            content,
            prefix_width=args.prefix_width,
            num_width=args.num_width,
            currency_column=args.currency_column,
        )
        if formatted_contents != content:
            with open(filename, "w") as f:
                f.write(formatted_contents)
