# setup.py

from setuptools import setup, find_packages

setup(
    name="mathutils",
    version="0.1.0",
    packages=find_packages(),
    author="Omkar Singh",
    author_email="singhomkar20.1995@gmail.com",
    description="A simple math operations package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/omkars20/mathutils_packagae",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
