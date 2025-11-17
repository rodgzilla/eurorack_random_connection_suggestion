# Modular Synthesizer Random Patch Generator - Specification

## Project Overview

A Python program that generates random patch cable connection suggestions for a modular synthesizer setup. The program reads module information from markdown files and creates complete random patches by suggesting connections between module outputs and inputs.

## Data Source

### Module Files
- **Location**: Configurable directory path (default: `Modules/`)
- **Format**: Markdown files with YAML frontmatter
- **Count**: 21 modules (in default location)

### Frontmatter Structure

```yaml
---
inputs:
  - channel 1 input
  - channel 1 trig
  - pitch
  - trigger

outputs:
  - channel 1 output
  - channel 2 output
  - out

tags:
  - modular
  - vco
  - voice

manufacturer: "[[Make Noise]]"
url: https://www.makenoisemusic.com/modules/example
---
```

### Key Properties for Parsing

- **inputs** (array): List of input jacks/ports
- **outputs** (array): List of output jacks/ports
- **tags** (array): Module categorization (optional)
- **manufacturer** (string): Manufacturer name (optional)
- **url** (string): Product page URL (optional)

### Module Examples

| Module | Inputs | Outputs |
|--------|--------|---------|
| Maths | 14 | 11 |
| DFAM | 15 | 8 |
| BIA | 10 | 1 |
| Pamela's PRO Workout | 4 | 8 |

## Requirements

### Functional Requirements

1. **Complete Random Patch Generation**
   - Generate multiple connections in a single patch
   - Randomly select source modules and outputs
   - Randomly select destination modules and inputs

2. **Connection Rules**
   - Any output can connect to any input (no signal type restrictions)
   - Avoid self-connections (module connecting to itself)
   - Number of connections should be configurable

3. **Configuration**
   - Modules directory path must be configurable via command-line argument
   - Default to `Modules/` directory if not specified
   - Number of connections configurable via argument

4. **Output Format**
   - Console/text output
   - Format: `Module1 [output] → Module2 [input]`
   - Display as numbered list

### Example Output

```
Random Patch Suggestion:

1. Maths [out 1] → DFAM [pitch]
2. BIA [out] → Quad VCA [channel 1 input]
3. Pamela's PRO Workout [out 1] → Maths [ch. 1 rise]
4. DFAM [vca eg] → Ruina Versio [in l]
5. Mother-32 [vca] → Mixup [channel 1 input]
```

## Development Methodology

### Test-Driven Development (TDD)

This project follows **Test-Driven Development** principles:

1. **Write Tests First**: Write failing tests before implementing functionality
2. **Implement Minimum Code**: Write just enough code to make tests pass
3. **Refactor**: Clean up code while keeping tests green
4. **Repeat**: Continue the cycle for each feature

### Testing Requirements

- Use **pytest** as testing framework
- Aim for high test coverage (>80%)
- Test files follow naming convention: `test_*.py`
- Each module should have corresponding tests
- Include both unit tests and integration tests

### TDD Workflow

For each feature:

1. **RED**: Write a failing test
   - Define expected behavior
   - Run test and verify it fails

2. **GREEN**: Write minimal code to pass
   - Implement just enough to make test pass
   - Run test and verify it passes

3. **REFACTOR**: Clean up code
   - Improve code quality
   - Ensure tests still pass

4. **COMMIT**: Commit working code
   - Tests passing
   - Code clean

## Implementation Plan

### Phase 1: Module Parser (TDD)
**Tests First:**
- Test parsing single markdown file with frontmatter
- Test extracting inputs and outputs arrays
- Test handling missing inputs/outputs
- Test parsing all files in directory
- Test handling non-markdown files

**Implementation:**
- Parse all markdown files in specified directory (configurable path)
- Extract YAML frontmatter using PyYAML
- Create module data structure with name, inputs, outputs
- Return list of all available modules

### Phase 2: Random Connection Generator (TDD)
**Tests First:**
- Test random module selection
- Test random output selection from module
- Test random input selection from different module
- Test no self-connections are generated
- Test generating N connections
- Test handling edge cases (module with no outputs/inputs)

**Implementation:**
- Function to randomly select a source module and output
- Function to randomly select a destination module and input
- Generate N connections (configurable parameter)
- Ensure no self-connections

### Phase 3: Output Formatter (TDD)
**Tests First:**
- Test formatting single connection
- Test formatting multiple connections as numbered list
- Test proper arrow symbol rendering

**Implementation:**
- Format connections as readable text
- Display numbered list to console
- Clean, easy-to-read format

### Phase 4: CLI Interface (TDD)
**Tests First:**
- Test default arguments
- Test custom modules directory argument
- Test custom connections count argument
- Test invalid directory handling
- Test help message

**Implementation:**
- Command-line arguments for configuration
- `--modules-dir PATH` or `-d PATH` - path to modules directory (default: `Modules/`)
- `--connections N` or `-n N` - number of connections to generate (default: 5)

#### Usage Examples
```bash
# Use default Modules/ directory, generate 5 connections
python patch_generator.py

# Specify custom modules directory
python patch_generator.py --modules-dir /path/to/my/modules

# Specify directory and number of connections
python patch_generator.py -d ./synth_modules -n 10
```

## Technical Stack

### Dependencies
- **Python 3.x**
- **PyYAML** - for parsing YAML frontmatter
- **pytest** - for testing framework

### File Structure
```
random_modular_connection/
├── Modules/                    # Module markdown files
│   ├── Maths.md
│   ├── DFAM.md
│   └── ...
├── tests/                      # Test directory
│   ├── __init__.py
│   ├── test_module_parser.py  # Tests for module parsing
│   ├── test_connection_generator.py  # Tests for connection generation
│   ├── test_output_formatter.py      # Tests for output formatting
│   ├── test_cli.py            # Tests for CLI interface
│   └── fixtures/              # Test fixtures
│       └── test_modules/      # Sample module files for testing
│           ├── module1.md
│           └── module2.md
├── patch_generator.py          # Main script/entry point
├── module_parser.py            # Module parsing logic
├── connection_generator.py     # Connection generation logic
├── output_formatter.py         # Output formatting logic
├── requirements.txt            # Python dependencies
├── pytest.ini                  # Pytest configuration (optional)
├── SPECIFICATION.md            # This file
└── README.md                   # Usage instructions
```

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

# Run tests in watch mode (requires pytest-watch)
ptw
```

## Future Enhancements (Out of Scope)

- Signal type compatibility checking (audio, CV, gate)
- Patch complexity levels (sparse vs dense)
- Export to structured formats (JSON, YAML)
- Visualization of patch connections
- Weighted random selection (prefer certain modules)
- Constraint-based generation (must use specific modules)
