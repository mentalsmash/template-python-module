###############################################################################
# (C) Copyright SETUP_YEAR SETUP_AUTHOR
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################
import setuptools

with open("README.md", "r") as readme_f:
    readme_contents = readme_f.read()

setuptools.setup(
    name="my_module",
    version="SETUP_VERSION",
    author="SETUP_AUTHOR",
    author_email="SETUP_EMAIL",
    description="SETUP_DESCRIPTION",
    license="License :: OSI Approved :: Apache Software License",
    long_description=readme_contents,
    long_description_content_type="text/markdown",
    url="SETUP_URL",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    python_requires='>=SETUP_PY_MIN, <4',
    install_requires=[
        # Add your pip dependencies here
        # (regenerate requirements.txt with `make venv.freeze`)
    ],
)
