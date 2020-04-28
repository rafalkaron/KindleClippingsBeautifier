# coding: utf-8
"""
Export a \"My Clippings.txt\" Kindle file to HTML5.
"""

import sys
import re
import os
import argparse
from Klipps import (read_file,
                    clipps_str_to_html_str,
                    style_html_str,
                    save_str_as_file,
                    open_file,
                    progressbar as pb)

__version__ = "0.6"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

def main():
    pb(0)
    par = argparse.ArgumentParser(description="Convert your Kindle clippings to HTML.")
    par.add_argument('clipps_path', help=r'A file path to the "My Clippings.txt" file on your Kindle device that you want to convert to HTML. For example: "D:\Kindle\Documents\My Clippings.txt" (Windows) or "/Volumes/Kindle/documents/My Clippings.txt" (macOS). Remember to encapsulate the path in inverted commas!')
    par.add_argument("-nopr", "--no_preview", action="store_true", help="Prevents the converted files from opening.")
    par.add_argument("-ns", "--no_style", action = "store_true",help="Does not style the HTML file by embedding CSS syntax.")
    try:
        args = par.parse_args()
    except:
        par.print_help()
        sys.exit(0)
    pb(10)
    html_str = clipps_str_to_html_str(read_file(args.clipps_path))
    pb(25)    
    html_path = args.clipps_path.replace(".txt", ".html")
    pb(50)    
    if not args.no_style:
        html_str = style_html_str(html_str)
    pb(75)
    publish_html5 = save_str_as_file(html_str, html_path)
    pb(90)
    if not args.no_preview:
        open_file(publish_html5)
    pb(100)
    print(f"Succesfully converted Kindle Clippings to: \"{html_path}\"")

if __name__ == "__main__":
    main()