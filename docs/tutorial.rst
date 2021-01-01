.. _tutorial:

Tutorial
========

This tutorial walks through some of this template's more important features.

.. contents:: Tutorial Contents
  :local:
  :depth: 1
  :backlinks: top


.. _packaging:

Packaging characteristics of this template
------------------------------------------

.. contents:: In this section
  :local:
  :backlinks: top

Using ``pipenv`` to manage your project dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are new to ``pipenv`` for dependency and package management, it may take a little time to get used to it. The best place to start is by taking some time to review core principles, benefits, and usage on the Pipenv_ project page.

Chances are, if you have been using ``virtualenv`` or ``conda`` to manage your Python virtual environments up to this point, then you'll probably wonder how you've made it this far without using ``pipenv`` previously. As is described on the Pipenv_ project page:

    "**Pipenv** is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. *Windows is a first-class citizen, in our world.*"

    "It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your ``Pipfile`` as you install/uninstall packages. It also generates the ever-important ``Pipfile.lock``, which is used to produce deterministic builds."


Adding / installing dependencies using ``pipenv``
"""""""""""""""""""""""""""""""""""""""""""""""""

As was shown in the section :ref:`install-pipenv` above, creating a ``pipenv`` environment and ``Pipfile.lock`` deterministic build is as easy as running ``pipenv install --dev`` from your ``cc-pyscript`` project directory.

To add additional dependencies to your project, you can either:

#. Edit your ``Pipfile`` list of dependencies directly, adding application-specific dependencies under the ``[packages]`` section or development-specific dependencies under the ``[dev-packages]`` section of the ``Pipfile``, then run ``pipenv install --dev`` to install the dependencies and update the ``Pipfile.lock`` build document.

#. Or, more easily, you can run ``pipenv install <pip-package-name>`` to add and install a new application dependency, or ``pipenv install --dev <pip-package-name>`` to add and install a new development dependency. When you add a dependency in this manner, not only will the dependency be installed in your ``pipenv`` environment, but ``pipenv`` will also automatically updated your ``Pipfile`` and ``Pipfile.lock`` to reflect the newly added dependency.

There are many additional actions you can take to update and change dependencies using ``pipenv``.

* To learn more, please see the `documentation on the basic usage of Pipenv <https://pipenv.pypa.io/en/latest/basics/>`_.

* If your preference is to manage dependencies using the ``setup.py`` ``install_requires`` argument, please take some time to `read the distinctions between Pipfile vs. setup.py <https://pipenv.pypa.io/en/latest/advanced/#pipfile-vs-setuppy>`_, and think carefully about the distinctions between managing dependencies for a Python "application" such as that which you are creating with the ``cc-pyscript`` template versus a Python "library", which the ``cc-pyscript`` template is not.


Installing your local ``cc-pyscript`` package as an editable
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
If you inspect the ``cc-pyscript`` template's default ``Pipfile``, you will see that ``pipenv`` will install your newly created local ``cc-pyscript`` package as an "editable" under the ``[packages]`` section of that ``Pipfile``. More specifically, the line in the ``Pipfile`` that reads::

  package_name = {editable = true,path = "."}

...is equivalent to running this from the command line::

    pipenv install -e .

...which is similar to running the following command in plain old ``pip`` if you were not working from a virtual environment::

    pip install -e .

.. _env:

Managing environment variables with the ``.env`` file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you generate a new ``cc-pyscript`` project using this template, by default you will be provided with a ``.env`` file in which you can set environment variables specific to your project.

* This ``.env`` file can be used for setting secret keys, credentials, or filepaths you need for your project, but would like to keep secret.
* By default, the ``.gitignore`` for this project is set to ignore the ``.env`` file.
* It is strongly, strongly, strongly suggested that you NEVER commit your ``.env`` file to source control, or else you will have compromised any credentials saved to that file.

Typically, to load and access the environment variables saved to your ``.env`` file you would need to use a tool such as `python-dotenv <https://saurabh-kumar.com/python-dotenv/>`_.

But alas, because we are using ``pipenv`` to manage our ``cc-pyscript`` project environment, ``pipenv`` **will automatically load your** ``.env`` **environment variables to your environment when you enter your** ``pipenv shell`` **or use** ``pipenv run``.

