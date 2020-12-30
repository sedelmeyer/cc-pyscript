#!/usr/bin/env python
"""
{{ cookiecutter.package_name }}.{{ cookiecutter.script_name }}
{% for _ in cookiecutter.package_name %}{{"~"}}{% endfor %}"~"{% for _ in cookiecutter.script_name %}{{"~"}}{% endfor %}

Add verbose script description.

REQUIREMENTS:

* Python>=3.7
* Only the Python Standard Library is required.

NOTES:

* This script can be run directly using ``python {{ cookiecutter.script_name }}.py``
* Alternatively, if the ``tech_grant`` package is installed locally,
  it can be accessed directly via the CLI entry-point
  ``{{ cookiecutter.command_line_interface_bin_name }}`` (see the ``{{ cookiecutter.package_name }}`` project's README for
  more detail at https://github.com/{{ cookiecutter.github_username }}/{{
  cookiecutter.repo_name }})
"""
import argparse
import sys

parser_description = "CLI script description"

required_args_dict = {
    "Required Arg 1": {
        "flags": ["flag_name_1"],
        "options": {
            "type": str,
            "help": "description of required arg 1",
        },
    },
    "Required Arg 2": {
        "flags": ["flag_name_2"],
        "options": {
            "type": str,
            "help": "description of required arg 2",
        },
    },
}

optional_args_dict = {
    "Optional Arg 1": {
        "flags": ["-f", "--flag"],
        "options": {
            "type": str,
            "default": "option 1",
            "choices": ["option 1", "option 2"],
            "help": 'description of optional arg, default="option 1"',
        },
    },
}


class ArgparseUserOptions:
    """Generate argparse user options for script CLI"""

    def __init__(self, description, args_dict_list=None, epilog=None):
        self.parser = self.generate_parser(description, args_dict_list, epilog)

    def generate_parser(self, description, args_dict_list=None, epilog=None):
        """Generates parser with all input arguments"""
        parser = argparse.ArgumentParser(
            description=description,
            epilog=epilog,
            formatter_class=argparse.RawDescriptionHelpFormatter,
        )

        if args_dict_list is not None:
            parser = self.add_args(parser, args_dict_list)

        return parser

    def add_args_dict(self, parser, args_dict):
        """Executes parser.add_argument for all args in and args_dict"""
        for arg, arg_dict in args_dict.items():
            parser.add_argument(*arg_dict["flags"], **arg_dict["options"])

        return parser

    def add_args(self, parser, args_dict_list):
        """Executes parser.add_argument for all args_dicts in an args_dict_list"""
        for args_dict in args_dict_list:
            parser = self.add_args_dict(parser, args_dict)

        return parser

    def parse_args(self, args):
        """Parses arguments based on CLI input"""
        return self.parser.parse_args(args)


def main():
    """Operations executed when calling this script from the command line"""
    args = ArgparseUserOptions(
        description=parser_description,
        args_dict_list=[required_args_dict, optional_args_dict],
        epilog=__doc__,
    ).parse_args(sys.argv[1:])

    return args


if __name__ == "__main__":
    main()
