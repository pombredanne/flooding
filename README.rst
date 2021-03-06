flooding
==========================================

Introduction

Usage, etc.

More details in src/flooding/USAGE.txt .


Works with RabbitMQ version 2.8.7.


Install production / staging server
-----------------------------------

Linux task machine (i.e. task 200). The task server checks out the
master trunk of flooding.

Init
    $ bin/fab staging_taskserver init
Update
    $ bin/fab staging_taskserver update_task

Init
    $ bin/fab production_taskserver init
Update
    $ bin/fab production_taskserver update_task

See staging-task-200.cfg as an example, it actually serves tasks 200,
210 and 220.

Problems can arise when installing netcdf4. Try:

    $ sudo apt-get install libhdf5-serial-dev libnetcdf-dev


WARNING: buildout run on jupiter
--------------------------------

Buildout chokes if you run it with the smb share still mounted.  So,
as root, first unmount ('umount') the share::

  #> umount /srv/flooding.lizardsystem.nl/var/external_data

After buildout finished correctly, mount it again as root::

  #> mount /srv/flooding.lizardsystem.nl/var/external_data


Development installation
------------------------

The first time, you'll have to run the "bootstrap" script to set up setuptools
and buildout::

    $> python bootstrap.py

And then run buildout to set everything up::

    $> bin/buildout

(On windows it is called ``bin\buildout.exe``).

You'll have to re-run buildout when you or someone else made a change in
``setup.py`` or ``buildout.cfg``.

The current package is installed as a "development package", so
changes in .py files are automatically available (just like with ``python
setup.py develop``).

If you want to use trunk checkouts of other packages (instead of released
versions), add them as an "svn external" in the ``local_checkouts/`` directory
and add them to the ``develop =`` list in buildout.cfg.

Tests can always be run with ``bin/test`` or ``bin\test.exe``.



Workflows
------------------------
The next workflow_templates are created on migration:

DEFAULT_TEMPLATE_CODE = 1 (workflow for a scenario with sobek model)
IMPORTED_TEMPLATE_CODE = 2 (workflow for a scenario with onknown model via import)
THREEDI_TEMPLATE_CODE = 3 (workflow for scenario with 3di model)
MAP_EXPORT_TEMPLATE_CODE = 4 (workflow for map's export)

The range of template's code 0 - 50 area reserved for auto workflows. 


Symlink a buildout configuration
--------------------------------

Initially, there's no ``buildout.cfg``. You need to make that a symlink to the
correct configuration. On your development machine, that is
``development.cfg`` (and ``staging.cfg`` or ``production.cfg``, for instance
on the server)::

    $> ln -s development.cfg buildout.cfg

