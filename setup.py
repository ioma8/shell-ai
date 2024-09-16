from setuptools import setup, find_packages

# Read requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Read README.md
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sacg',
    version='0.1.0',
    author='Jakub Kolcar',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        'dev': ['setuptools', 'wheel', 'twine']
    },
    entry_points={
        'console_scripts': [
            'sacg=sacg.main:main',
        ],
    },
)
