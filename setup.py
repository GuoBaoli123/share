from setuptools import setup, find_packages

setup(
    name='myproject',  # Replace with your project's name
    version='0.1.0',
    description='A short description of the project.',
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
