import argparse

from beancount.scripts.format import align_beancount


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="*")
    args = parser.parse_args()

    for filename in args.filename:
        with open(filename, "r") as f:
            content = f.read()
        formatted_contents = align_beancount(content)
        if formatted_contents != content:
            with open(filename, "w") as f:
                f.write(formatted_contents)
