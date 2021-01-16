import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="devops-challenge-vchslav", # Replace with your own username
    version="0.0.1",
    author="Slava Bikov",
    author_email="slava.bikov@gmail.com",
    description="Simple Flask app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/devops-challenge-vchslav-v001",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)