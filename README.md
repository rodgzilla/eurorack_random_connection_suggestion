# Modular Synthesizer Random Patch Generator

A Python program that generates random patch cable connection suggestions for modular synthesizers. Built using Test-Driven Development (TDD). This project was entirely built using Claude Code.

## Features

- Parse module definitions from markdown files with YAML frontmatter
- Generate random connections between module outputs and inputs
- Avoid self-connections (module connecting to itself)
- Configurable number of connections
- Configurable modules directory path
- Clean, readable console output

## Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
# Generate 5 random connections (default)
python patch_generator.py

# Specify custom modules directory
python patch_generator.py --modules-dir /path/to/modules

# Generate 10 connections
python patch_generator.py --connections 10

# Use short flags
python patch_generator.py -d ./Modules -n 8
```

### Command-Line Options

- `--modules-dir`, `-d`: Path to directory containing module markdown files (default: `Modules/`)
- `--connections`, `-n`: Number of random connections to generate (default: 5)
- `--help`, `-h`: Show help message

### Example Output

```
Random Patch Suggestion:

1. Maths [out 1] → DFAM [pitch]
2. BIA [out] → Quad VCA [channel 1 input]
3. Pamela's PRO Workout [out 1] → Maths [ch. 1 rise]
4. DFAM [vca eg] → Ruina Versio [in l]
5. Mother-32 [vca] → Mixup [channel 1 input]
```

## Module File Format

Modules are defined in markdown files with YAML frontmatter:

```markdown
---
inputs:
  - pitch
  - fm
  - sync
outputs:
  - out
  - square
tags:
  - vco
  - oscillator
---

# Module Name

Description of the module...
```

## Development

This project was built using Test-Driven Development (TDD).

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_module_parser.py
```

### Test Coverage

Current test coverage: **92%**

### Project Structure

```
random_modular_connection/
├── Modules/                    # Module markdown files
├── tests/                      # Test suite
│   ├── test_module_parser.py
│   ├── test_connection_generator.py
│   ├── test_output_formatter.py
│   ├── test_cli.py
│   └── fixtures/              # Test data
├── patch_generator.py          # Main CLI entry point
├── module_parser.py            # Module parsing logic
├── connection_generator.py     # Connection generation
├── output_formatter.py         # Output formatting
├── requirements.txt            # Dependencies
├── SPECIFICATION.md            # Full specification
└── README.md                   # This file
```

## License

This project was created for personal use.
