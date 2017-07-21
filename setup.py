# -*- coding: utf-8 -*-
from setuptools import setup
def readme():
    with open('README.rst', encoding='utf8') as f:
        return f.read()
setup(name='generator',
      version='0.0.1',
      description='Generator is a package for generating strong password and check strength of user defined password.',
      long_description=readme(),
      install_requires=[],
      classifiers=[
        'Operating System :: OS Independent',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',		
        'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Development Status :: 5 - Production/Stable',
		'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      keywords='password generator strength pass',
      url='http://github.com/arsho/generator',
      author='Ahmedur Rahman Shovon',
      author_email='shovon.sylhet@gmail.com',
      license='MIT',
      packages=['generator'],
      include_package_data=True,
      zip_safe=False
	  )
