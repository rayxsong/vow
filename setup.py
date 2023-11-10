from setuptools import setup, find_packages

setup(
    name='vow',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'subprocess', 'sys', 'openai', 'dotenv', 'os'
    ],
    entry_points={
        'console_scripts': [
            'my-command=my_package.my_script:main',
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