For instance, if you have a secret key you wish to access programatically when running your ``cc-pyscript`` package locally, you can add the following to your ``.env`` file::

    SECRET_KEY=YOURSECRETKEY

``pipenv`` will seamlessly take care of loading this ``.env``-stored enviroment variable in the background.

Then, to access that secret key directly within your code, you simply need to access it using ``os.getenv``::

    import os

    SECRET_KEY = os.getenv("SECRET_KEY")

To learn more about this ``pipenv`` behavior, please see the documentation on `Pipenv loading of .env`_.


Versioning your project with ``git`` tags and ``setuptools_scm``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``cc-pyscript`` template is configured to make use of `setuptools_scm`_ to manage and track your ``cc-pyscript`` project's current version.

There are a number of different ways to maintain a Python project's current version. For a survey of different approaches to maintain a "single source of truth" for the version number of your project (i.e. where you only need to update the version in one single location), please see this article on `Single-sourcing the package version`_. ``cc-pyscript`` makes use of option #7 in that article.

By using ``setuptools_scm``, your ``cc-pyscript`` application pulls the version number directly from the latest ``git`` tag associated with your project.

Therefore, instead of manually setting a global ``__version__`` variable in your application, you simply add a tag when you commit a new version of your application to ``master``.


Implications for choosing an effective ``git`` branching methodology
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

To use ``setuptools_scm`` effectively, you'll likely want to use a proper/consistent ``git`` branching methodology while building and maintaining your project.

* At a minimum, you should perform all of your development work on separate non-``master`` ``git`` branches, and only when features are complete, "release" them by merging them into your ``master`` branch.

* Therefore, each time you merge a set of your changes into ``master``, that event should be considered a release.

* Thus, a release merged into ``master`` would require you tag it with a new version number.

For instance, say you have a set of tested features on a ``develop`` branch that are ready for release...

You would first merge it into ``master`` (and consider using the ``--no-ff`` argument to prevent fast-forward merges, `thus maintaining the context of your branches and the branching topology <https://stackoverflow.com/questions/9069061/what-is-the-difference-between-git-merge-and-git-merge-no-ff>`_ of your ``git`` history):

.. code-block:: Bash

    # Assuming your 'develop' branch is your current active branch
    git checkout master

    git merge --no-ff develop

    git tag -a v0.3.0 -m "Add a set of features that ..."

As you can see in the steps above, once the set of new features are merged into your ``master`` branch, you would then immediately add an "annotated" (designated by the ``-a`` argument) version tag, and comment it with a brief message describing the release.

Now, if you were to check the version of your project::

    python setup.py --version

... ``setuptools_scm`` would provide you the following result:

.. code-block:: Bash

    v0.3.0

Then, once you have completed and tagged your merge into ``master``, you would push your latest release changes (including the new tag) to your desired ``remote`` and switch back your "development" branch so you don't accidentally make any additional changes to ``master``:

.. code-block:: Bash

    git push origin master
    git push origin v0.3.0
    git checkout develop
    git merge --no-ff master

Now, because you are past your prior release, if you were to re-run ``python setup.py --version``, you'd receive a result similar to this:

.. code-block:: Bash

    0.3.0.dev5+gefeb5a6.d20200620

Voilà! You have released a new version of your project!

To systematize your branching methodology in a manner similar to this, please take some time to:

* Consider using `the Git-flow methodology <https://nvie.com/posts/a-successful-git-branching-model/>`_
* Or, at a minimum, `the simpler GitHub flow methodology <https://guides.github.com/introduction/flow/>`_.

While you're at it, why not do yourself a favor and also add some some useful and consistent context to each of your commits by using the:

* `Conventional Commits specification for adding human and machine readable meaning to your commit messages <https://www.conventionalcommits.org/>`_.


Implications for using Semantic Versioning as a consistent version-numbering scheme
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

According to the ``setuptools_scm`` documentation, `it is required to always include a "patch version" in your tagged version numbers <https://github.com/pypa/setuptools_scm/#default-versioning-scheme>`_.

That means:

* If you are releasing ``v0.3.0`` as was demonstrated in the previous section,
* Then be certain to include the final "``0``", which indicates the "patch version" of that release.

