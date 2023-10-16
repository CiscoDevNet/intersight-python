from setuptools import setup, find_packages

NAME = "intersight"
VERSION = "1.0.11.13892"
REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
  "pem>=19.3.0",
  "pycryptodome>=3.9.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="The Python SDK for Cisco Intersight",
    author="Intersight API support",
    author_email="intersight@cisco.com",
    url="https://intersight.com",
    keywords=["Cisco Intersight"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
)

