import setuptools

setuptools.setup(
    name="freecell",
    version="0.0.1",
    author="Mateusz and Kamil",
    description="A Freecell game",
    packages=setuptools.find_packages(),
    python_requires=">=3.10",
    py_modules=["game"],
    install_requires=open("requirements.txt").read().splitlines(),
    package_dir={"": "."},
)