In fact, while you're at it, why not just consistently use Semantic Versioning (i.e. `SemVer`_) for every release you tag in ``git``.

* `SemVer`_ is clean, easy to use, and it conveys important meaning about the underlying code in your package and what has been modified from one version to the next.
* An added benefit, ``setuptools_scm`` is expected to switch to SemVer as its default behavior in the future.

At its core, SemVer uses the ``MAJOR.MINOR.PATCH`` increment scheme for version numbering. As is specified in the `SemVer`_ documentation:

1. You change the ``MAJOR`` version when you make incompatible API changes,
2. You change the ``MINOR`` version when you add functionality in a backwards compatible manner, and
3. You change the ``PATCH`` version when you make backwards compatible bug fixes.

Therefore, each version you release to ``master`` should always be tagged with three distinct period-separated digits, such as in the example:

.. code-block:: Bash

    git tag -a v0.3.0 -m "Add a set of features that ..."



Documenting your project using Sphinx and GitHub Pages
------------------------------------------------------

.. contents:: In this section
  :local:
  :backlinks: top

Getting started with Sphinx and reStructuredText
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The resulting project template is configured to use reStructuredText_ and Sphinx_ to generate and maintain your project documentation. By defult, ``sphinx`` has been added as a ``dev-packages`` requirement to `the template's base Pipfile <https://github.com/sedelmeyer/cc-pyscript/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/Pipfile>`_. Therefore, when you run ``pipenv install --dev`` for the first time for your new project (see :ref:`install-pipenv`), ``sphinx`` will be installed to your ``pipenv`` virtual environment by default.

* **If you are new to Sphinx**, please see `the Sphinx documentation <https://www.sphinx-doc.org>`_
* **If you are new to reStructuredText**, a good starting place will be `the reStructuredText documentation provided by the Sphinx project <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_

.. _make-html:

Generating and previewing your site HTML
""""""""""""""""""""""""""""""""""""""""

Sphinx provides a convenient ``Makefile`` for performing basic site-building tasks. Generating (and re-generating) your Sphinx site's HTML is as easy as following the next two steps:

#. Navigate to your project's ``docs/`` directory::

    cd docs/

#. Run the ``make`` command for building your HTML::

    make html

If your reStructuredText contains any errors, Sphinx will tell you as it builds your HTML.

Your generated HTML, CSS, and related site files will now be located in the project's ``docs/_build/html/`` directory.

At any time you can preview your generated site content by opening your site's ``index.html`` file and navigating throughout your generated site files.

* If you are using Ubuntu, you can open your site content with your default web-browser by using this command::

    xdg-open docs/_built/html/index.html

* If you are using a different operating system, use the appropriate command or simply open the ``index.html`` with your system's GUI.

**It is recommended that you DO NOT** ``git commit`` **those generated site files to your** ``master`` **branch.** It is poor practice (and an inefficient use of git history storage) to commit your site source files and generate site HTML content to the same git branch. Instead, please refer to the section :ref:`gh-pages`. That section outlines a recommended workflow for managing and commiting your generated site content using `GitHub Pages`_.

.. _make-docs:

Auto-generating documentation for your custom package modules
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Sphinx is a powerful tool for auto-generating API documentation directly from the docstrings embedded within your code. In other words, if you take the time to document your code correctly using docstrings, your API reference material can largely write itself.

There are several approaches you can take to accomplish this. Options include:

1. Manual configuration of API reference materials using the ``sphinx.ext.autodoc`` `autodoc Sphinx extension <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_;

2. Manual configuration of API reference materials using the ``sphinx.ext.autosummary`` `autsummary Sphinx extension <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`_;

3. Fully automated generation of API reference materials using the ``sphinx-apidoc`` `command line utility, which relies on the autodoc extension <https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html>`_;

4. Automatic generation of API reference materials by setting the ``autosummary`` extension's ``autosummary_generate = True`` `parameter in your Sphinx <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html#confval-autosummary_generate>`_ ``conf.py`` file;

5. ...a combination of any of the approaches listed above.

