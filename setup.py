from distutils.core import setup

setup(
    name='j2',
    version='0.1',
    description='Jinja template renderer command',
    author='Ruslan Zhenetl',
    author_email='nc6401+gthb@gmail.com',
    url='https://github.com/c6401/j2',
    license='MIT',
    install_requires=[
        'fire==0.1.3',
        'Jinja2==2.10.3',
        'PyYAML==5.4',
    ],
    scripts=['j2'],
)
