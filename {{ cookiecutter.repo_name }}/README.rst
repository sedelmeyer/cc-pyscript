{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}{{"="}}{% endfor %}

{{ cookiecutter.project_short_description }}
{% if cookiecutter.gh_actions == 'yes' %}
.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/workflows/build/badge.svg?branch=master
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/actions
{% else -%}
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

Python package configuration and associated workflows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Testing
^^^^^^^

Version control and git workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Documentation using Sphinx and reStructuredText
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _issues:

Questions or issues related to this project
-------------------------------------------

.. todo::

    * Add details on the best method for others to reach you regarding questions they might have or issues they identify related to this project.


.. _sources:

Sources and additional resources
--------------------------------

.. todo::

    * Add links to further reading and/or important resources related to this project.
