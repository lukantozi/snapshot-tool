from setuptools import setup, find_packages
setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={"console_scripts": ["snapshot = snapshot.snapshot:main"]},
    install_requires=["psutil==7.2.2", "packaging==26.0", "setuptools==82.0.1"],
    version="0.1",
    author="Luka Mamrikishvili",
    author_email="lukamamrik@proton.me",
    description="System snapshot tool")
