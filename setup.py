from setuptools import setup, find_packages

setup(
    name='fusionLM',
    version='1.0.0',
    description='A SDK for interacting with your API service',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/your_sdk_package',
    author='Your Name',
    author_email='your_email@example.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='sdk api ',
    packages=find_packages(),
    install_requires=[
        'openai',
    ],
    python_requires='>=3.8',
)

