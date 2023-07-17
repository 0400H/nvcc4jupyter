from distutils.core import setup

setup(
    name='NVCCPlugin',
    version='0.3',
    author='somebody',
    author_email='',
    py_modules=['nvcc_plugin'],
    license='LICENSE',
    description='Jupyter notebook plugin to run CUDA C/C++ code',
    long_description=open('README.md').read(),
)
