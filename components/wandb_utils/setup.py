from setuptools import setup, find_packages

setup(
    name="wandb_utils",
    version=0.1,
    description="Utilities for interacting with Weights and Biases and mlflow",
    zip_safe=False,  # avoid eggs, which make the handling of package data cumbersome
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
    ],
    install_requires=[
        "mlflow==2.8.1",
        "wandb==0.16.0"
    ]
)
