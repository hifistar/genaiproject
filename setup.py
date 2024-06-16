from setuptools import find_packages, setup

setup(
    name='genaiproject',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    description='GEN AI Project',
    author='Amol',
    license='MIT',
    install_requires=[
        'pandas',
        'numpy',
       'scikit-learn',
       'matplotlib',
       'seaborn',
        'jupyter',
        'jupyterlab',
        'jupyter_contrib_nbextensions',
        'jupyter_nbextensions_configurator'
    ]
)
