import io
import os

from setuptools import find_packages, setup

NAME = "scrape_tools"
DESCRIPTION = "Scraping tools."
URL = "https://github.com/Pleased2Code/ScrapeTools"
EMAIL = "code.aurelien@gmail.com"
AUTHOR = "Pleased2Code"
REQUIRES_PYTHON = ">=3.6.0"

REQUIRED = [
    "certifi==2024.2.2",
    "charset-normalizer==3.3.2",
    "coverage==7.4.1",
    "exceptiongroup==1.2.0",
    "idna==3.6",
    "iniconfig==2.0.0",
    "packaging==23.2",
    "pluggy==1.4.0",
    "pytest==8.0.0",
    "pytest-cov==4.1.0",
    "requests==2.31.0",
    "stem==1.8.2",
    "tomli==2.0.1",
    "urllib3==2.2.0",
]

EXTRAS = {}


here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
with open(os.path.join(here, project_slug, "__version__.py")) as f:
    exec(f.read(), about)


setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*"], where="."
    ),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license="MIT",
)