Each approach listed above has its own pros and cons which are far too detailed to explore here. For a great comparison of using the ``automodule`` versus the ``autosummary`` extension, `please see this article by Roman Miroshnychenko <https://romanvm.pythonanywhere.com/post/autodocumenting-your-python-code-sphinx-part-ii-6/>`_. Otherwise, please refer to the ``autodoc``, ``sphinx-apidoc``, ``autosummary``, and ``autosummary_generate`` links provided in the list above.

I am sure approaches other than those listed above exist as well, but you should be able to accomplish everything you need to accomplish using these tools, so I will save myself the time it would take to provide a more exhaustive list.

**If you have questions about the proper syntax for writing  Sphinx-friendly reStructuredText docstrings in your Python code**, please see:

* `Roman Miroshnychenko's article on autodocumenting your python code <https://romanvm.pythonanywhere.com/post/autodocumenting-your-python-code-sphinx-part-i-5/>`_

* `Thomas Cokelaer's example on how to document your Python docstrings <https://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html>`_

You may also find Sphinx's `documentation on its Python Domain directives <https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain>`_ to be extremely useful while trying to embed references within your docstrings.

Sphinx can also generate documentation from the Google- and Numpy-formatted docstring styles with the help of the ``sphinx.ext.napoleon`` Sphinx extension. If either of those docstring formats are your jam, please `see the napoleon documentation <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_.

.. note::

   * The first time you run ``make html`` as was described in :ref:`make-html`, the ``docs/modules.rst`` file contained in the default ``cc-pyscript`` template will generate a starter "API Reference" page documenting all modules and functions already contained in the ``cc-pyscript`` template. That initial ``modules.rst`` file makes use of the manual approach #1 listed above and uses the ``sphinx.ext.autodoc`` extension's ``automodule`` `directive <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directive-automodule>`_ to generate that starter documentation.

   * All Sphinx extensions listed above, including ``sphinx.ext.autodoc``, ``sphinx.ext.autosummary``, and ``sphinx.ext.napoleon`` are imported by default in the ``cc-pyscript`` template's ``conf.py`` Sphinx configuration file.


Rationale for using reStructuredText instead of Markdown
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

GitHub, Jupyter notebooks, and other static site generators typically rely on Markdown as a lightweight markup language.

QUESTION:

* So then, why does the ``cc-pyscript`` project template use reStructuredText instead of Markdown?
* Afterall, reStructuredText is a bit more verbose and not quite as frictionless for an author to use compared to Markdown.

ANSWER:

* Because benefits abound, particularly for technical writing (once you get past the initial learning curve).
* And, because the primary assumption is that you'll be writing technical content to document and support your Python-based ``cc-pyscript`` project, reStructuredText is the better choice.

Here are a few primary reasons worth highlighting:

* reStructuredText supports semantic meaning in a manner not supported by Markdown,
* reStructuredText is extensible and standardized while any Markdown implementation that is feature-rich enough to even begin supporting moderate-to-heavy technical writing needs will come in many flavors which are not always portable between different platforms without tedious modification,
* reStructuredText is a stable "go-to", has been around for a while, and has been used heavily in the Python community since 2002,
* reStructuredText is the default markup language for Sphinx (see more about why we are using Sphinx in the section below) and integrates well with `Sphinx's more powerful directives <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_

Rationale for using Sphinx instead of Jekyll, Pelican, or some other static site generator
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

GitHub Pages strongly favors GitHub's homegrown static site generator `Jekyll <https://jekyllrb.com/>`_ and it's hella simple to use for some basic web publishing needs.

* Unfortunately, Jekyll is a Ruby-based tool.
* That means, if you use Jekyll, you'll need to run both a Ruby environment and Python environment to publish your ``cc-pyscript`` documentation.

Meanwhile, Sphinx is through-and-through a Python-based tool (in fact the documentation for the Python language itself is published using Sphinx)!

* The second major drawback for Jekyll is, it's not a tool custom-suited for documenting code.
* This drawback also applies to the Python-based `Pelican <https://docs.getpelican.com/>`_ site generator and many other static site generators.
* They typically provide no means for auto-generating project documentation directly from the custom code contained in your packaged Python library.
* Sphinx, on the otherhand, excels at this task!

