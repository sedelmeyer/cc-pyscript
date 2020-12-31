.. _about:

About this project
==================

This page contains information to help you learn a bit more about the ``cc-pyscript`` project and how it is configured.

* If your goal is to learn more about the Cookiecutter tool used as the basis for the ``cc-pyscript`` project, your best source of information will be the official Cookiecutter_ documentation.

* If you just want to know what the ``cc-pyscript`` project is, please see the :ref:`README<README>` documentation for this project.

* If you want to (a) learn more about the how to generate or use the resulting ``cc-pyscript`` template or (b) better understand the features and functionality embedded in the resulting ``cc-pyscript`` template, please see the :ref:`Tutorial` for this project.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

.. contents:: On this page
  :local:
  :depth: 1
  :backlinks: top

.. _development:

Development philosophy
----------------------

As is discussed in the :ref:`design` section of the ``cc-pyscript`` documentation, I have sought to balance Python best practices and standards with my own needs across a wide range of projects. What's more, I've also sought to embed structural characteristics of other great Cookiecutter templates (see :ref:`sources`).

Starting from those initial principals, I hope to have built a Cookiecutter template that is flexible and robust enough for others to find useful for their own Python scripting projects.

I have taken the time to :ref:`carefully test<project-testing>` and document the ``cc-pyscript`` project, both for my own sake, as well as for the sake of others who might find this project and wish to use it themselves.

I hope that the :ref:`Tutorial` for this project not only enlightens the user, but provides (a) the blueprint needed for those who may not be familiar with all of the tools and methods employed in the template, and (b) enough of a foundation for those who wish `to fork <https://en.wikipedia.org/wiki/Fork_(software_development)>`_ and modify the project to better suit their own needs.

License
-------

The ``cc-pyscript`` Cookiecutter template is offered for use under the MIT open source license.

The content of this license is shown below and can also be found in `the LICENSE file contained in the project repository on GitHub <https://github.com/sedelmeyer/cc-pyscript/blob/master/LICENSE>`_:

    .. include:: ../LICENSE


Contributing
------------

As is mentioned above in the :ref:`development` section of this page, I have sought to balance best practices and features with my own particular needs. Therefore, I am not actively seeking contributions to the ``cc-pyscript`` project from others. My primary reason being that, as soon as others begin adding features to this project, the more likely it will be that the template no longer fits my specific needs.

If however, you do see opportunities to improve this project and its resulting template, I am still interested in hearing from you.

If you'd like to suggest changes or to get in touch regarding the ``cc-pyscript`` project, `please feel free to open an issue and we can discuss <https://github.com/sedelmeyer/cc-pyscript/issues>`_.

I am not quite sure how firm I am on my position of "no contributions." **Therefore, if you have great ideas on how to improve this project...there's a very good chance that I can be convinced!**

.. _project-testing:

Project testing and test API
----------------------------

It has been my experience that testing a Cookiecutter template presents its own set of unique challenges.

Not only do you need to:

1. Test that the template renders, but you also need to...
2. Test that the template renders appropriately according to whatever sorts of build options you provide when invoking the template, and you also need to...
3. Test that the default functionality baked into template after it's been rendered functions appropriately as well (i.e. you need to perform "*tests within tests*").

Thus far, I have been unable to find any clear documentation online on how to do this correctly.

Therefore, I am providing more detail than might otherwise be warranted on how I have configured my ``cc-pyscript`` project tests to deal with (what I can only imagine are) common challenges encountered by anyone who has ever sought to thoroughly test their own custom Cookiecutter template.

.. contents:: In this section
  :local:
  :depth: 2
  :backlinks: top

Using ``pipenv`` to install the required development dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prior to running any of the tests outlined below, you will need to first install the `Pipenv`_ virtual environment required for development of the ``cc-pyscript`` Cookiecutter template.

For details regarding Pipenv and its usage, please :ref:`see the packaging section section<packaging>` of the Tutorial.

Assuming :ref:`you already have Pipenv installed on your development machine<requirements>`, you should be able to install the required dependencies and virtual environment by running the following commands from the ``cc-pyscript`` repository's base directory::

   pipenv install --dev
   pipenv shell

