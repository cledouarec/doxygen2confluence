#! python3

"""
Main script entry point to convert Doxygen documentation to Confluence pages.
"""

from doxygen2confluence.cli import main


if __name__ == "__main__":
    # Entry point of converter script.
    # Execute only if run as a script.
    main()
