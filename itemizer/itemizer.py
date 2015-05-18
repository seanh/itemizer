#!/usr/bin/env python2
"""A dmenu wrapper script."""
import argparse
import yaml
import os
import sys


def read_items_file(items_file):
    """Return the items from the items file as a dict."""

    def _items(items_file):
        items_file = os.path.abspath(os.path.expanduser(items_file))
        return yaml.load(open(items_file, "r").read())

    using_default = False
    if items_file is None:
        using_default = True
        items_file = "~/.itemizer.yaml"

    try:
        return _items(items_file)
    except IOError as err:
        if err.errno == 2 and using_default:
            # If no file is given on the command line and there's none at
            # the default path, fall back on the example itemizer.yaml that
            # ships with the code.
            here = os.path.split(sys.modules[__name__].__file__)[0]
            items_file = os.path.join(here, "itemizer.yaml")
            return _items(items_file)
        else:
            # Don't crash if a user-specified items file doesn't exist.
            return {}


def read_items_files(items_files):
    """Return the items from the items files as a dict.

    If two items files both contain items with the same key, the item from the
    file later in the list will overwrite the earlier one.

    """
    items_files = items_files or []
    items = {}
    for items_file in items_files:
        items.update(read_items_file(items_file))
    return items


def list_keys(items_files):
    """Return a newline-separated list of the keys from ``items_files``."""
    items = read_items_files(items_files)
    return "\n".join(key for key in items.keys())


def show_value(items_files, key):
    """Return the value for the given ``key`` from the ``items_files``."""
    return read_items_files(items_files).get(key, key)


def main():
    """Parse and return the command-line arguments."""
    parser = argparse.ArgumentParser()

    def list_keys_(args):
        return list_keys(args.items_files)

    def show_value_(args):
        return show_value(args.items_files, sys.stdin.read().strip())

    subparsers = parser.add_subparsers()

    list_parser = subparsers.add_parser(
        "list", help="list the keys from the items file")
    list_parser.set_defaults(func=list_keys_)

    show_parser = subparsers.add_parser(
        "show",
        help="read a key from stdin and print its value from the items file")
    show_parser.set_defaults(func=show_value_)

    for sub_parser in (list_parser, show_parser):
        sub_parser.add_argument(
            "-i", "--items-files", default=None, nargs='*',
            help="a space-separated list of the YAML files containing the "
                 "menu items")

    args = parser.parse_args()
    print args.func(args)


if __name__ == "__main__":
    main()
