from setuptools import setup
from setuptools import find_packages

install_requires = [
    'pygments==2.2.0',
    'prompt_toolkit==1.0.15',
    'gevent==1.2.2',
    'importlib==1.0.4',
    'termcolor==1.1.0'
]
test_requires = []

setup(
    name='mCli',
    version='1.0.0',
    description="CLI framework for automation scripts",
    author="S.Suresh Kumar",
    author_email="sureshkumarr.s@gmail.com",
    url="https://github.com/sureshkvl/mCli",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    scripts=[],
    license="Apache",
    entry_points={
    },
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: User Interfaces',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ]
)
