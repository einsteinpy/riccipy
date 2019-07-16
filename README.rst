.. riccipy

.. |mailing| image:: https://img.shields.io/badge/mailing%20list-groups.io-8cbcd1.svg?style=flat-square
   :target: https://groups.io/g/einsteinpy-dev

.. |gitter| image:: https://img.shields.io/gitter/room/EinsteinPy-Project/EinsteinPy.svg?logo=gitter&style=flat-square
   :alt: Join the chat at https://gitter.im/EinsteinPy-Project/EinsteinPy
   :target: https://gitter.im/EinsteinPy-Project/EinsteinPy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. |riotchat| image:: https://img.shields.io/matrix/einsteinpy:matrix.org.svg?logo=riot&style=flat-square
   :target: https://riot.im/app/#/room/#einsteinpy:matrix.org

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
   :target: https://github.com/einsteinpy/riccipy/raw/master/COPYING

.. |docs| image:: https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat-square
   :target: https://docs.riccipy.einsteinpy.org/en/latest/?badge=latest

.. |travisci| image:: https://img.shields.io/travis/einsteinpy/riccipy/master.svg?style=flat-square&logo=travis
   :target: https://travis-ci.org/einsteinpy/riccipy

.. |codeclimate| image:: https://img.shields.io/codeclimate/maintainability/einsteinpy/riccipy.svg?logo=code-climate&style=flat-square
   :target: https://codeclimate.com/github/einsteinpy/riccipy/maintainability
   :alt: Maintainability

.. |circleci| image:: https://img.shields.io/circleci/project/github/einsteinpy/riccipy/master.svg?style=flat-square&logo=circleci
   :target: https://circleci.com/gh/einsteinpy/riccipy

.. |codecov| image:: https://img.shields.io/codecov/c/github/einsteinpy/einsteinpy.svg?style=flat-square
   :target: https://codecov.io/github/einsteinpy/einsteinpy?branch=master

.. |appveyor| image:: https://img.shields.io/appveyor/ci/shreyasbapat/einsteinpy.svg?logo=appveyor&style=flat-square
   :target: https://ci.appveyor.com/project/shreyasbapat/einsteinpy

:Name: RicciPy
:Website: https://riccipy.einsteinpy.org/
:Version: 0.1.dev0

|astropy| |mailing| |gitter| |riotchat| |license| |docs|

|circleci| |travisci| |appveyor| |codecov| |codeclimate|


RicciPy is an open source package that exists as part of The EinsteinPy Project for the
purpose of providing a API that makes tensor algebra as easy as possible on arbitrary
manifolds. RicciPy implements the use of Sympy for representing tensor equations and expressions
symbolically with automatic applications of a metric when contracting indices. Lastly, the
Library also provides a means for converting the results of tensor equations to numpy-like
functions for use in numerical calculations. It is released under the MIT license.

Documentation
=============

|docs|

Complete documentation, including a user guide and an API reference, can be read on
the wonderful `Read the Docs`_.

https://doc.riccipy.einsteinpy.org/

.. _`Read the Docs`: https://readthedocs.org/


Requirements
============

RicciPy requires the following Python packages:

* NumPy, for basic numerical routines
* SymPy, for symbolic calculations related to GR.


..
   Installation
   ============

   The easiest and fastest way to get the package up and running is to
   install EinsteinPy using `conda <http://conda.io>`_::

     $ conda install einsteinpy --channel conda-forge

   Or for Debian/Ubuntu/Mint users, the package is installable from `apt <https://packages.debian.org/sid/python3-einsteinpy>`_::

     $ sudo apt install python3-einsteinpy

   Please note that the package version in Debian Repositories might not be the latest.
   But it will be definitely the most stable version of EinsteinPy available till date.

   Please check out the `guide for alternative installation methods`_.

   .. _`guide for alternative installation methods`: https://einsteinpy.github.io/installation/

..
   Testing
   =======

   |codecov|

   If installed correctly, the tests can be run using pytest::

     $ python -c "import einsteinpy.testing; einsteinpy.testing.test()"
     ============================= test session starts ==============================
     platform linux -- Python 3.7.1, pytest-4.3.1, py-1.8.0, pluggy-0.9.0
     rootdir: /home/shreyas/Local Forks/einsteinpy, inifile: setup.cfg
     plugins: remotedata-0.3.1, openfiles-0.3.1, doctestplus-0.3.0, cov-2.5.1, arraydiff-0.3
     collected 56 items
     [...]
     ==================== 56 passed, 1 warnings in 28.19 seconds ====================
     $

Problems
========

If the installation fails or you find something that doesn't work as expected,
please open an issue in the `issue tracker`_.

.. _`issue tracker`: https://github.com/einsteinpy/riccipy/issues

Contributing
============

RicciPy is a community project, hence all contributions are more than
welcome! For more information, head to `CONTRIBUTING.rst`_.

.. _`CONTRIBUTING.rst`: https://github.com/einsteinpy/riccipy/blob/master/CONTRIBUTING.rst

Developers Documentation can be found here.

Support
=======

|mailing|

Release announcements and general discussion take place on our `mailing list`_.
Feel free to join!

.. _`mailing list`: https://groups.io/g/einsteinpy-dev

https://groups.io/g/einsteinpy-dev

Please join our `[matrix]`_ channel or `gitter`_ chat room for further queries.

.. _`[matrix]`: https://matrix.to/#/#einsteinpy:matrix.org

.. _`gitter`: https://gitter.im/EinsteinPy-Project/EinsteinPy

If you still have a doubt, write a mail directly to `developers@einsteinpy.org <mailto:developers@einsteinpy.org>`_.

Citing
======

If you use EinsteinPy on your project, please
`drop us a line <mailto:developers@einsteinpy.org>`_.

You can also use the DOI to cite it in your publications. This is the latest
one:

|doi|

And this is an example citation format::

 Shreyas Bapat et al.. (2019). EinsteinPy: riccipy 0.1.0. Zenodo. 10.5281/zenodo.2582388


License
=======

|license|

RicciPy is released under the MIT license, hence allowing commercial
use of the library. Please refer to `COPYING`_.

.. _`COPYING`: https://github.com/einsteinpy/riccipy/blob/master/COPYING

..
   FAQ
   ===

   Why Einstein-Py?
   ----------------

   EinsteinPy comes from the name of the famous physicist, Nobel laureate, revolutionary person, Prof. Albert Einstein.
   This is a small tribute from our part for the amazing work he did for the humanity!


   Can I do <insert nerdy thing> with EinsteinPy?
   ----------------------------------------------

   EinsteinPy is focused on general relativity.  One can always discuss probable features on the mailing list and try to implement it.
   We welcome every contribution and will be happy to include it in EinsteinPy.

   What's the future of the project?
   ---------------------------------

   EinsteinPy is actively maintained and we hope to receive an influx of new contributors.
   The best way to get an idea of the roadmap is to see the `Milestones`_ of
   the project.

   .. _`Milestones`: https://github.com/einsteinpy/einsteinpy/milestones

   Inspiration
   -----------

   The whole documentation and code structure is shamelessly inspired by `poliastro`_ . We really thank the poliastro
   developers to make this possible. EinsteinPy is nothing without it's supporters.

   .. _`poliastro`: https://docs.poliastro.space/
