from setuptools import setup

setup(
    name='juno',
    version='0.01',
    py_modules=['juno'],
    install_requires=['Click',],
    entry_points='''
    [console_scripts]
    juno=juno:juno
    '''
)