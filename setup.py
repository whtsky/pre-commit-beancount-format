from setuptools import setup


setup(
    name="beancount_format",
    version="0.0.1",
    py_modules=["beancount_format"],
    install_requires=["beancount==3.0.0"],
    entry_points={
        "console_scripts": ["beancount_format=beancount_format:main"],
    },
)
