from setuptools import find_packages, setup

setup(
    name="clustering_project",
    packages=find_packages(exclude=["clustering_project_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
