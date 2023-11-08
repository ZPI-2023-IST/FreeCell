import setuptools


def read_from_requirements():
    with open("requirements.txt") as f:
        return [filter(f.read().splitlines(), lambda x: not x.startswith("-e"))]


setuptools.setup(
    name="freecell",
    version="0.0.1",
    author="Mateusz and Kamil",
    description="A Freecell game",
    packages=setuptools.find_packages(),
    python_requires=">=3.10",
    py_modules=["game"],
    install_requires=read_from_requirements(),
    package_dir={"": "."},
)