As was illustrated above (see :ref:`make-docs`), Sphinx offers powerful built-in extensions such as `sphinx.ext.autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_ for generating and organizing your project documentation, pulling documentation directly from the docstrings in your code.

Information about other popular "built-in" Sphinx extensions that help to make Sphinx a smart choice for technical documentation `can be found in the "Extensions" section of the Sphinx documentation <https://www.sphinx-doc.org/en/master/usage/extensions/index.html>`_.

Adding a logo to your Sphinx site
"""""""""""""""""""""""""""""""""

The default theme used for the Sphinx docs in the ``cc-pyscript`` template is called `Alabaster <https://alabaster.readthedocs.io/en/latest/>`_. It's clean, responsive, and configurable. Did I mention it was clean?

The Alabaster theme provides a simple option for adding a site logo to the top of the lefthand navbar. A reasonable width for that logo image is 200 pixels. To add a logo to your ``cc-pyscript`` project documentation, simply:

#. Save your 200-pixel-width image file (e.g. as .jpg or .png file) to the ``docs/`` directory, and name it ``docs/logo.png`` (with the appropriate file extension of course).
#. Go to the ``docs/conf.py`` file and uncomment the ``logo`` setting in the ``html_theme_options`` dictionary.
#. Then ``make html`` and your new logo image should appear in the generated site HTML.

Adding a favicon to your Sphinx site
""""""""""""""""""""""""""""""""""""

Similar to the site logo, if you wish to add a favicon image to your Alabaster-themed Sphinx site:

#. Generate your ``favicon.ico`` image at 16x16 pixels, or 32x32, or whatever size makes the most sense given current browser standards and backwards compatibility concerns (truthfully, I couldn't care less and would just choose a size that works for your browser of choice).
#. Save it as ``docs/favicon.ico``.
#. Go to the ``docs/conf.py`` file and uncomment the ``html_favicon = '_static/favicon.ico'`` line and ``make html`` again.

.. _gh-pages:

Hosting your project documentation using GitHub Pages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Outlined here is the basic Git workflow for hosting your Sphinx-generated project documentation on `GitHub Pages`_. There are several different methods for configuring GitHub to host your project documentation. The one we will use here is to use a separate ``gh-pages`` Git branch for just your Sphinx-generate site content.

While GitHub can be configured to use the base directory of your ``master`` branch or the ``./docs`` directory of your ``master`` branch, using a separate ``gh-pages`` branch for your site content has the added benefit of keeping your source content separate from your Sphinx-generated build content. This will help to keep your master branch git history storage from ballooning with built site content, particularly when that content can be rebuilt at any time using your historical Git commits.

The basic steps for publishing your GitHub pages content are as follows:

* After running ``make html`` to generate your site content, you need to first create an orphaned ``gh-pages`` branch. Note that this only needs to be done the first time you create this branch::

    git checkout --orphan gh-pages

* By default, all existing files not excluded by your ``.gitignore`` will be staged in your new branch. You will need to remove them all from staging with this command::

    git rm --cached -r .

* Once they're removed from staging and no longer tracked by Git, you can delete them from the gh-pages branch all together. (Don't worry, they will still exist on your ``master`` branch.)::

    git clean -id

* You will then receive a prompt asking you what you want to do. The command you want to specify is ``c`` (clean). By cleaning your repo, your ``gh-pages`` branch will be left containing only your ``.git/`` directory, as well as any other files previously ignored by Git as specified by your ``.gitignore`` file (including your ``docs/_build/html/`` site content).

* Now, to be certain we don't delete or commit any of the other files you had ignored by Git on your ``master`` branch (because these will vanish from your ``master`` branch too if you accidentally delete them), you want to checkout your master version of ``.gitignore``::

    git checkout master -- .gitignore

* If you type ``git status`` you will see that this command has placed your master .gitignore in your ``gh-pages`` staging area, and you will see that Git has gone back to ignoring the other files you'd like ignored. Commit it as such::

    git commit -m "git: add .gitignore from master"

* Now you want to place all of your Sphinx-generated site content into your ``gh-pages`` base directory for rendering by GitHub Pages::

    cp -r docs/_build/html/* .

* Next, add a blank ``.nojekyll`` file to your directory to tell GitHub that you are not using Jekyll (the default site generator for GitHub Pages) to generate your site::

    touch .nojekyll

* If you check ``git status``, you will see that your site content is now visible to git because we have taken it out of the previously ignored ``docs/_build/`` directory.

* Add your site content files to your staging area and commit them::

    git add -A
    git commit -m "docs: add <current release version> site content"

* Then, push the changes to GitHub::

    git push origin gh-pages

* Once committed and pushed, you can return to any of your other branches to continue work on your project::

    git checkout master

* Next time you want to return to your ``gh-pages`` branch to load your latest Sphinx-generated site content to GitHub Pages, you can just checkout that branch and follow the above outlined process again starting with the step of copying over your latest .gitignore in case you've made any edits to it on ``master``::

    git checkout gh-pages
    git checkout master -- .gitignore
    ...

Accessing your new site on GitHub Pages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have pushed the first version of your ``gh-pages`` branch to GitHub, GitHub will automatically generate a new site. To view this site, go to your project repo on GitHub, go to Settings, and scroll down until you see the GitHub Pages section of your settings.

There should now appear a hyperlink indicating the URL at which your new site is located. Follow that link and you can preview your site.

Test configuration and continuous integration with GitHub Actions
-----------------------------------------------------------------

.. contents:: In this section
  :local:
  :backlinks: top

Unit-testing your project and using the ``pytest`` test-runner
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Location of ``cc-pyscript`` unit tests
""""""""""""""""""""""""""""""""""""""

The ``cc-pyscript`` template, by default, provides a ``tests/`` directory at the same level as the ``src/`` directory.

* Opinions and rationale about where to store Python unit tests vary.
* Some people prefer storing unit tests directly within their modules, some under ``src/``, but outside their actual modules, and others in the manner we have done here for ``cc-pyscript``.
* Sometimes circumstances and/or preferences warrant using one location over another.
* To keep things simple, and to make it easy to locate tests in your project, the current ``tests/`` location has been chosen for the ``cc-pyscript`` template.
* However, you should feel free to relocate your unit tests to a different location if it makes sense for you or your project.

``pytest`` test-runner
""""""""""""""""""""""

