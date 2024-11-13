from setuptools import setup, find_packages\n\nsetup(\n    name='project_name',\n    version='0.1',\n    packages=find_packages(where='src'),\n    package_dir={'': 'src'},\n)
