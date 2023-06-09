Copyright (c) 2018 Uber Technologies, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

# OpenVSP Python Packages

## Background

This repository of Python packages is designed to assist in the analysis of
aircraft, with a special interest in VTOL aircraft.  These packages extend the
OpenVSP Python API.

## Installation

Before installation, ensure you have installed Python via Anaconda or
Miniconda.  Conda is required for the environment management utilized in this
repository.  When installing via Anaconda or Miniconda, pip should also be
installed, but it is worth verifying that this has been done.

### Windows Installation Only

1. Open a Windows PowerShell
2. Navigate to the location of this README.md file
3. Execute `./setup.ps1`

### Mac OS Installation (via BASH)

1. Open a terminal window and navigate to the location of this README.md file
2. Execute `conda env create -f ./environment.yml
3. Execute `conda activate vsppytools`
4. Execute `pip install -r requirements.txt`

   Note: You can install `requirements-dev.txt` if you are going to modify the Python packages. See [the pip install documents](https://pip.pypa.io/en/stable/cli/pip_install/#cmdoption-e) for more info on installing with `-e`.

### Linux Installation (via BASH)

Linux users often use OpenVSP as installed by their packaging system in a
location such as /opt/OpenVSP.  The final step of this process required write
permissions.  You shouldn't need to do this as root, so we'll start by copying
all the files somewhere you will have write access.

1. Open a terminal window and navigate to the location of this README.md file.  If you have write permissions, continue with the MacOS instructions above.
2. Execute `cd ..; cp -r python /tmp/vsptemp; cd /tmp/vsptemp`
3. Execute `conda env create -f ./environment.yml
4. Execute `conda activate vsppytools`
5. Execute `pip install -r requirements.txt`

   Note: You can install `requirements-dev.txt` if you are going to modify the Python packages. See [the pip install documents](https://pip.pypa.io/en/stable/cli/pip_install/#cmdoption-e) for more info on installing with `-e`.

## Uninstall Directions

To uninstall the vsppytools packages, simply invoke `pip uninstall -r
requirements-uninstall.txt`

## OpenVSP to CHARM Automation

Instructions for setting up the OpenVSP to CHARM automation process can be found
in the CHARM Python package [README](./CHARM/README.md).  Ensure that this
installation process above has been completed successfully before setting up the
CHARM automation.
