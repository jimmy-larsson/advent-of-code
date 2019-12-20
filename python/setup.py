from setuptools import setup, find_packages


with open('../README.md') as f:
    readme = f.read()

with open('../LICENSE') as f:
    license = f.read()

setup(
    name='Advent of Code 2019',
    version='1.0.0',
    description='Python implementation of Advent of Code 2019',
    long_description=readme,
    author='Jimmy Larsson',
    author_email='90.jimmy.larsson@gmail.com',
    url='https://github.com/jimmy-larsson/advent-of-code',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
