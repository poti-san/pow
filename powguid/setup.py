from setuptools import find_packages, setup

setup(
    name="powguid",
    version="0.1.0",
    install_requires=(),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
