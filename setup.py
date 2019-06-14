#!/usr/bin/env python

from setuptools import setup

import os
import sys
import pysimplesoap

VERSION = '0.0.0'

package_dir = 'pysimplesoap'

setup(name='PySimpleSOAP',
      version=VERSION,
      description='Python Simple SOAP Library',
      author='Mariano Reingart',
      author_email='reingart@gmail.com',
      url='https://github.com/pysimplesoap/pysimplesoap/tree/stable',
      download_url='https://github.com/NicolasSandoval/pysimplesoap/tarball/stable_py3k',
      packages=['pysimplesoap',],
      package_dir={'pysimplesoap': package_dir}
      #package_data={'pysimplesoap':['']}
      #console=['client.py'],
      #cmdclass = {"py2exe": build_installer},
     )

