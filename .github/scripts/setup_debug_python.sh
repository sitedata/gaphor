#!/bin/sh
# shellcheck disable=SC2086

# https://github.com/actions/python-versions/

# MIT License

# Copyright (c) 2020 GitHub

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

set -e

# PYTHON_FULL_VERSION="{{__VERSION_FULL__}}"
MAJOR_VERSION=$(echo $PYTHON_FULL_VERSION | cut -d '.' -f 1)
MINOR_VERSION=$(echo $PYTHON_FULL_VERSION | cut -d '.' -f 2)

PYTHON_MAJOR=python$MAJOR_VERSION
PYTHON_MAJOR_DOT_MINOR=python$MAJOR_VERSION.$MINOR_VERSION
PYTHON_MAJORMINOR=python$MAJOR_VERSION$MINOR_VERSION

if [ -z ${AGENT_TOOLSDIRECTORY+x} ]; then
    # No AGENT_TOOLSDIRECTORY on GitHub images
    TOOLCACHE_ROOT=$RUNNER_TOOL_CACHE
else
    TOOLCACHE_ROOT=$AGENT_TOOLSDIRECTORY
fi

PYTHON_TOOLCACHE_PATH=$TOOLCACHE_ROOT/Python
PYTHON_TOOLCACHE_VERSION_PATH=$PYTHON_TOOLCACHE_PATH/$PYTHON_FULL_VERSION
PYTHON_TOOLCACHE_VERSION_ARCH_PATH=$PYTHON_TOOLCACHE_VERSION_PATH/x64

echo "Check if Python hostedtoolcache folder exist..."
if [ ! -d $PYTHON_TOOLCACHE_PATH ]; then
    echo "Creating Python hostedtoolcache folder..."
    mkdir -p $PYTHON_TOOLCACHE_PATH
elif [ -d $PYTHON_TOOLCACHE_VERSION_PATH ]; then
    echo "Deleting Python $PYTHON_FULL_VERSION"
    rm -rf $PYTHON_TOOLCACHE_VERSION_PATH
fi

echo "Create Python $PYTHON_FULL_VERSION folder"
mkdir -p $PYTHON_TOOLCACHE_VERSION_ARCH_PATH

echo "Copy Python binaries to hostedtoolcache folder"
cd $RUNNER_TEMP/Python
cp -R ./* $PYTHON_TOOLCACHE_VERSION_ARCH_PATH
# rm $PYTHON_TOOLCACHE_VERSION_ARCH_PATH/setup.sh

cd $PYTHON_TOOLCACHE_VERSION_ARCH_PATH

echo "Create additional symlinks (Required for the UsePythonVersion Azure Pipelines task and the setup-python GitHub Action)"
ln -s ./bin/$PYTHON_MAJOR_DOT_MINOR python

cd bin/
ln -s $PYTHON_MAJOR_DOT_MINOR $PYTHON_MAJORMINOR
if [ ! -f python ]; then
    ln -s $PYTHON_MAJOR_DOT_MINOR python
fi

chmod +x ../python $PYTHON_MAJOR $PYTHON_MAJOR_DOT_MINOR $PYTHON_MAJORMINOR python

echo "Upgrading PIP..."
./python -m ensurepip
./python -m pip install --ignore-installed pip --no-warn-script-location

echo "Create complete file"
touch $PYTHON_TOOLCACHE_VERSION_PATH/x64.complete
