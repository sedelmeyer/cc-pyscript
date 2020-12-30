import argparse
import shlex
import subprocess
from unittest import TestCase

import {{ cookiecutter.package_name }}.{{ cookiecutter.script_name }} as {{ cookiecutter.script_name }}


class TestArgparseUserOptions(TestCase):
    """Tests that ArgparseUserOptions class functions as expected"""

    def setUp(self):
        self.test_description = "Test description"
        self.test_args = ["arg1", "arg2"]
        self.test_args_dict = {
            arg: {
                "flags": [arg], "options": {"type": str}
                } for arg in self.test_args
        }
        self.test_inputs = ["test{}".format(i) for i in range(len(self.test_args_dict))]
        self.UserOptions = {{ cookiecutter.script_name }}.ArgparseUserOptions(
            "test", [self.test_args_dict]
        )

    def test_add_args_dict_returns_parser(self):
        """Ensure add_args_dict returns parser with input dict args"""
        parser = argparse.ArgumentParser()
        parser = self.UserOptions.add_args_dict(parser, self.test_args_dict)
        args = parser.parse_args(self.test_inputs)
        self.assertIsInstance(parser, argparse.ArgumentParser)
        for arg in self.test_args:
            self.assertTrue(arg in dir(args))

    def test_add_args_returns_parser(self):
        """Ensure add_args returns parser with input dict args"""
        parser = argparse.ArgumentParser()
        parser = self.UserOptions.add_args(parser, [self.test_args_dict])
        args = parser.parse_args(self.test_inputs)
        self.assertIsInstance(parser, argparse.ArgumentParser)
        for arg in self.test_args:
            self.assertTrue(arg in dir(args))

    def test_generate_parser_returns_parser(self):
        """Ensure generate parser returns parser"""
        test_epilog = "Test epilog"
        parser = self.UserOptions.generate_parser(
            self.test_description, [self.test_args_dict], test_epilog
        )
        self.assertIsInstance(parser, argparse.ArgumentParser)
        self.assertEqual(parser.description, self.test_description)
        self.assertEqual(parser.epilog, test_epilog)

    def test_generate_parser_returns_parser_no_dict_list_or_epilog(self):
        """Ensure generate_parser returns parser when no dict_list or epilog provided"""
        test_epilog = None
        parser = self.UserOptions.generate_parser(self.test_description)
        self.assertIsInstance(parser, argparse.ArgumentParser)
        self.assertEqual(parser.description, self.test_description)
        self.assertEqual(parser.epilog, test_epilog)

    def test_init_parser_attribute_exists(self):
        """Ensure self.parser attribute exists after class initialization"""
        self.assertIsInstance(self.UserOptions.parser, argparse.ArgumentParser)

    def test_parse_args_returns_args(self):
        """Ensure parse_arges returns parsed args"""
        args = self.UserOptions.parse_args(self.test_inputs)
        for arg in self.test_args:
            self.assertTrue(arg in args)
        for val, arg in zip(self.test_inputs, [args.arg1, args.arg2]):
            self.assertEqual(val, arg)


class TestMainCLI(TestCase):
    """Test main functions as expected from command line"""

    def test_cli_argparse_help(self):
        """Ensure main CLI default argparse produces help docs with all relevant args"""
        # delete try-except logic and keep only first subprocess call shown below
        # this try-except is only required for testing the original cc-pyscript template
        try:
            result = subprocess.check_output(
                shlex.split(
                    "{{ cookiecutter.command_line_interface_bin_name }} -h"
                )
            )
        except FileNotFoundError:
            result = subprocess.check_output(
                shlex.split(
                    "python {{ cookiecutter.package_name }}/{{ cookiecutter.script_name }}.py -h"
                )
            )
        self.assertTrue({{ cookiecutter.script_name }}.parser_description in str(result))
        for args_dict in [
            {{ cookiecutter.script_name }}.required_args_dict,
            {{ cookiecutter.script_name }}.optional_args_dict,
        ]:
            for sub_dict in args_dict.values():
                for flag in sub_dict["flags"]:
                    self.assertTrue(flag in str(result))
