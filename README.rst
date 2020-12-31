Cookiecutter PyScript
=====================

Cookiecutter PyScript (``cc-pyscript``) is a Cookiecutter_ template for generating fully tested Python scripting projects.

.. image:: https://github.com/sedelmeyer/cc-pyscript/workflows/build/badge.svg?branch=master
    :target: https://github.com/sedelmeyer/cc-pyscript/actions

.. image:: https://img.shields.io/badge/License-MIT-black.svg
    :target: https://github.com/sedelmeyer/cc-pyscript/blob/master/LICENSE

|

* **GitHub repo:** https://github.com/sedelmeyer/cc-pyscript

.. contents:: Contents
  :local:
  :depth: 1
  :backlinks: top

Summary
-------

This Cookiecutter_ template allows for the creation of a fully tested Python scripting project. The benefits of this Cookiecutter template include:

* Scripts can be executed as standalone ``.py`` script files OR directly from the command-line entry-point as part of an installable Python application.

* Finished scripts can be made as portable as you like, but can also benefit from added assurances of full unit-testing and test-matrix coverage using Tox_ and continuous integration services such as `GitHub Actions`_ (optional) or `Azure Pipelines`_ (optional, but not yet implemented).

* If your project grows in complexity such that it needs to be reconfigured into a fully-featured Python library, minimal work is needed because the majority of the Python scaffolding needed to make that conversion is already implemented as part of the project.
  
* Conventions and best practices implemented using this template are similar to those used by the similar ``cc-pydata`` and ``cc-pyapp`` Cookiecutter templates, and their use when bootstrapping a new project creates a sense of consistency, making it easier for yourself and others to interpret and extend your code for any new project.


``cc-pyscript`` directory structure
-----------------------------------

Below is a high level overview of the resulting directory structure when you generate a ``cc-pyscript`` project template.

.. code::

    {{ repo_name }}

     │
     ├─ src/               <- Python source code for your project
     │ └─ {{ package_name }}/       <- Default module containing your
     │   │                             script(s)
     │   ├─ __init__.py             <- Makes this directory a module
     │   └─ {{ script_name }}.py    <- The initial script saved to
     │                                 this project
     │
     ├─ tests/             <- Unit tests for Python your script(s)
     │ └─ test_{{ script_name }}.py <- Default tests for script
     │
     ├─ .github/           <- GitHub actions CI workflows (optional)
     │ └─ workflows                 <- Workflows directory
     │   └─ ci-test-matrix.yml      <- CI tests (runs tox matrix)
     │
     ├─ docs/              <- A default Sphinx project for generating
     │ └─ ...                 documentation (if required)
     │
     ├─ .env               <- Sets project-specific environment
     │                        variables such as credentials that you
     │                        do not want committed to Git history
     ├─ .gitignore         <- Specified files to ignore from Git
     ├─ CHANGLOG.rst       <- Documents version-by-version changes
     ├─ LICENSE            <- Project license (included if open source)
     ├─ logging.json       <- Default logging configuration dictionary
     ├─ Pipfile            <- Requirements file for reproducing your
     │                        project environment using the Pipenv
     │                        package manager
     │                        (see pipenv.readthedocs.io)
     ├─ README.rst         <- The top-level README for developers
     ├─ setup.py           <- Setup script for the project using
     │                        setuptools
     ├─ setup.cfg          <- Contains default options for development
     │                        tools (i.e. flake8, isort, pytest, etc.)
     └─ tox.ini            <- Default tox-automated test configuration



.. _design:

Design decisions
----------------

Of primary importance to me while designing the ``cc-pyscript`` template, was the ability to write **fully-tested Python scripts** while retaining the ability to BOTH:

1. Run those scripts as individual ``.py`` files, independent of the overarching project repository,

2. Run those scripts as a suite of command-line applications, directly from CLI entry-points if so desired.

Also of importance, was to have the code packaged within standardized Python application, easily extensible should the project grow in size and complexity.

While I have attempted to embed Python best practices and standards into the design of this template, best practices and standards change over time. What's more, this template is designed to formalize the workflows (see `Getting started`_) and leverage the tools (see `Features`_) that work best for me across a wide range of projects. If you choose to adopt this template for your own use, you may find these workflows and tools do not work for you without making some changes yourself. For that reason, please feel free to fork and modify your own version of this project.

.. _sources:

Inspiration and sources
^^^^^^^^^^^^^^^^^^^^^^^

When I started building this project, I took note of the workflows and design decisions I began repeating across a number of my Python-based projects. Many of those workflows and decisions were inspired by methods I had learned from others and from patterns codified by other great Cookiecutter templates.

As a result, this template takes inspiration and borrows heavily from these other fabulous Cookiecutter templates available on GitHub:

* `audreyfeldroy/cookiecutter-pypackage`_
* `ionelmc/cookiecutter-pylibrary`_

For additional background on these other projects and to better understand the elements that appealed most to me, please read:

* Ionel Cristian Mărie's articles on `Packaging a python library`_ and `Packaging pitfalls`_,

.. _features:

Features
--------

The default ``cc-pyscript`` template makes use of the following tools and features:

