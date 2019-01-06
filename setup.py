import os
from setuptools import setup, find_packages

from helloworld import __version__, __description__


def requirements():
    with open(os.path.join(os.path.dirname(__file__), "requirements.txt")) as f:
        ret = []
        for eachline in f.readlines():
            if eachline.startswith("-"):
                continue
            if eachline.startswith("git+") \
                    or eachline.startswith("http://") \
                    or eachline.startswith("https://"):
                continue

            ret.append(eachline)

        return ret


setup(name='helloworld-kujyp',
      version=__version__,
      description=__description__,
      packages=find_packages(exclude=[]),
      entry_points="""
        [console_scripts]
        helloworld = helloworld.main:main
      """,
      include_package_data=True,
      install_requires=requirements())
