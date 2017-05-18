"""Setup for trigrams.py."""
from setuptools import setup

extra_packages = {
    'testing': ['ipython', 'pytest', 'pytest-watch', 'pytest-cov',
                'test_trigrams']
}

setup(
    name='trigrams',
    desctription='Implements the Trigrams function.',
    version='0.1',
    author='Chris Hudson, James Feore, Sean Beseler',
    author_email='c.ahudson84@yahoo.com, bob@bob.com, seanwbeseler@gmail.com',
    license='MIT',
    py_modules=['trigrams'],
    package_dir={'': 'src'},
    install_requires=['random', 'io', 'sys', 'os'],
    extras_require=extra_packages,
    entry_points={
        'console_scriptes': [
            'trigrams = trigrams:main'
        ]
    }
)
