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


Command line usage
------------------

To invoke this Python script, simply run ``python {{ cookiecutter.script_name }}.py``.

Additionally, this script can also be run from the CLI entry-point ``{{ cookiecutter.command_line_interface_bin_name }}`` if the overarching ``{{ cookiecutter.package_name }}`` python application (i.e. package) is installed locally.

Running the script's ``--help`` command with ``python {{ cookiecutter.script_name }}.py -h`` will provide the following usage intructions::

  ADD STDOUT USAGE INSTRUCTIONS AS THEY APPEAR IN THE TERMINAL

.. todo::

   * Add stdout usage instructions to the code block above.


Getting started
---------------

.. _requirements:

0. Ensure system requirements are met
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The requirements for executing this script are:

* Python>=3.7

  * Python=3.6 will also likely work, but has not been tested.
  
  * Only the Python Standard Library is required.

Additional requirements for developing and testing this script, or installing the ``tech_grant`` package locally for running the CLI ``download-files`` entry-point directly are:

* ``pipenv``
  
  * ``pipenv, version 2020.8.13`` was used for developing this script, however older versions of ``pipenv`` will likely work.
  
  * If you prefer NOT to use ``pipenv`` for packaging and virtual environment management in favor of an alternative such as ``conda`` or ``virtualenv``, you will need to modify the project repository and ``.tox`` test matrix accordingly.

1. Clone this repository locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``src/{{ cookiecutter.package_name }}/{{ cookiecutter.script_name }}.py`` script can be used as a standalone document, therefore, the rest of the files included in this project repository are not technically required for its use. However, for development and testing of this script, it is recommended that the entire project repository be cloned locally from GitHub. This repository can be cloned with the following command::

  git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git

2. Install the required environment using Pipenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are new to using Pipenv for managing your working environments, please take some time to familiarize yourself with the tool. The `official Pipenv documentation <https://pipenv.pypa.io/en/latest/>`_ is a good place to start.

To install your Python dependencies directly from the deterministic build specified by the ``Pipfile.lock``, simply run::

  pipenv install --dev

Once your ``pipenv`` environment is built, you can enter it with::

  pipenv shell

As noted above in the requirements section, Pipenv is used to manage development requirements for this project. Pipenv is not necessarily required for just executing the script, because the script requires only the Python Standard Library to execute successfully.

**Troubleshooting:** It is possible that the frozen requirements specified in the ``Pipfile.lock`` may cause errors on some operating systems due to varying system-specific requirements needed to install ``pytest`` and some other development requirements. If you encounter this error, you may wish to delete your local version of the ``Pipfile.lock`` file and re-run ``pipenv install --dev``.


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

The repository structure, packaging, and workflows for this project are largely based on the conventions used in the ``cc-pyscript`` Cookiecutter template `available here <https://github.com/sedelmeyer/cc-pyscript>`_. Please read the documentation for that project for a complete overview of the tools and conventions used in the {{ cookiecutter.repo_name }} project.


Python package configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This package is configured via the ``setup.py`` and ``setup.cfg`` files found in this repository. The source code for this package is located in the ``src/{{ cookiecutter.package_name }}/`` directory. For general information on the benefits to this approach for packaging a Python library, please `see this article <https://blog.ionelmc.ro/2014/05/25/python-packaging/>`_.


Testing
^^^^^^^

This project is configured for automated testing using ``tox``{% if cookiecutter.gh_actions == 'yes' %} and continuous integration services via GitHub Actions{% endif %}. Additionally, the ``pytest`` test-runner is used for running the associated test suite located in the ``tests/`` directory.

* If you are new to ``pytest``, please see `the official pytest documentation <https://docs.pytest.org/en/stable/index.html>`_. 
* If you are new to ``tox``, please see `the official Tox documentation <https://tox.readthedocs.io/en/latest/>`_.
{% if cookiecutter.gh_actions == 'yes' %}
* If you are new to GitHub Actions, additional information `can be found here <https://github.com/features/actions>`_.
{%- endif %}


Project versioning
^^^^^^^^^^^^^^^^^^

This project is configured to use ``setuptools_scm`` to manage and track the project's current release version. By using ``setuptools_scm``, this project's ``setup.py`` pulls the version number directly from the latest ``git`` tag associated with the project. Therefore, instead of manually setting a global ``__version__`` variable in the application, you simply add a tag when commiting a new version of this project to the ``master`` branch.

* If you are new to ``setuptools_scm``, please see `the official documentation <https://pypi.org/project/setuptools-scm/>`_.


Documentation using Sphinx and reStructuredText
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo::

   * If this project is not complex enough to require the use of full-fledged Sphinx documentation, feel free to:

     * Delete this section of ``README.rst``
     * Delete the ``docs/`` directory
     * Delete the ``docs`` test environment from ``tox.ini``{% if cookiecutter.gh_actions == 'yes' %}and ``.github/workflows/ci-test-matrix.yml``{% endif %}.


This project is configured to use reStructuredText_ and Sphinx_ to generate and maintain project documentation. By defult, ``sphinx`` has been added as a ``dev-packages`` requirement to this project's Pipfile. Therefore, when you run ``pipenv install --dev`` for the first time for your new project ``sphinx`` will be installed to your ``pipenv`` virtual environment by default.

* **For an overview of usage, or for more info on the benefits of Sphinx and reStructuredText**, please see `this section of this brief overview of using Sphinx to document a project <https://sedelmeyer.github.io/cc-pydata/tutorial.html#documenting-your-project-using-sphinx-and-github-pages
>`_
* **If you are new to Sphinx**, please see `the Sphinx documentation <https://www.sphinx-doc.org>`_
* **If you are new to reStructuredText**, a good starting place will be `the reStructuredText documentation provided by the Sphinx project <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_


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
