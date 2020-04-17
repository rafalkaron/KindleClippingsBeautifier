# coding: utf-8
"""
Export your Kindle Clippings to a nice PDF.
"""

__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

from dirs import enter_filepath
from read import read_file

filepath = enter_filepath()
file_lines = read_file(filepath)

def convert_to_markdown(file_lines):
    """Marks up a list of Kindle Clipping lines with Markdown Syntax"""
    print(file_lines)
    #return markdown

def save(markdown_file):
    """Saves a Markdown file"""


def main():
    #read_file(filepath)
    convert_to_markdown(file_lines)

if __name__ == "__main__":
    main()