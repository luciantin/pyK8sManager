import setuptools 

VERSION = '0.3.3' 

DESCRIPTION = 'pyK8sManager'
LONG_DESCRIPTION = 'pyK8sManager'


setuptools.setup(
        name="pyK8sManager", 
        version=VERSION,
        author="Lucian Tin Udovicic",
        author_email="luciantin@protonmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=setuptools.find_packages('.'),
        install_requires=["kubernetes"], 
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
        ]
)
