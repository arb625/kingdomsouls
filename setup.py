from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="kingdomsouls",
    version="1.0.0",
    description="Game where you can create, train, and battle with characters.",
    url="https://github.com/arb625/kingdomsouls.git",
    author="a-baddam",
    author_email="baddamanu@gmail.com",
    packages=["kingdomsouls", "kingdomsouls.commands", "kingdomsouls.tests"],
    zip_safe=False,
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["kingdomsouls = kingdomsouls.main:initialize"]},
    install_requires=["click"],
)
