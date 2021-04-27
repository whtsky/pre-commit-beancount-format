import sys

from beancount.scripts.format import align_beancount


def main() -> None:
    for filename in sys.argv[1:]:
        with open(filename, "r") as f:
            content = f.read()
        formatted_contents = align_beancount(content)
        if formatted_contents != content:
            with open(filename, "w") as f:
                f.write(formatted_contents)
