from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='Very useful code',
    author='Mariia',
    author_email='mashakeyt2209@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['cleaning=clean_folder.clean:cleaning']}
)