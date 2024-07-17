from setuptools import setup, find_packages

setup(
    name='hexlet-code',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gendiff=gendiff.scripts.gendiff:main',
        ],
    },
    install_requires=[
        # Здесь можно указать зависимости вашего проекта
    ],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
