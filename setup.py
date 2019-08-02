import os
import codecs
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def read(*folders):
    with codecs.open(os.path.join(here, *folders), encoding='utf-8') as f:
        return f.read()


def get_requirements(file_name):
    requires_file = read('requirements', file_name)
    return requires_file.splitlines()


setup(
    name='scraper_api',

    version='0.0.1',

    description='Scraper API to retrieve data from useful pages',
    long_description=read('README.md'),

    url='https://github.com/machinia/scraper-api',

    author='Pablo Ahumada, Jorge Capona',
    author_email='pablo.ahumadadiaz@gmail.com, jcapona@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: System',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='scraping api wishlist amazon',
    packages=find_packages(exclude=['test']),
    install_requires=get_requirements('default.txt'),
    setup_requires=get_requirements('test.txt'),
    test_suite='test',
    extras_require={},
    package_data={},
    data_files=[],
    entry_points={},
)
