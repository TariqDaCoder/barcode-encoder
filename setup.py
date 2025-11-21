# setup.py
from setuptools import setup, find_packages

setup(
    name="barcode-encoder",
    version="1.0.0",
    description="Libre Barcode 128 Encoder GUI",
    author="Tariq Hassan",
    packages=find_packages(),
    install_requires=[
        "python-docx",
        "openpyxl"
    ],
    entry_points={
        "console_scripts": [
            "barcode-encoder=gui:main"
        ]
    },
)