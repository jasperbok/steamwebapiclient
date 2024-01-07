from setuptools import setup, find_packages

setup(
    name="steamwebapiclient",
    version="0.1.0",
    description="A Python client for the Steam Web API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Jasper Bok",
    author_email="hello@jasperbok.nl",
    packages=find_packages(include=["steamwebapiclient", "steamwebapiclient.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
    ],
    license="MIT License",
    keywords="steam,valve,api",
    install_requires=["requests"],
    project_urls={
        "Source": "https://github.com/jasperbok/steamwebapiclient",
    },
)
