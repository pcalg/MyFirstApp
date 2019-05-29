from setuptools import setup

setup(
    name='MyFirstApp',
    version='1.0',
    packages=['myapp', 'myapp.calculations'],
    entry_points={
        'console_scripts': ['myapp = myapp.__main__:main']
    },
    url='',
    license='Expensive!',
    author='pcalg',
    author_email='',
    description='Very expensive and cool app'
)
