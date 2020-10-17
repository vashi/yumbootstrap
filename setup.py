#!/usr/bin/python

from setuptools import setup, find_packages
from glob import glob

setup(
  name         = 'yumbootstrap',
  version      = '0.0.3',
  description  = 'chroot installer for Red Hat derivatives',
  scripts      = glob("bin/*"), # yumbootstrap should go to sbin, not to bin
  packages     = find_packages("yumbootstrap"),
#  package_dir  = { "": "lib" },
  install_requires=['rpm', 'bsddb'],
  
)
