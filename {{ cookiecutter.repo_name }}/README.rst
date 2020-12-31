{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}{{"="}}{% endfor %}

{{ cookiecutter.project_short_description }}
{% if cookiecutter.gh_actions == 'yes' %}
.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/workflows/build/badge.svg?branch=master
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/actions
{%- endif %}

.. contents:: Contents
  :local:
  :depth: 1
  :backlinks: none

Summary
-------

.. todo::

    * Add a brief summary of this project.


The ``{{ cookiecutter.script_name }}.py`` script itself can be found in the ``src/{{ cookiecutter.package_name }}/`` sub-directory.

Please note that this script can also be run from this project's ``{{ cookiecutter.package_name }}`` package

Command Line Usage
------------------

To invoke this Python script, simply run ``python {{ cookiecutter.script_name }}.py``.

Additionally, this script can also be run from the CLI entry-point ``{{ cookiecutter.command_line_interface_bin_name }}`` if the overarching ``{{ cookiecutter.package_name }}`` python application (i.e. package) is installed locally.

Running the script's ``--help`` command with ``python {{ cookiecutter.script_name }}.py -h`` will provide the following usage intructions::

  ADD STDOUT USAGE INSTRUCTIONS AS THEY APPEAR IN THE TERMINAL

.. todo::

   * Add stdout usage instructions to the code block above.

0. Ensure system requirements are met
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Clone this repository locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2. Install the required environment using Pipenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. _development:

Adding to this project
----------------------

If you'd like clone and build off of this project, below are some important notes regarding the configuration of this project.

.. contents:: In this section
  :local:
  :backlinks: none

.. todo::

    * Below are placeholder sections for explaining important characteristics of this project's configuration.
    * This section should contain all details required for someone else to easily begin adding additional development and analyses to this project.

Project repository directory structure, design, and usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The repository structure, packaging, and workflows for this project are largely based on the conventions used in the ``cc-pyscript`` Cookiecutter template `available here <https://github.com/sedelmeyer/cc-pyscript>`_.

Python package configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This package is configured via the ``setup.py`` and ``setup.cfg`` files found in this repository. The source code for this package is located in the ``src/{{ cookiecutter.package_name }}/`` directory. For general information on the benefits to this approach for packaging a Python library, please `see this article <https://blog.ionelmc.ro/2014/05/25/python-packaging/>`_.

Testing
^^^^^^^

This project is configured for automated testing using ``tox``{% if cookiecutter.gh_actions == 'yes' %} and continuous integration services via GitHub Actions{% endif %}. Additionally, the ``pytest`` test-runner is used for running the associated test suite located in the ``tests/`` directory.

* If you are new to ``tox``, please see `the official Tox documentation <https://tox.readthedocs.io/en/latest/>`_.
{% if cookiecutter.gh_actions == 'yes' %}
* If you are new to GitHub Actions, additional information `can be found here <https://github.com/features/actions>`_.
{%- endif %}
* If you are new to ``pytest``, please see `the official pytest documentation <https://docs.pytest.org/en/stable/index.html>`_. 

Project versioning
^^^^^^^^^^^^^^^^^^

This project is configured to use ``setuptools_scm`` to manage and track the project's current release version. By using ``setuptools_scm``, this project's ``setup.py`` pulls the version number directly from the latest ``git`` tag associated with the project. Therefore, instead of manually setting a global ``__version__`` variable in the application, you simply add a tag when commiting a new version of this project to the ``master`` branch.

* If you are new to ``setuptools_scm``, please see `the official documentation <https://pypi.org/project/setuptools-scm/>`_.

Documentation using Sphinx and reStructuredText
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo::

   * If this project is complex enough to require the use of full-fledged Sphinx documentation, add details here.

.. _issues:

Questions or issues related to this project
-------------------------------------------

Questions or issues related to this project can be submitted as an "issue" via the GitHub repository at: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/issues

.. todo::

    * Add details on the best method for others to reach you regarding questions they might have or issues they identify related to this project.


.. _sources:

Sources and additional resources
--------------------------------

.. todo::

    * Add links to further reading and/or important resources related to this project.
