from setuptools import setup, find_packages
 
classifiers = [
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Education",
  "Operating System :: Microsoft :: Windows :: Windows 10",
  "License :: OSI Approved :: MIT License",
  "Programming Language :: Python :: 3.9"
]
 
setup(
  name="pastebinapi",
  version="1.0.0",
  description="This module allows to use Pastebin API very easily.",
  long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
  url="https://github.com/joshnoe94/pastebinapi",  
  author="ksIsCute",
  author_email="joshnoe929@gmail.com",
  license="MIT", 
  keywords="pastebinapi", 
  classifiers=classifiers,
  install_requires=["requests"],
  packages=find_packages()
)