* Pipenv_ for package management and for generating a repeatable environment;
* Automated testing using Tox_;
* `GitHub Actions`_ for continuous integration (optional);
* `Azure Pipelines`_ as an alternative continuous integration service (optional, but not yet implemented);
* Project versioning with `setuptools_scm`_;
* Configuration of your individual script files for easy use as standalone Python scripts when used separately from the project repository (i.e. you can email someone just your ``.py`` script file, and they should be able to use it separate from the supporting Python package scaffolding);
* Packaging of your Python scripts as part of an overarching module, allowing you to fully test your code and alternatively execute your scripts as an installable command-line entry-point;
* Project documentation generated using Sphinx_ and reStructuredText_, ready for hosting alongside your project on GitHub pages.

To see functionality anticipated for future versions of the ``cc-pyscript`` template, please see `the Changelog notes regarding future-releases <https://sedelmeyer.github.io/cc-pyscript/changelog.html#future-releases>`_.

.. _requirements:

Requirements
------------

Basic prerequisites
^^^^^^^^^^^^^^^^^^^

This template and resulting ``cc-pyscript`` project has been tested to work with the following installed dependencies. However, I suspect it will will work with a broader range of ``cookiecutter`` and ``pipenv`` versions than are shown here:

* ``python >= 3.6``
* ``cookiecutter >= 1.7``
* ``pipenv >= 2018-11-26``

For an in-depth review of testing perfomed on this project, please see `the write-up I have provided on "Project testing and the test API" <https://sedelmeyer.github.io/cc-pyscript/about.html#project-testing-and-test-api>`_.

Installing ``cookiecutter``
"""""""""""""""""""""""""""

In order to generate this template, you will need ``cookiecutter`` installed on your machine. For instruction on how to install this, please see the `Cookiecutter installation documentation <https://cookiecutter.readthedocs.io/en/1.7.2/installation.html>`_.

Installing ``pipenv``
"""""""""""""""""""""

In addition, because the resulting ``cc-pyscript`` project template is configured to use ``pipenv`` for package management, you will also want to enure that you have ``pipenv`` installed on your machine. For more information on ``pipenv`` please see `the documentation <https://pipenv.pypa.io/en/latest/>`_. For instructions on how to properly install ``pipenv``, please see `the official installation instructions <https://pipenv.pypa.io/en/latest/install/#installing-pipenv>`_.

Using an alternative to ``pipenv`` for package management
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

If you prefer NOT to use ``pipenv`` for packaging and virtual environment management in favor of an alternative such as ``conda`` or ``virtualenv``, you will need to modify the resulting template structure accordingly.


Getting started
---------------

.. contents:: In this section
  :local:
  :backlinks: top


0. Ensure all prerequisites are met
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See the :ref:`requirements` section of above to ensure basic system dependencies are met.


1. Initiate the ``cc-pyscript`` template using Cookiecutter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have met the basic requirements listed above, generating a new ``cc-pyscript`` project template is as easy as executing this in your command line::

  cookiecutter gh:sedelmeyer/cc-pyscript

Alternatively, if you have a local working copy of the ``cc-pyscript`` project in which you have made customizations to the template, you can run::

  cookiecutter <path-to-directory>/cc-pyscript


2. Complete template prompts required to generate the template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The below listed prompts will be presented on the command-line after initiating your project template (see Step 1 above). For each prompt, default values will be presented in brackets (i.e. ``full_name [Bob Smith]:``).

To modify defaults or customize these prompts, you can do so in the ``cookiecutter.json`` file. Additional information on the ``cookiecutter.json`` file can be found in `the Cookiecutter "choice variables" documentation <https://cookiecutter.readthedocs.io/en/1.7.2/advanced/choice_variables.html>`_.

Additionally, if you would like to auto-populate the values for any of these promptsi across multiple Cookiecutter templates, you can also create a ``.cookiecutterrc`` configuration file as is outlined in `the Cookiecutter "user config" documentation <https://cookiecutter.readthedocs.io/en/1.7.2/advanced/user_config.html#user-config>`_.

