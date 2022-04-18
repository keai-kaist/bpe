from setuptools import setup, find_packages

setup(
    name='bpe',
    version='1.0.0',
    author='Simcs',
    author_email='smh3946@gmail.com',
    url='https://github.com/keai-kaist/bpe',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only'
    ],
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    python_requires='>=3.8',
)