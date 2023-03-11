from setuptools import find_packages, setup
from typing import List


def get_requirements(fpath:str)->List[str]:
    requirements = []
    with open(fpath) as obj:
        requirements = obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
name = "MLProjects",
version = '0.0.1',
author = 'Naveenkumar',
author_email = 'bnaveen14569@gmail.com',
packages = find_packages(),
install_requires = get_requirements("requirements.txt")
)  
     