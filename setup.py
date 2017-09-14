#! /bin/python

from setuptools import setup, find_packages

setup(name='browser',
      version='0.1.1',
      description='A small browser implementation in Python',
      url='https://github.com/rony728/py-browser',
      author='rony728',
      author_email='rony728@gmail.com',
      license='GNU GPLv3',
      packages=find_packages(),
      install_requires=[
        'PyQt5',
        'requests'
      ],
      entry_points={
        'console_scripts':[
            'browser = py-browser.browser:start'
        ]
      }, 
      include_package_data=True,
      zip_safe=False)
