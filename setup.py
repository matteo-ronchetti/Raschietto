from setuptools import setup

setup(
    name='raschietto',
    packages=['raschietto'],
    version='0.1.1',
    description='A simple web scraping library',
    author='Matteo Ronchetti',
    author_email='mttronchetti@gmail.com',
    url='https://github.com/matteo-ronchetti/raschietto',
    install_requires=['lxml', 'cssselect', 'requests>=2.18.4', 'urllib3'],
    keywords=['scraping', 'web'],  # arbitrary keywords
    classifiers=['Programming Language :: Python :: 3'],
)
