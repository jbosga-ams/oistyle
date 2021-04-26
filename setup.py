import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oistyle",
    version="0.0.1",
    author="Jorren Bosga",
    author_email="j.bosga@amsterdam.nl",
    description="Amsterdam OIS house style.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jbosga-ams/oistyle",
    project_urls={
        "Bug Tracker": "https://github.com/jbosga-ams/oistyle/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "python"},
    packages=setuptools.find_packages(where="python"),
    python_requires=">=3.6",
)