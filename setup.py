from setuptools import setup, find_packages

setup(
    name='emojext',
    version='0.1.0',
    url="https://github.com/yorukaze-luru/emojext",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'discord.py',
    ],
)
