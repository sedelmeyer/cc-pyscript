{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}{{"="}}{% endfor %}

{{ cookiecutter.project_short_description }}
{% if cookiecutter.travis == 'yes' %}
.. image:: https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?branch=master
    :target: https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
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
