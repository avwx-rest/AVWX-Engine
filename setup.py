"""
avwx Package Setup
"""

from setuptools import find_namespace_packages, setup

VERSION = "1.5.9"

dependencies = [
    "geopy~=2.1",
    "httpx~=0.16",
    "python-dateutil~=2.8",
    "xmltodict~=0.12",
]

test_dependencies = ["pytest-asyncio~=0.14", "time-machine~=1.3"]

extras = {
    "scipy": ["scipy~=1.6"],
    "docs": ["mkdocs~=1.1"],
    "tests": test_dependencies,
}

setup(
    name="avwx-engine",
    version=VERSION,
    description="Aviation weather report parsing library",
    url="https://github.com/avwx-rest/avwx-engine",
    author="Michael duPont",
    author_email="michael@dupont.dev",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">= 3.7",
    install_requires=dependencies,
    packages=find_namespace_packages(include=["avwx*"]),
    package_data={"avwx.data": ["aircraft.json", "stations.json"]},
    tests_require=test_dependencies,
    extras_require=extras,
)
