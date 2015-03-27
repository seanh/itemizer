[![Latest Version](https://pypip.in/version/itemizer/badge.svg)](https://pypi.python.org/pypi/itemizer/)
[![Downloads](https://pypip.in/download/itemizer/badge.svg)](https://pypi.python.org/pypi/itemizer/)
[![Supported Python versions](https://pypip.in/py_versions/itemizer/badge.svg)](https://pypi.python.org/pypi/itemizer/)
[![Development Status](https://pypip.in/status/itemizer/badge.svg)](https://pypi.python.org/pypi/itemizer/)
[![License](https://pypip.in/license/itemizer/badge.svg)](https://pypi.python.org/pypi/itemizer/)


itemizer
========

A [dmenu](http://tools.suckless.org/dmenu/) wrapper script that:

1. Lets you define menu items as `key: value` pairs in a
   [YAML](http://yaml.org/) file, like:

        Firefox: firefox
        Terminal: gnome-terminal
        Nautilus: nautilus --no-desktop --new-window

   The keys are what will be shown in dmenu. The values are the commands that
   will be run when you select the keys from dmenu. Unlike the usual way of
   using dmenu, the items shown in the menu don't have to be the same as the
   commands executed when they're selected.

2. Sorts the items in dmenu most-recently-used first (not yet implemented!)


Installation
------------

    pip install itemizer


Usage
-----

    itemizer_run

It accepts all the same command-line arguments as dmenu:

    itemizer_run -f -i -nb "#222222" -nf "#bbbbbb" -sb "#005577" -sf "#eeeeee" -fn "-*-terminus-medium-r-*-*-16-*-*-*-*-*-*-*"

To customize the menu copy the [default itemizer.yaml file](itemizer/itemizer.yaml) to `~/.itemizer.yaml`
and edit it.

Itemizer is composed of two subcommands:

1. `itemizer list` prints a newline-separated list of all the keys from your
   items file to stdout, suitable for piping into dmenu.

2. `itemizer show` reads a key from stdin, looks up its value in your items
   file, and prints it to stdout. Pipe the output from dmenu into
   `itemizer show`, then pipe the ouput from `itemizer show` to `sh`.

Run `itemizer -h` for complete documentation of the options and subcommands.

[itemizer_run](bin/itemizer_run) is a shell script that ties `itemizer list`, `dmenu`,
`itemizer show` and `sh` together, and that passes any command-line arguments
that you pass it on to dmenu.
