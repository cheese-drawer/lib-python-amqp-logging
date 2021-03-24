import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="amqp_logging",
    version="0.1.0a",
    author="Andrew Chang-DeWitt",
    author_email="andrew@andrew-chang-dewitt.dev",
    description="Async logging library for sending records over AMQP.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cheese-drawer/lib-python-amqp-logging/",
    packages=setuptools.find_packages(),
    package_data={
        'amqp_logging': ['py.typed']},
    install_requires=[
        'aio-pika>=6.7.1,<7.0.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
