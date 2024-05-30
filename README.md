# langchain-examples
Examples of langchain concepts

## Table of Contents
- [Setup](#setup)
- [Structure](#structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [Tests](#tests)
- [License](#license)

## Setup

First, clone the repository and navigate to the project directory:

```bash
git clone git@github.com:ai-ost/langchain-examples.git
cd langchain-examples
```

Then, create a virtual environment using Python 3.12, activate the environment, and install the required packages:

```bash
python3.12 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

When you're done working, you can deactivate the virtual environment:

```bash
deactivate
```

## Structure

Here's a brief overview of the project's structure:

- `src/`: This directory contains the source code for the project.
- `tests/`: This directory contains the test files.
- `examples/`: This directory contains example scripts demonstrating the use of the project.
- `requirements.txt`: This file lists the Python dependencies required by the project.
- `README.md`: This file provides an overview of the project and information about how to install, use, and contribute to the project.

## Usage

This project contains several example files that you can run to see the concepts in action. Here's how you can run an example:

```bash
python example.py
```

Replace example.py with the name of the example file you want to run.

Here's a brief description of what each example does:

* example1.py: (Description of what example1.py does)
* example2.py: (Description of what example2.py does)
* example3.py: (Description of what example3.py does)

Please replace the placeholders with the actual names of your example files and descriptions of what they do.

Remember to activate the virtual environment before running the examples, as described in the Setup section.


## Contributing

We welcome contributions from everyone. If you're interested in contributing, we encourage you to join the [AI Öst GitHub organization](https://github.com/ai-ost) and the community at [my.ai.se](https://my.ai.se/organizations/1816).

Here are some ways you can contribute:

- **Reporting Bugs**: If you find a bug, please create an issue in the GitHub repository describing the problem and including steps to reproduce it.
- **Suggesting Enhancements**: If you have an idea for a new feature or an improvement to an existing feature, please create an issue describing your suggestion.
- **Pull Requests**: If you want to write code to fix bugs or add new features, we welcome pull requests. Please make sure to follow the existing code style.

Before submitting a pull request, please make sure your changes pass all the tests. If you're adding a new feature, please add tests that cover the new functionality.

Thank you for your interest in contributing to langchain-examples!

## Tests

This project uses pytest for testing. After setting up the project, pytest should already be installed. If not, please refer back to the [Setup](#setup) section.

You can run the tests with the following command:

```bash
pytest
```

This will automatically find all the test files (files that start with test\_ or end with \_test.py), import them, and run the test functions (functions that start with test\_) in those files.

If you want to run a specific test, you can do so by specifying the file and the test function like this:

```
pytest tests/test_file.py::test_function
```

Replace test\_file.py with the name of the test file and test\_function with the name of the test function.

If you're adding a new feature, please make sure to add tests that cover the new functionality. This helps ensure that the feature works as expected and prevents regressions in the future.


## License

MIT License

Copyright (c) 2024 AI Öst

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.