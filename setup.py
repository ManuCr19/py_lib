from setuptools import setup, find_packages

setup(
    name='manucr19-py',
    version='0.1',
    url='https://github.com/manucr19/library',
    packages=find_packages(),
    license='GPLv3',
    install_requires=[
        'pythondialog',
        'subprocess.run'
    ]
)
