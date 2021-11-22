# Doxygen to Confluence

[![Lint](https://github.com/cledouarec/doxygen2confluence/actions/workflows/lint.yaml/badge.svg)](https://github.com/cledouarec/doxygen2confluence/actions/workflows/lint.yaml)
[![Unit tests](https://github.com/cledouarec/doxygen2confluence/actions/workflows/test.yaml/badge.svg)](https://github.com/cledouarec/doxygen2confluence/actions/workflows/test.yaml)

**Table of Contents**
* [Overview](#Overview)
* [Installation](#Installation)
* [Usage](#Usage)
* [Configuration](#Configuration)

## Overview

Doxygen2Confluence is a module and a script used to convert Doxygen XML output
to Confluence wiki format.

## Installation

### From PyPI (Recommended)

You can install the converter easily with the following command or insert into
your requirements file :
```
pip install doxygen2confluence
```

### From sources

It is recommended to use a virtual environment :
```
python -m venv venv
```
To install the module and the main script, simply do :
```
pip install .
```
For the developers, it is useful to install extra tools like :
* [pre-commit](https://pre-commit.com)
* [pytest](http://docs.pytest.org)

These tools can be installed with the following command :
```
pip install .[dev]
```
The Git hooks can be installed with :
```
pre-commit install
```
The hooks can be run manually at any time :
```
pre-commit run --all-file
```

## Usage

The script with required argument can be started by executing the following
command :
```
./doxygen2confluence my_config.yaml
```

The full list of arguments supported can be displayed with the following
helper :
```
./doxygen2confluence -h
TBC
```

## Configuration

The configuration file support 2 formats :
- [YAML format](https://yaml.org) (Recommended format)
- [JSON format](https://www.json.org)

**_In Yaml :_**
```yaml
Server:
  Confluence: "https://my.confluence.server.com"
```
**_In Json :_**
```json
{
  "Server": {
    "Confluence": "https://my.confluence.server.com"
  }
}
```

The space key can be found easily in the URL of any page :
```
https://my_confluence_url.com/display/<Space key>/...
```

### Server configuration

The `Server` node will configure the URL of the Confluence server.
For the moment, only the username/password authentication is supported but only
in the command line for security reason.

**_In Yaml :_**
```yaml
Server:
  Confluence: "https://my.confluence.server.com"
```
**_In Json :_**
```json
{
  "Server": {
    "Confluence": "https://my.confluence.server.com"
  }
}
```

#### Server

Main configuration node for server.  
**It is a mandatory field.**

#### Confluence

Define the Confluence server URL to write the documentation pages.  
**It is a mandatory field.**
