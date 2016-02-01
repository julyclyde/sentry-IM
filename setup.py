#!/usr/bin/env python
"""
sentry-IM
===============
An extension for Sentry which allows notification to instant messaging service
:copyright: (c) 2016 by the Engineering Effetive Team, TNE
:license: property
"""
from setuptools import setup


install_requires = [
    # 'sentry>=7.0.0',
]

setup(
    name='sentry-IM',
    version='0.2.1',
    author='REN Xiaolei',
    author_email='renxiaolei@meituan.com',
    description='A Sentry extension which integrates IM.',
    long_description=__doc__,
    license='property',
    packages=['sentry_IM'],
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
       'sentry.plugins': [
            'sentry_daxiang= sentry_IM.plugin:IMPlugin'
        ],
    },
    classifiers=[
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
    ],
)
