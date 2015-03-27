#!/usr/bin/env python2
"""A dmenu wrapper script."""
import argparse
import yaml
import os
import sys


def read_items(items_file):
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
            raise


def list_keys(items_file):
    """Return a newline-separated list of the keys from the ``items`` dict."""
    items = read_items(items_file)
    return "\n".join(key for key in items.keys())


def show_value(items_file, key):
    """Return the value for the given ``key`` from ``items``."""
    return read_items(items_file).get(key, key)


def main():
    """Parse and return the command-line arguments."""
    parser = argparse.ArgumentParser()

    def list_keys_(args):
        return list_keys(args.items_file)

    def show_value_(args):
        return show_value(args.items_file, sys.stdin.read().strip())

    parser.add_argument(
        "-i", "--items-file", default=None,
        help="the YAML file containing the menu items")

    subparsers = parser.add_subparsers()

    list_parser = subparsers.add_parser(
        "list", help="list the keys from the items file")
    list_parser.set_defaults(func=list_keys_)

    show_parser = subparsers.add_parser(
        "show",
        help="read a key from stdin and print its value from the items file")
    show_parser.set_defaults(func=show_value_)

    args = parser.parse_args()
    print args.func(args)


if __name__ == "__main__":
    main()
