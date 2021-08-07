import setuptools

if __name__ == '__main__':
    setuptools.setup(
        name='pytest-takeltest',
        version='0.9.2',
        author='Takelwerk',
        author_email='takeltest@takelwerk.net',
        description='Fixtures for ansible, testinfra and molecule',
        long_description='See takelage-var at github: '
                         'https://github.com/takelwerk/takelage-var',
        url='https://github.com/takelwerk/takelage-var',
        license='GPLv3',
        packages=setuptools.find_packages(),
        package_data={
            '': ['*.md'],
        },
        entry_points={
            'pytest11': ['takeltest=takeltest.plugin']
        },
        install_requires=[
            'ansible>=2.8',
        ],
        platforms='any',
        zip_safe=False,
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Intended Audience :: Information Technology',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: MIT License',
            'Operating System :: POSIX',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: Testing',
            'Topic :: System :: Systems Administration',
            'Framework :: Pytest',
        ],
    )
