from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='personal_assistant',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    entry_points={
        'console_scripts':
            ['personal_assistant = personal_assistant.__main__:main']
        },
    include_package_data=True,
)
