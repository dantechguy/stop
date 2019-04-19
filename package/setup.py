import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stop-dantechguy",
    version="0.0.1",
    author="Daniel Wendon-Blixrud",
    author_email="d@nielwb.com",
    description="Scratch in Python, and conversion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dantechguy/stop",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)