* ``pytest`` and ``pytest-cov`` are installed as default ``dev-packages`` in the base ``Pipfile`` included with the ``cc-pyscript`` project template.
* `Pytest`_ makes for a simple yet powerful test-runner for test discovery, reporting, and simple diagnostics; and `pytest-cov <https://pytest-cov.readthedocs.io/en/latest/readme.html>`_ produces coverage reports.

Running unit tests using ``pytest``
"""""""""""""""""""""""""""""""""""

At any time during development of your ``cc-pyscript`` project, you can run your entire suite of unit tests. The two easiest methods for doing this are:

#. If you aren't currently in your project's ``pipenv`` environment, run::

    pipenv run pytest

#. If you are currently in your ``pipenv shell``, run::

    python -m pytest

    # or even more simply just the single word command...

    pytest

The ``pytest`` test-runner is a powerful command-line tool. There are far too many features to describe here. For a good overview:

* Please see `the documentation regarding the Usage and Invocations <https://docs.pytest.org/en/latest/usage.html>`_ of ``python -m pytest``;
* Additionally, you can see the complete listing of available ``pytest`` arguments in the "help" documentation by running ``pytest -h``.

Running ``pytest`` will provide a convenient summary as tests are run. As an example, your default ``cc-pyscript`` test output will look something like this if there are no test failures:

.. code::
   
  ====================== test session starts =========================
  platform linux  Python 3.7.9, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
  cachedir: .tox/py37/.pytest_cache
  rootdir: /home/repo_name, configfile: setup.cfg, testpaths: tests
  plugins: cov-2.10.1
  collected 7 items
  
  tests/test_script_name.py .......                             [100%]
  
  ---------- coverage: platform linux, python 3.7.9-final-0 ----------
  Name                                 Stmts  Miss Branch BrPart Cover
  --------------------------------------------------------------------
  src/package_name/__init__.py           6      2      0      0    67%
  src/package_name/script_name.py       29      2      8      1    92%
  --------------------------------------------------------------------
  TOTAL                                 35      4      8      1    88%

  ====================== 7 passed in 0.38s ===========================


Test matrix automation using ``tox``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``cc-pyscript`` template includes the options to render the resulting template with ``tox`` automated testing.

If you are not familiar with Python's test automation tool `Tox`_, learning to use it is well worth the investment in time.

If you review the ``tox.ini`` configuration file contained in the template directory, you will see that ``tox`` automation for this project is configured to:

1. Run the template's unit tests on several different versions of Python to ensure compatibility with each of those versions,
2. Run a test build of the project template's default Sphinx documentation to ensure docs build successfully, and...
3. Run a ``flake8`` linting test to ensure all of the Python syntax in the template meets `PEP 8`_ standards.

To run these automated ``tox`` tests, you simply run the ``tox`` command from within your active ``pipenv`` development environment.

Alternatively, you can run individual ``tox`` environments (instead of all at once) by explcitly specifying the environment you wish to run, such as::

   tox -e docs

If you select ``"no"`` for the ``tox`` choice variable prompt during the ``cc-pyscript`` template rendering process, there will be no ``tox.ini`` file contained in the final rendered template and ``tox`` will not be included in the ``Pipfile`` ``dev-packages`` requirements.


Configuring GitHub Actions for your project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``cc-pyscript`` project template offers the option to configure the rendered template to use `GitHub Actions`_ services for continuous integration testing.

* The ``.github/workflows/ci-test-matrix.yml`` file provided in the ``cc-pyscript`` project template is used to configure your `GitHub Actions`_ build.
* For a tutorial on how to use GitHub Actions, please `see the official GitHub Actions tutorial <https://docs.github.com/en/free-pro-team@latest/actions>`_.

If you select ``"no"`` for the ``gh_actions`` choice variable prompt during the ``cc-pyscript`` template rendering process, there will be neither a ``.github/workflows/`` directory added to the finished template, nor will there be a GitHub Actions build-badge included in the rendered template's default documentation.

The default ``ci-test-matrix.yml`` configuration file
"""""""""""""""""""""""""""""""""""""""""""""""""""""

