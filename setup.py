from setuptools import setup  # type: ignore
from setuptools import find_packages


if __name__ == '__main__':
    # This is based on the instructions from
    # https://packaging.python.org/guides/making-a-pypi-friendly-readme/
    from os import path
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as readme_file:
        long_description = readme_file.read()

    setup(
        name='downloadutil',
        version='1.0.0',
        url='https://github.com/yugabyte/downloadutil',
        author='Mikhail Bautin',
        author_email='mbautin@users.noreply.github.com',
        description='Common utilities for downloading and extracting archives',
        packages=find_packages(),
        install_requires=[],
        long_description=long_description,
        long_description_content_type='text/markdown',
        extras_require={
            # Following advice in this answer: https://stackoverflow.com/a/28842733/220215
            # Install with: pip install -e '.[dev]'
            'dev': [
                'pycodestyle',
                'mypy',
                'twine',
                'codecheck'
            ]
        },
        entry_points={
            'console_scripts': ['downloadutil=downloadutil.download_util:main'],
        }
    )
