from setuptools import setup, find_packages

setup(
    name="python-cnab240-bb",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "cnab240.bancos.banco_brasil.specs": ["*.json"],
        "cnab240.bancos.bradesco.specs": ["*.json"],
        "cnab240.bancos.cecred.specs": ["*.json"],
        "cnab240.bancos.cef.specs": ["*.json"],
        "cnab240.bancos.itau.specs": ["*.json"],
        "cnab240.bancos.santander.specs": ["*.json"],
        "cnab240.bancos.sicoob.specs": ["*.json"],
        "cnab240.bancos.sicredi.specs": ["*.json"],
    },
    install_requires=[
        "python-dateutil"
    ],
    author="Alexandre Ferreira",
    description="Geração de arquivos CNAB240 para o Banco do Brasil adaptado com campos válidos para boletos.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Alexandre-Dev1010/python-cnab240-bb",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
