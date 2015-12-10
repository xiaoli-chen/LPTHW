try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Xiaoli Chen',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'xiaoli_chen@umail.ucsb.edu.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['sentence'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
