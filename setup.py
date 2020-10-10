import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iomotions",
    version="0.0.2",
    author="Eric Gonzalez",
    author_email="erigonz89@gmail.com",
    description="Utilities to interface with iMotions from oTree",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT License',
    url="https://github.com/lochiego/iomotions",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)