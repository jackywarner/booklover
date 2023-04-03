from setuptools import setup, find_packages

setup(
    name='booklover',
    version='1.0.0',
    description='book book book',
    author='Jack Warner',
    author_email='21jackwarner@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.3.3'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
