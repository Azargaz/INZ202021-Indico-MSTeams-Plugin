# This file is part of the Indico plugins.
# Copyright (C) 2002 - 2020 CERN
#
# The Indico plugins are free software; you can redistribute
# them and/or modify them under the terms of the MIT License;
# see the LICENSE file for more details.

from __future__ import unicode_literals

from setuptools import find_packages, setup


setup(
    name='indico-plugin-vc-ms-teams',
    version='1.0',
    description='MsTeams/Microsoft Teams video-conferencing plugin for Indico',
    url='https://github.com/Azargaz/INZ202021-Indico-MSTeams-Plugin',
    license='MIT',
    author='Hubert Jakubek',
    author_email='hjakubek9@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'indico>=2.0'
    ],
    classifiers=[
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    entry_points={'indico.plugins': {'vc_ms_teams = indico_vc_ms_teams.plugin:MsTeamsPlugin'}}
)
