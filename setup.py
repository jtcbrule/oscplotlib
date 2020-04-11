import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oscplotlib",
    version="0.1.0",
    author="Joshua Brule",
    author_email="jtcbrule@gmail.com",
    description="OSC1337 wrapper for Matplotlib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jtcbrule/oscplotlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    install_requires=['matplotlib']
)
