from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='postgrest-py',
    version='0.1.0',
    description='PostgREST client-side library',
    long_description=readme,
    author='Bobbie Soedirgo',
    author_email='bobbie@soedirgo.dev',
    url='https://github.com/soedirgo/postgrest-py',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'aiohttp<=3.6.2',
    ]
)
