from setuptools import setup, find_packages

setup(
    name='vow',
    version='0.1',
    packages=['vow'],
    install_requires=[
        'subprocess', 'sys', 'openai', 'dotenv', 'os'
    ],
    entry_points={
        "console_scripts": [
            "vow = vow.vow:main",
        ],
    },
    # Additional metadata
    author='Ray Song',
    author_email='yuxin_song@outlook.com',
    description='A short description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rayxsong/vow',
)
