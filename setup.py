#!/usr/bin/env python

from setuptools import setup
try:
    import py2exe
    from nsis import build_installer
except:
    build_installer = None

import pysimplesoap
package_dir = pysimplesoap

setup(name='PySimpleSOAP',
      version=pysimplesoap.client.__version__,
      description='Python Simple SOAP Library',
      author='Mariano Reingart',
      author_email='reingart@gmail.com',
      url='https://github.com/pysimplesoap/pysimplesoap/tree/stable',
      packages=['pysimplesoap',],
      package_dir={'pysimplesoap': package_dir}
      #console=['client.py'],
      #cmdclass = {"py2exe": build_installer},
     )

