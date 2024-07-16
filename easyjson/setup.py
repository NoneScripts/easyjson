from setuptools import setup, find_packages

setup(
    name='easyjson',
    version='0.1',
    packages=find_packages(),
    install_requires=[
    ],
    author='None scripts',
    description='библиотека easyjson немного упрощает работу с json файлами',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/твой_проект',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.4',
)