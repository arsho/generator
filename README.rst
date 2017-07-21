GENERATOR
=========

|Build Status| |Version| |Python| |Size| |Codecov|

Generator is a package for generating strong password and check strength of user defined password.

This software can be used on Linux/Unix, Mac OS and Windows systems.

Features
~~~~~~~~

-  Generate strong password

   - The length can be defined by the user. If the length is not defined this will generate minimum eight length password.

   - Password will be generated using English uppercase letters, lowercase letters, numbers and special symbols.

-  Check the strength of any English string as password.

Installation
~~~~~~~~~~~~

We recommend install ``generator`` through pip install.

.. code:: bash

    $ pip install generator

Example
~~~~~~~

To generate a password of minimum 8 length:

.. code:: python

	import generator
	password = generator.generate()
	print(password)
	# Output: 54#@!WdSa!9

To generate a password of user defined length:

.. code:: python

	import generator
	password = generator.generate(10)
	print(password)
	# Output: W2@da%1Fz*

To get strength of any password:

.. code:: python

	import generator
	strength = generator.strength("password")
	print(strength)
	# Output: 5.5

Contribute
~~~~~~~~~~

Create Github Pull Request https://github.com/arsho/generator/pulls

If you have suggestion use GitHub issue system or send a message in Facebook https://www.facebook.com/ars.shovon.

Thanks
~~~~~~

Thanks to the developers who have inspired to create it.
https://github.com/

Change log
----------

See `CHANGELOG <https://github.com/arsho/generator/blob/master/CHANGELOG.rst>`_.

.. |Build Status| image:: https://travis-ci.org/arsho/generator.svg?branch=master
   :target: https://travis-ci.org/arsho/generator

.. |Version| image:: https://img.shields.io/pypi/v/generator.svg?
   :target: http://badge.fury.io/py/generator
   
.. |Python| image:: https://img.shields.io/pypi/pyversions/generator.svg?
   :target: https://pypi.python.org/pypi/generator/
      
.. |Size| image:: https://img.shields.io/github/size/arsho/generator/generator/__init__.py.svg?
   :target: https://github.com/arsho/generator/
   
.. |Codecov| image:: https://codecov.io/github/arsho/generator/coverage.svg?branch=master
   :target: https://codecov.io/github/arsho/generator