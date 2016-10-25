from setuptools import setup
import os

packages = []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('market_manipulator'):
    # Ignore dirnames that start with '.'
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


setup(
    name='market_manipulator',
    version="0.1",
    packages=packages,
    author="P. James Joyce",
    author_email="pjamesjoyce@gmail.com",
    license=open('LICENSE.txt').read(),
    #package_data={'ocelot': package_files(os.path.join('ocelot', 'data'))},
    #entry_points = {
    #    'console_scripts': [
    #        'ocelot-cli = ocelot.bin.ocelot_cli:main',
    #    ]
    #},
    #install_requires=[
    #],
    url="https://github.com/pjamesjoyce/market_manipulator/",
    long_description=open('README.md').read(),
    description='Multifunctional market manipulator (in python) plugin for ocelot',
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
)

# Also consider:
# http://code.activestate.com/recipes/577025-loggingwebmonitor-a-central-logging-server-and-mon/