"Choice variable" template prompts
""""""""""""""""""""""""""""""""""

1. ``full_name``

   * Main author of this library or application (used in ``setup.py`` and ``docs/conf.py``)
   * Can be set in your ``~/.cookiecutterrc`` config file

2. ``email``
  
   * Contact email of the author (used in ``setup.py``)
   * Can be set in your ``~/.cookiecutterrc`` config file

3. ``website``

   * Website of the author (not yet used in resulting template).
   * Can be set in your ``~/.cookiecutterrc`` config file

4. ``github_username``

   * GitHub user name of this project (used for GitHub links in ``setup.py`` and ``docs/conf.py``)
   * Can be set in your ``~/.cookiecutterrc`` config file

5. ``project_name``

   * Verbose project name (used in headings in ``README.rst``, ``docs/index.rst``, etc.)

6. ``repo_name``

   * Repository root-directory name and repo name on GitHub (used in ``setup.py``, ``docs/conf.py``, and for GitHub links)

7. ``package_name``

   * Python package name (the source code package name as you would import it in your code, i.e.: ``import package_name``)

8. ``script_name``

   * Python script ``.py`` filename for the initial script saved to your project (can be executed as a standalone script by running a command such as ``python src/package_name/script_name.py -h`` )

9. ``distribution_name``

   * PyPI distribution name (what you would ``pip install``)

10. ``project_short_description``

    * One line description of the project (used in ``README.rst``, ``setup.py``, and ``docs/conf.py``)

11. ``release_date``

    * Release date of the project (ISO 8601 format), defaults to ``today`` (used in ``CHANGELOG.rst``)

12. ``year_from``

    * Initial copyright year (used in Sphinx ``docs/conf.py``)

13. ``version``

    * Release version, defaults to ``0.0.0`` (used in ``setup.py`` and ``docs/conf.py``)

14. ``scm_versioning``

    * Enables the use of `setuptools-scm <https://pypi.org/project/setuptools-scm/>`_, defaults to ``yes`` (there is currently no option to turn this off, all projects will include this capability by default)

15. ``license``

    * License to use in the rendered template
    * Available options:

      * MIT license
      * BSD 2-Clause license
      * BSD 3-Clause license
      * ISC license
      * Apache Software License 2.0
      * Not open source

    * If need help deciding which license to pick, see this: https://choosealicense.com/

16. ``test_runner``

    * Available options: ``pytest`` only

17. ``linter``

    * Available options: ``flake8`` only

18. ``command_line_interface``

    * Enables a CLI bin/executable file.
    * Available options: ``argparse`` only

19. ``command_line_interface_bin_name``

    * Name of the CLI bin/executable file (used to set the console script name in ``setup.py`` and the name you would use to invoke the CLI from your terminal when you have the overarching Python module installed in your active environment)

20. ``gh_actions``

    * Adds a default `GitHub Actions`_ badge and ``.github/workflows/ci-test-matrix.yml`` configuration file to the rendered template, defaults to ``yes``
    * Available options:

      * yes
      * no

21. ``tox``

    * Adds a default ``tox.ini`` test automation configuration file to the rendered template, defaults to ``yes`` (there is currently no option to turn this off, all projects will include this capability by default)


3. Initiate git version control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first thing you should do once your template has been generated is to ``cd`` into your new repository and initialize ``git``::

  cd <newly-generate-directory>
  git init

This step will be required prior to inititating your Pipenv environment because ``setuptools-scm`` is used for versioning your newly generated package. If Git has not yet been initialized for your project, the ``pipenv`` install of your local package will fail in the next step below.


.. _install-pipenv:

4. Install your new ``pipenv`` environment from the Pipfile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have Git version control initiated (see Step 3 above), you can build your working Pipenv_ virtual environment::

    pipenv install --dev

Note that the ``--dev`` option is specified so that both development and package dependencies are installed in your Pipenv environment.

To activate your environment after it has been created::

    pipenv shell

To deactivate your environment::

    exit

For a more complete overview of how to use ``pipenv`` for package and dependencies management, please see the Pipenv_ project page.

**Congratulations!** You've stood up a new ``cc-pyscript`` project template!

**Now it's time to explore some of the features of this template!**


.. _other resources:

Other resources
---------------

For further reading, please see `this project's full tutorial`_ as well as these other useful resources:

Cookiecutter resources
^^^^^^^^^^^^^^^^^^^^^^

* The Cookiecutter_ project on GitHub
* The official `Cookiecutter project documentation <https://cookiecutter.readthedocs.io/en/1.7.2/>`_

Tools leveraged by ``cc-pyscript``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Pipenv_ for package and virtual environment management
* `GitHub Actions`_ for continuous integration
* setuptools_scm_ for project versioning
* Sphinx_ and reStructuredText_ for authoring project documentation
* Pytest_ for use as a Python test-runner
* Tox_ for automated test configuration and matrix testing on multiple versions of Python

Articles related to Python packaging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* `Packaging a python library`_
* `Packaging pitfalls`_
* `Distributing packages using setuptools <https://packaging.python.org/guides/distributing-packages-using-setuptools/>`_


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyfeldroy/cookiecutter-pypackage`: https://github.com/audreyfeldroy/cookiecutter-pypackage
.. _`ionelmc/cookiecutter-pylibrary`: https://github.com/ionelmc/cookiecutter-pylibrary
.. _Packaging a python library: https://blog.ionelmc.ro/2014/05/25/python-packaging/
.. _Packaging pitfalls: https://blog.ionelmc.ro/2014/06/25/python-packaging-pitfalls/
.. _Tox: https://tox.readthedocs.io/en/latest/
.. _Sphinx: http://sphinx-doc.org/
.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _setuptools_scm: https://github.com/pypa/setuptools_scm/
.. _Pytest: http://pytest.org/
.. _Pipenv: https://pipenv.readthedocs.io/en/latest/#
.. _`Azure Pipelines`: https://azure.microsoft.com/en-us/services/devops/pipelines/
.. _`GitHub Actions`: https://github.com/features/actions

.. _`this project's full tutorial`: https://sedelmeyer.github.io/cc-pyscript/tutorial.html
