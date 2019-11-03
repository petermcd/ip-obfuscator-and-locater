from setuptools import setup, find_packages

short_description = "Simple tool to identify the Country an IP is registered" \
                    "in using the IPStack API"

with open("README.md") as readmeFile:
    readme = readmeFile.read()

additional_requirements = [
    "flake8",
    "pytest",
    "pytest-mock",
    "pytest-cov",
]

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
    setup_requires=(
        "pytest-runner"
    ),
    install_requires=[
        "requests",
        "config-parser",
    ],
    tests_require=additional_requirements,
    extras_require={"test": additional_requirements},
    packages=find_packages(
        where="IpToCountry"
    ),
)
