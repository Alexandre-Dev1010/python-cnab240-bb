from setuptools import setup, find_packages

setup(
    name="python-cnab240-bb",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["*.json"]},
    install_requires=[
        "python-dateutil"
    ],
    author="Alexandre Ferreira",
    description="Geração de arquivos CNAB240 para o Banco do Brasil adaptado com campos válidos para boletos.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Alexandre-Dev1010/python-cnab240-bb",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)
