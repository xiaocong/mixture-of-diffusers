import os
from setuptools import setup


# Read long description from readme
with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()


# Get tag from Github environment variables
TAG = os.environ['GITHUB_TAG'] if 'GITHUB_TAG' in os.environ else "0.0.0"


setup(
    name="mixdiff",
    version=TAG,
    description="Mixture of Diffusers for scene composition and high resolution image generation .",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=['mixdiff'],
    install_requires=[
        'numpy',
        'torch',
        'torchvision',
        'tqdm',
        'scipy',
        'diffusers[torch]',
        'ftfy',
        'gitpython',
        'ligo-segments',
        'torchvision',
        'transformers'
    ],
    author="Alvaro Barbero",
    url='https://github.com/xiaocong/mixture-of-diffusers',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: GPU :: NVIDIA CUDA',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Artistic Software',
        'Topic :: Multimedia :: Graphics'
    ],
    keywords='artificial-intelligence, deep-learning, diffusion-models',
    test_suite="pytest",
)
