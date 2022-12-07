import argparse
import sys
from typing import Optional, List


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser("Skeleton")
    parser.add_argument("--names", nargs="*", default=["Elvis"], help="names to greet")
    args = parser.parse_args(argv)

    for name in args.names:
        print(f"Greetings {name} !")

    return 0

if __name__ == "__main__":
    sys.exit(main())