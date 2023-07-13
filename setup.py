from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in el_salvador/__init__.py
from el_salvador import __version__ as version

setup(
	name="el_salvador",
	version=version,
	description="El Salvador customizations",
	author="Juan Pablo López Garciaguirre",
	author_email="juanpablo@heavywebdesign.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
