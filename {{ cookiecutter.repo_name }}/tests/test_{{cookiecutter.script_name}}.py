import sys
from unittest import TestCase

sys.path.append("..")
import {{ cookiecutter.script_name }} # noqa: E402


class TestPlaceholder(TestCase):
    """"""

    def test_placehoder(self):
        """"""
        self.assertTrue(True)
