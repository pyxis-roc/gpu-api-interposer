from setuptools import setup

setup(name='libcudareplay',
      version='0.1',
      packages=['libcudareplay'],
      install_requires=['pycapnp',
                        'pkgconfig',
                        'cython'],
)
