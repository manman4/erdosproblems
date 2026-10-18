#!/usr/bin/env python3
"""Regenerate the fork's progress charts from the current history CSV.

The upstream chart images remain frozen; these images are displayed only on
PROGRESS.md in the manman4 fork.
"""

import plot_statistics_history as history


def main():
    history.OUTPUT_LIGHT = history.ROOT / "data" / "fork_statistics_history_light.svg"
    history.OUTPUT_DARK = history.ROOT / "data" / "fork_statistics_history_dark.svg"
    history.generate_charts(force=True)


if __name__ == "__main__":
    main()
