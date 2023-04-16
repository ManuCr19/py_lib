from setuptools import setup, find_packages

setup(
    name='manucr19_py',
    version='1.0.2',
    url='https://github.com/manucr19/library',
    packages=find_packages(),
    license='GPLv3',
    install_requires=[
        'pythondialog',
        'subprocess.run'
    ]
)
