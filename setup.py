import re
from pathlib import Path

from setuptools import setup

with open(Path("fastapi_vo") / "__init__.py", encoding="utf-8") as fh:
    version = re.search(r'__version__ = "(.*?)"', fh.read(), re.M).group(1)


setup(
    name="fastapi-vo",
    version=version,
    url="https://github.com/rennancockles/fastapi-vo",
    license="MIT",
    author="Rennan Cockles",
    author_email="rcdev@hotmail.com.br",
    description="Utilities to simplify FastAPI view objects",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=["fastapi_vo"],
    python_requires=">=3.6",
    install_requires=["fastapi"],
    keywords=["fastapi", "view objects", "model"],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development",
        "Typing :: Typed",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
