from setuptools import setup, find_packages

short_description = "Simple tool to identify the Country an IP is registered" \
                    "in using the IPStack API"

with open("README.md") as readmeFile:
    readme = readmeFile.read()

setup(
    name="IP Obfuscator And Locator",
    version="0.1",
    description=readme,
    long_description=readme,
    author="Peter McDonald",
    maintainer="Peter McDonald",
    url="https://github.com/petermcd/ip-obfuscator-and-locater",
    download_url="https://github.com/petermcd/ip-obfuscator-and-locater",
    license="MIT",
    keywords="ip,geolocation",
    install_requires=[
        "requests",
        "config-parser",
    ],
    tests_require=[
        "tox",
        "flake8",
        "pytest",
        "pytest-mock",
    ],
    packages=find_packages(),
)