The configuration of the default ``ci-test-matrix.yml`` file will trigger a GitHub Actions build every time you push to either the ``develop`` or ``master`` remote branch on GitHub. That build will run all of the default ``tox`` environment tests specified in the template's ``tox.ini`` file.

The build badge provided at the top of the template's ``README.rst`` file reflects the latest build results for the project's ``master`` branch.

To modify the branches on which your GitHub Actions are built, or to change the specific Python versions or operating systems used in your test matrix, you will want to change the initial parameters set in the ``ci-test-matrix.yml``::

   ...

   on:
     push:
       branches:
           - master
           - develop
     pull_request:
       branches: [ master ]
   
   jobs:
     build:
   
       strategy:
         matrix:
           python-version: [3.6, 3.7, 3.8]
           os: ["ubuntu-latest"]

   ...

However, please note that other changes may need to be made to your template in order for tests to pass on other operating systems.


.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _`drivendata/cookiecutter-data-science`: https://github.com/drivendata/cookiecutter-data-science
.. _`ionelmc/cookiecutter-pylibrary`: https://github.com/ionelmc/cookiecutter-pylibrary
.. _Packaging a python library: https://blog.ionelmc.ro/2014/05/25/python-packaging/
.. _Packaging pitfalls: https://blog.ionelmc.ro/2014/06/25/python-packaging-pitfalls/
.. _Cookiecutter Data Science: https://drivendata.github.io/cookiecutter-data-science/
.. _`GitHub Actions`: https://github.com/features/actions
.. _Tox: https://tox.readthedocs.io/en/latest/
.. _Sphinx: http://sphinx-doc.org/
.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _setuptools_scm: https://github.com/pypa/setuptools_scm/
.. _Pytest: http://pytest.org/
.. _Pipenv: https://pipenv.readthedocs.io/en/latest/#
.. _Azure Pipelines: https://azure.microsoft.com/en-us/services/devops/pipelines/

.. _Pipenv loading of .env: https://pipenv.kennethreitz.org/en/latest/advanced/#automatic-loading-of-env
.. _Single-sourcing the package version: https://packaging.python.org/guides/single-sourcing-package-version/#single-sourcing-the-version
.. _reStructuredText primer: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

.. _GitHub Pages: https://pages.github.com/
.. _SemVer: https://semver.org/

.. _`pep 8`: https://www.python.org/dev/peps/pep-0008/

