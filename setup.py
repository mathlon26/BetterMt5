import setuptools
import os


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="BetterMt5",
    version="0.0.1",
    author="Mathijs Follon",
    author_email="contact@mfollon.com",
    description="The user friendly version of the Metatrader5 python library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mathlon26/BetterMt5",
    packages=[
        "BetterMt5",
    ],
    install_requires=["MetaTrader5==5.0.45"],
    python_requires=">=3.6",
    include_package_data=True
)
