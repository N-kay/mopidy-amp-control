****************************
Mopidy-Amp-Control
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-Amp-Control
    :target: https://pypi.org/project/Mopidy-Amp-Control/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/circleci/build/gh/N-kay/mopidy-amp-control
    :target: https://circleci.com/gh/N-kay/mopidy-amp-control
    :alt: CircleCI build status

.. image:: https://img.shields.io/codecov/c/gh/N-kay/mopidy-amp-control
    :target: https://codecov.io/gh/N-kay/mopidy-amp-control
    :alt: Test coverage

Runs configurable commands to power / unpower your amplfier. Requires pre-built functionality to do that, this just runs the commands at appropriate times.


Installation
============

Install by running::

    python3 -m pip install Mopidy-Amp-Control


Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-Amp-Control to your Mopidy configuration file::

    [amp_control]
    cmd_power = "send 11111 4 1"
    cmd_unpower = "send 11111 4 0"
    unpower_in_minutes = 5

Project resources
=================

- `Source code <https://github.com/N-kay/mopidy-amp-control>`_
- `Issue tracker <https://github.com/N-kay/mopidy-amp-control/issues>`_
- `Changelog <https://github.com/N-kay/mopidy-amp-control/blob/master/CHANGELOG.rst>`_


Credits
=======

- Original author: `N-kay <https://github.com/N-kay>`__
- Current maintainer: `N-kay <https://github.com/N-kay>`__
- `Contributors <https://github.com/N-kay/mopidy-amp-control/graphs/contributors>`_
