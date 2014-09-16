from setuptools import setup, find_packages


def desc():
    with open("README.md") as f:
        return f.read()


setup(
    name='frasco-twitter',
    version='0.1',
    url='http://github.com/frascoweb/frasco-twitter',
    license='MIT',
    author='Maxime Bouroumeau-Fuseau',
    author_email='maxime.bouroumeau@gmail.com',
    description="Twitter integration for Frasco",
    long_description=desc(),
    packages=find_packages(),
    platforms='any',
    install_requires=[
        'frasco',
        'frasco-users'
    ]
)