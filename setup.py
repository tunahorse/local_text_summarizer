from setuptools import setup, find_packages

setup(
    name='local_text_summarizer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'nltk',
    ],
    entry_points={
        'console_scripts': [
            'summarize=text_summarizer.summarize:main',
        ],
    },
    author='Fabian Anguiano',
    author_email='fabiananguiano@gmail',
    description='A package simple local text summarization.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/text_summarizer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
