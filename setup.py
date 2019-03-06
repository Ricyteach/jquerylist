from setuptools import setup, find_packages

requirements = ['IPython', 'ipywidgets', 'traitlets']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author='Ricky L Teachey Jr',
    author_email='ricky@teachey.org',
    name='jquerylist',
    version='0.1',
    packages=find_packages(include=['jquerylist']),
    url='https://github.com/Ricyteach/jquerylist',
    install_requires=requirements,
    license='MIT',
    description='A sequence object created from the indexes of DOM elements matching a JQuery string.',
    setup_requires = setup_requirements,
    test_suite = 'tests',
    tests_require = test_requirements,
)
