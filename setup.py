# setup.py
from setuptools import setup, find_packages

setup(
    name="proj7_sql", 
    version="0.1", 
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'proj7_sql=main:main',
        ],
    },
    install_requires=[
        "databricks-sql-connector",
        "pandas",
        "python-dotenv",
    ],
    author="Fuyao Li",
)