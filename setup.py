import setuptools

with open('README.md') as f:
    long_desc = f.read()

setuptools.setup(
    name="porron",
    version="0.0.1",
    author="Aidan Williams",
    author_email="aweraw@gmail.com",
    description="AWS API Gateway/Lambda framework",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/aweraw/porron",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
