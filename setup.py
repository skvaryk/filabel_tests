from setuptools import setup, find_packages

with open('README.adoc') as f:
    long_description = ''.join(f.readlines())

setup(
    name='filabel_tests',
    version='0.4',
    keywords='github labels management pull-requests globs',
    description='Simple CLI & WEB tool for labeling GitHub PRs using globs',
    long_description=long_description,
    author='Marek Alexa',
    author_email='alexama1@fit.cvut.cz',
    license='MIT',
    url='https://github.com/skvaryk/filabel_tests',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    package_data={
        'filabel': [
            'static/*.css',
            'templates/*.html',
        ]
    },
    entry_points={
        'console_scripts': [
            'filabel = filabel:cli',
        ]
    },
    install_requires=[
        'click',
        'Flask',
        'jinja2',
        'requests',
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'click',
        'Flask',
        'jinja2',
        'requests',
        'pytest',
        'betamax'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
