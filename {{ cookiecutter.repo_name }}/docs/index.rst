.. {{ (cookiecutter.project_name) }} documentation master file. This file should
   at least contain the root `toctree` directive.

Welcome to {{ cookiecutter.project_name }}'s documentation!
{% for _ in cookiecutter.project_name %}{{"="}}{% endfor %}============================

.. toctree::
   :maxdepth: 2

   readme
   modules
   changelog

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
