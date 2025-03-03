from setuptools import setup, find_packages

setup(
    name="political-perspectives",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "transformers>=4.30.2",
        "torch>=2.0.1",
        "numpy>=1.24.3",
    ],
    author="Yevhen Leontiev",
    author_email="eleonti.it@gmail.com",
    description="A multi-agent system for balanced political analysis",
    keywords="nlp, political-analysis, multi-agent, ai",
    url="https://github.com/yourusername/political-perspectives",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
)
