"""CLI"""

import argparse

from topn.topn import Topn


class Cli:
    """CLI"""

    def __init__(self):
        self.args = self._parse_args()

    def _parse_args(self):
        """Parses args"""

        parser = argparse.ArgumentParser()
        parser.add_argument("-p", "--path")
        parser.add_argument("-c", "--count", type=int, default=10)

        return parser.parse_args()

    def run(self):
        """Runs CLI"""

        topn = Topn(self.args.path).top(self.args.count)
        print("\n".join(topn), end="")
