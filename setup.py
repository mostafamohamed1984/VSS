from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lead_conversion_control/__init__.py
from lead_conversion_control import __version__ as version

setup(
    name="lead_conversion_control",
    version=version,
    description="Control lead conversion options in ERPNext",
    author="Mustafa Nazier",
    author_email="mustafanazieer@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
) 