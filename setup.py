from setuptools import setup, find_packages

setup(
    name='maketests',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'maketests = driver.driver.module:main',
        ],
    },
)
