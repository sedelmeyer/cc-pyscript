"""
This script contains the cookiecutter hooks that run immediately following the
generation of the ``cc-pydata`` template.

For more information about cookiecutter hooks, please see:
https://cookiecutter.readthedocs.io/en/1.7.2/advanced/hooks.html

"""

import os
import shutil

if __name__ == '__main__':

    if 'Not open source' == '{{ cookiecutter.license }}':
        os.remove('LICENSE')

    if 'no' == '{{ cookiecutter.gh_actions }}':
        shutil.rmtree('.github')

    if 'no' == '{{ cookiecutter.tox }}':
        os.remove('tox.ini')
