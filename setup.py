"""Example market maker strategy for Deribit futures."""

from setuptools import setup

with open('README.md', 'rt') as f:
    long_description = f.read()

setup(
    name='deribit_example_marketmaker',
    version='1.0.0',
    description='An example market maker for Deribit',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/deribit/examples',

    author="Uriel Scott",
    author_email="uriel.scott@gmail.com",
    maintainer='Deribit',
    maintainer_email='contact@deribit.com',

    classifiers=[
        'Development Status :: 7 - Inactive',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='deribit marketmaker bot',
    py_modules=["market_maker"],
    install_requires=['deribit_api'],

)