Once you are working from your active ``pipenv`` shell, you will be able to run all other testing commands outlined in the sections below.

Testing tools employed for this project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I have sought to develop a thorough set of tests to ensure that the ``cc-pyscript`` project and resulting template function as expected. Programmatic tests for this project can be found in the ``tests`` directory, where I seek to test each unique feature of this template.

Tests for this project occur in several ways.

1. There are :ref:`the programmatic tests<unit-tests>` using Python's standard ``unittest`` library to author test cases for each template feature I wish to test.

   * My governing principal here, is that I should not add any additional functionality into the template, or the means by which the overarching ``cc-pyscript`` project renders the template, without also developing a test (or set of tests) to test that functionality.

   * There are additionally unit tests built into the rendered template produced by this project. Those in-template tests ensure that the baseline package provided in that rendered template functions correctly (presenting the opportunity for *tests within tests*).

2. There are :ref:`a set of automated tests configured<test-automation>` using ``tox`` to ensure that the ``cc-pyscript`` project functions correctly on several different versions of Python (those versions are ``python 3.7`` and ``python 3.8`` as of ``cc-pyscript v0.1.0`` at the time of my writing this).

   * This ``tox`` configuration also runs a documentation test build to ensure that the ``cc-pyscript`` Sphinx-based documentation renders successfully, and it runs a linter to ensure that the project code meets `PEP 8`_ standards.

   * Also, dependent on whether the ``tox`` option is enabled for the rendered ``cc-pyscript`` template, the rendered template itself will also contain a ``tox``-automated test-configuration. That in-template ``tox`` configuration will perform similar tasks for the resulting rendered template (and here is our true layer of *tests within tests*).

3. Lastly, :ref:`continuous integration is implemented<ci-services>` using `GitHub Actions`_ to run and test automated builds each time committed revisions to the ``cc-pyscript`` project are pushed to the GitHub-hosted remote ``develop`` or ``master`` branches for the project.

.. _`test-automation`:

``tox`` test matrix and automation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are not familiar with Python's test automation tool `Tox`_, learning to use it is well worth the investment in time.

If you review the ``tox.ini`` configuration file contained in the ``cc-pyscript`` project repository, you will see that ``tox`` automation for this project is configured to:

1. Run tests on several different versions of Python to ensure compatibility with each of those versions;
2. Run a test build of the ``cc-pyscript`` project's Sphinx documentation to ensure docs build successfully;
3. Run a ``flake8`` linting test to ensure all of the Python syntax in this project meets `PEP 8`_ standards; and...
4. Run a full build of the ``cc-pyscript`` default template and then run that rendered template's own automated ``tox`` tests (see details concerning the ``tests.toxtest`` test module :ref:`outlined in this section<tests-structure>`)

To run these automated ``tox`` tests, you simply run the ``tox`` command from within your active ``pipenv`` development environment.

Additionally, you can run individual ``tox`` environments (instead of all at once) by explcitly specifying the environment you wish to run, such as::

   tox -e docs


.. _`ci-services`:

Continuous integration test builds with GitHub Actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Continuous integration (CI) build tests are set to run via `GitHub Actions`_ every time a change is pushed to either the ``master`` or ``develop`` remote branches.

These CI tests ensure that the ``cc-pyscript`` ``tox``-automated test matrix runs successfully on a Linux system.

Please see the ``cc-pyscript`` project's ``.github/workflows/ci-test-matrix.yml`` configuration file for more detail.


.. _`unit-tests`:

Custom ``tests`` module using ``unittest`` and the ``pytest`` test-runner
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To run unit tests for the ``cc-pyscript`` project, enter your development environment by running ``pipenv shell`` and invoke the ``pytest`` test-runner by running the following command from your top-level project directory::

   pytest


You should see output similar to this:

.. code-block:: Bash

    ====================== test session starts ========================
    platform linux Python 3.7.9, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
    rootdir: /home/cc-pyscript, configfile: setup.cfg, testpaths: tests
    plugins: cov-2.10.1
    collected 28 items

    tests/test_defaults.py ..........                            [ 35%]
    tests/test_options.py .........                              [ 67%]
    tests/test_testutils.py .........                            [100%]

    ====================== 28 passed in 6.26s =========================


