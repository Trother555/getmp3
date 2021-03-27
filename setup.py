import setuptools


setuptools.setup(
    name='getmp3',
    version='0.0.1',
    author='Pavel Zharov',
    author_email='trother555@gmail.com',
    description='Download mp3 from youtube video',
    long_description='TODO',
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=['ffmpeg-python', 'pytube'],
)
