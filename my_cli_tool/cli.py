"""my-cli-tool 命令行工具入口。"""

import argparse

__version__ = "0.1.0"


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="my-cli-tool",
        description="一个简洁的 Python 命令行工具示例",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "--name",
        default="World",
        help="要问候的名字",
    )
    args = parser.parse_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
