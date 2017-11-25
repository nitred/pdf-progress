"""Setup file."""
import re
from codecs import open  # To use a consistent encoding
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
# Get version without importing, which avoids dependency issues


def get_version():
    """Get version number from the root __init__ file."""
    with open('pdf_progress/__init__.py') as version_file:
        return re.search(r"""__version__\s+=\s+(['"])(?P<version>.+?)\1""",
                         version_file.read()).group('version')


install_requires = ['future', 'PyPDF2']
test_requires = ['pytest', 'pytest-sugar', 'pytest-asyncio', 'pytest-cov', ]
setup(
    name='pdf-progress',
    description="Track the progress of PDF files over time.",
    long_description=long_description,
    version=get_version(),
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=['pytest-runner'],
    tests_require=test_requires,
    packages=find_packages(),
    zip_safe=False,
    author="Nitish Reddy Koripalli",
    download_url="".format(get_version()),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
    ],
    entry_points={
        'console_scripts': [
            'pdf-progress-wc=pdf_progress.word_count:main',
            'pdf-progress-wc-mp=pdf_progress.word_count_mp:main',
        ]
    }
)
