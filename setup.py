from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """Read the requirements from a file and return them as a list."""
    requirements = []

    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.strip() for req in requirements] 
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='ml_project',
    version='0.1.0',
    author='Bijesh Mishra',
    author_email='bijeshbt@gmail.com',
    description='A machine learning project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)