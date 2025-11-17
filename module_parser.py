"""Module parser for reading modular synthesizer module definitions from markdown files."""

import yaml
from pathlib import Path
from typing import List, Optional
from dataclasses import dataclass


@dataclass
class Module:
    """Represents a modular synthesizer module with inputs and outputs."""
    name: str
    inputs: List[str]
    outputs: List[str]

    def __repr__(self):
        return f"Module(name='{self.name}', inputs={len(self.inputs)}, outputs={len(self.outputs)})"


def parse_module_file(file_path: Path) -> Optional[Module]:
    """
    Parse a single markdown file and extract module information from frontmatter.

    Args:
        file_path: Path to the markdown file

    Returns:
        Module object with name, inputs, and outputs

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Module file not found: {file_path}")

    # Read file content
    content = file_path.read_text(encoding='utf-8')

    # Extract frontmatter
    frontmatter = {}
    if content.startswith('---'):
        try:
            # Split by frontmatter delimiters
            parts = content.split('---', 2)
            if len(parts) >= 3:
                yaml_content = parts[1]
                frontmatter = yaml.safe_load(yaml_content) or {}
        except yaml.YAMLError:
            # If YAML parsing fails, use empty frontmatter
            frontmatter = {}

    # Extract module name from filename (without .md extension)
    module_name = file_path.stem

    # Extract inputs and outputs, defaulting to empty lists
    inputs = frontmatter.get('inputs', [])
    outputs = frontmatter.get('outputs', [])

    # Ensure they are lists
    if not isinstance(inputs, list):
        inputs = []
    if not isinstance(outputs, list):
        outputs = []

    return Module(
        name=module_name,
        inputs=inputs,
        outputs=outputs
    )


def load_modules_from_directory(directory_path: Path) -> List[Module]:
    """
    Load all module definitions from markdown files in a directory.

    Args:
        directory_path: Path to directory containing module markdown files

    Returns:
        List of Module objects

    Raises:
        FileNotFoundError: If directory doesn't exist
        ValueError: If directory path is invalid
    """
    directory_path = Path(directory_path)

    if not directory_path.exists():
        raise FileNotFoundError(f"Directory not found: {directory_path}")

    if not directory_path.is_dir():
        raise ValueError(f"Path is not a directory: {directory_path}")

    modules = []

    # Find all markdown files in directory
    for md_file in directory_path.glob('*.md'):
        try:
            module = parse_module_file(md_file)
            if module:
                modules.append(module)
        except Exception as e:
            # Skip files that can't be parsed
            print(f"Warning: Could not parse {md_file}: {e}")
            continue

    return modules
