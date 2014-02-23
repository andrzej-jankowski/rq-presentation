# -*- encoding: utf-8 -*-

import sys
from setuptools import setup, find_packages


assert sys.version_info >= (3, 3), "Python 3.3+ required."


from rq_presentation import VERSION
version = ".".join(str(num) for num in VERSION)


setup(
    name='RQ Presentation',
    version=version,
    license='',
    author='Andrzej Jankowski',
    url='',
    author_email='',
    description='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django==1.6.2',
        'rq==0.3.13',
        'django_rq==0.6.1',
    ],
    entry_points={
        'console_scripts': [
            'rq_presentation = rq_presentation.__main__:main',
        ],
    },
)
