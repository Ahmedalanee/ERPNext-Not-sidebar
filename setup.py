from setuptools import setup, find_packages

setup(
    name='my_custom_app',
    version='0.0.1',
    description='Custom app to hide sidebar in ERPNext desk',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
)