from setuptools import setup, find_packages

setup(
    name="poker-hands",
    version="0.1.0",
    description="Texas Hold'em Poker Hands Kata",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
        ]
    },
)
