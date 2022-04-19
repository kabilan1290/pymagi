from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(

    name="pymagi",  # Required

    version="0.0.1",  # Required

    description="A python based client for CyberChef API server.",  # Optional

    long_description=long_description,  # Optional

    long_description_content_type="text/markdown",  # Optional (see note above)

    url="https://github.com/kabilan1290/pymagi",  # Optional

    author="Game0v3r",  # Optional

    author_email="tamiltuts1290@gmail.com",  # Optional

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3",

    ],

    keywords="cyberchef","ctf tool","ctf toolkit","decoder",  # Optional

    py_modules="pymagi"
 
    package_dir={"": "src"},  # Optional


    python_requires=">=3.6, <4",

    install_requires=["requests","json"],  # Optional
 

)