Testing rendered Cookiecutter templates
"""""""""""""""""""""""""""""""""""""""

Before getting into the details of the ``tests`` test module, it is probably worth acknowledging that:

1. There exists a ``pytest`` plugin for testing Cookiecutter templates. That plug-in is named ``pytest-cookies``, and it provides a boilerplate-free experience for building and testing Cookiecutter templates.

2. However, I DO NOT use that plug-in in any way for testing this project.

If you'd like to learn more about the ``pytest-cookies`` plugin for your own use, `please see that project's documentation <https://pytest-cookies.readthedocs.io/en/latest/>`_.

While I use ``pytest`` as the test-runner for this project, I do not use the ``pytest`` framework for writing my tests. I have attempted to keep my tests written entirely using ``unittest`` from the Python standard library. This approach requires a bit more boilerplate in my test code, but it also helps to ensure that I am not locked into ``pytest`` as a testing requirement. Besides, I have also found a simple-enough approach to building and testing my Cookiecutter template using just ``unittest`` test cases. As a result, I haven't felt a need to use ``pytest`` or the ``pytest-cookies`` plug-in.

If you examine the ``TestCase`` classes in the ``tests.test_default`` and ``tests.test_options`` test modules, you will see that each ``TestCase`` contains a ``setUp()`` method that:

a. Uses the ``contextlib.ExitStack()`` `context manager <https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack>`_ to generate a ``tempfile.TemporaryDirectory()`` `temporary directory <https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryDirectory>`_ in which I can build each of my ``cc-pyscript`` rendered templates for testing; and...

b. Contains a call to ``self.addCleanup(stack.pop_all().close)`` to ensure the temporary directory gets cleaned up after each test, `regardless of whether the test setup fails in any way <https://stackoverflow.com/questions/37534021/addcleanup-vs-teardown>`_.

Each test case additionally uses ``cookiecutter.main.cookiecutter()``, `the main entry point to the cookiecutter command <https://cookiecutter.readthedocs.io/en/1.7.2/cookiecutter.html#module-cookiecutter.main>`_, which allows you to easily initiate a template build directly from your Python code.

By putting these pieces together, ``cc-pyscript`` template builds become predictable and easy to manage for testing.

.. _`tests-structure`:

The structure of the ``tests`` module
"""""""""""""""""""""""""""""""""""""

As you will see in the ``tests`` module API documentation below, ``cc-pyscript`` tests are split among several submodules.

1. :mod:`tests`: At the highest level are a set of utility functions that make testing easier and reduce boilerplate code in each test case. These utility functions themselves are tested in :mod:`tests.test_testutils`.
2. :mod:`tests.test_defaults`: This sub-module contains a set of tests focused on the default ``cc-pyscript`` template build.
3. :mod:`tests.test_options`: This sub-module focuses on testing versions of the ``cc-pyscript`` template produced when using the optional arguments available when rendering the template.
4. :mod:`tests.toxtest`: Finally, this is a sub-module that only runs when explicitly called using the command ``pytest -s tests/test_toxtest.py``.

   * ``tests.toxtest`` contains a costly test to run because, it not only renders the ``cc-pyscript`` template, but it also invokes that template's own ``tox.ini`` to run all of its own ``tox`` environments.
   * Think of it as *tests-within-tests-within-tests*, all running in their own embedded temporary environments.
   * This sub-module can take several minutes to run, so considered yourself warned.
   * See :mod:`tests.toxtest` for more detail.

Located below is the full API documentation for each of these modules.

API documentation for the ``tests`` module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: Module contents
  :local:
  :depth: 2
  :backlinks: top

.. automodule:: tests
   :members:

.. automodule:: tests.test_testutils
   :members:

.. automodule:: tests.test_defaults
   :members:

.. automodule:: tests.test_options
   :members:

.. automodule:: tests.toxtest
   :members:


.. _`GitHub Actions`: https://github.com/features/actions
.. _tox: https://tox.readthedocs.io/en/latest/
.. _`pep 8`: https://www.python.org/dev/peps/pep-0008/
.. _`Pipenv`: https://pipenv.readthedocs.io/en/latest/#
