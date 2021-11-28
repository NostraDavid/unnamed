from pathlib import Path
from typing import Any, Dict

from setuptools import find_packages, setup

here = Path(__file__).parent

with (here / "requirements" / "base.txt").open(mode="r") as requirements_file:
    requirements = requirements_file.read().splitlines()

meta: Dict[Any, Any] = {}
with (here / "src" / "unnamed" / "meta.py").open(mode="r") as meta_file:
    exec(meta_file.read(), meta)

with (here / "README.md").open(mode="r") as readme_file:
    readme = readme_file.read()

# https://packaging.python.org/guides/using-manifest-in/#how-files-are-included-in-an-sdist
setup(
    author=meta["__author__"],
    author_email=meta["__author_email__"],
    description=meta["__description__"],
    include_package_data=True,
    install_requires=requirements,
    license="None",
    long_description_content_type="text/markdown",
    long_description=readme,
    name=meta["__app_name__"],
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=["tests"]),
    python_requires=">=3.7",
    url="https://thaumatorium.com/",
    version=meta["__version__"],
    entry_points={
        "console_scripts": [
            "unnamed=unnamed.main:cli",
        ],
    },
)
