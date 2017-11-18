from setuptools import setup
from setuptools import find_packages

install_requires = [
    'pygments',
    'prompt_toolkit',
    'gevent',
    'importlib',
    'termcolor'
]
test_requires = []

setup(
    name='miniCli',
    version='0.1',
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'
    ]
)