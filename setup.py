from setuptools import find_packages, setup 
def get_requirements(file_path): 
    with open(file_path) as file: 
        requirements = file.readlines() 
        requirements = [req.replace("\n", "") for req in requirements] 
        if "-e ." in requirements: 
            requirements.remove("-e .") 
    return requirements 
setup( 
        name='myntra_scraper', 
        version='0.0.1',
        author='Daizy', 
        author_email='daizy@gmail.com', 
        packages=find_packages(), 
        install_requires=get_requirements('requirements.txt')
              )

"""
from setuptools import find_packages, setup

def get_requirements(file_path):
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name='myntra_scraper',
    version='0.0.1',
    author='Daizy',
    author_email='daizy@gmail.com',
    description="Web scraper for Myntra product reviews",
    #long_description=open("README.md").read(),
    #long_description_content_type="text/markdown",
    # url="https://github.com/DAIZYGUPTA/Myntra_Review_Scrapper_Project",
    install_requires=get_requirements('requirements.txt'),
    #python_requires=">=3.8"
    packages=find_packages()
    
)
"""