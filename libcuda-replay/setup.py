# SPDX-FileCopyrightText: 2019,2021,2023 University of Rochester
#
# SPDX-License-Identifier: MIT

from setuptools import setup

setup(name='libcudareplay',
      version='0.1',
      packages=['libcudareplay'],
      scripts=['libcudareplay/pack_api_trace.py']
)
