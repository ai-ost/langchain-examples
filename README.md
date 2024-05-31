# langchain-examples
Examples of langchain concepts.

This is basically a code-along with the tutorials suggested at https://python.langchain.com/v0.2/docs/introduction/

The tutorials we will cover are the following:
- https://python.langchain.com/v0.2/docs/tutorials/llm_chain/
- https://python.langchain.com/v0.2/docs/tutorials/chatbot/
- https://python.langchain.com/v0.2/docs/tutorials/retrievers/
- https://python.langchain.com/v0.2/docs/tutorials/agents/

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

### langsmith

langchain has a service called `langshith` that you can use to trace the flow of the examples.
To use it you must sign up at [langsmith](https://smith.langchain.com/) and generate a key.
You can run the examples without langsmith if you like. just dont set a key in the `.env` and set `LANGCHAIN_TRACING_V2=false`

### environment variables

One small change is made if you compare to the tutorials.
We use a `.env` file instead of the `getpass` method used in the tutorials.

**Important** You need to set your own keys in the `.env` file to make the examples work.

```
OPENAI_API_KEY=sk-proj-your-own-key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=lsv2_pt_your-own-key
```

#### Old MacOS

When using chroma the following environment variable had to be set.
```
$> export HNSWLIB_NO_NATIVE=1  
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
python src/example.py
```

Replace `example.py` with the name of the example file you want to run.

see (EXAMPLES.md) for more information about the examples.

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