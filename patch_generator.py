#!/usr/bin/env python3
"""
Modular Synthesizer Random Patch Generator

Generates random patch cable connection suggestions for modular synthesizers.
"""

import argparse
import sys
from pathlib import Path

from module_parser import load_modules_from_directory
from connection_generator import generate_random_connections
from output_formatter import format_patch


def parse_arguments():
    """
    Parse command-line arguments.

    Returns:
        Namespace object with parsed arguments
    """
    parser = argparse.ArgumentParser(
        description='Generate random patch connections for modular synthesizers',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                                    # Use defaults (Modules/ directory, 5 connections)
  %(prog)s --modules-dir /path/to/modules     # Specify custom modules directory
  %(prog)s -d ./synth_modules -n 10           # Use short flags for 10 connections
        """
    )

    parser.add_argument(
        '--modules-dir', '-d',
        default='Modules',
        help='Path to directory containing module markdown files (default: Modules)'
    )

    parser.add_argument(
        '--connections', '-n',
        type=int,
        default=5,
        help='Number of random connections to generate (default: 5)'
    )

    return parser.parse_args()


def main():
    """Main entry point for the patch generator."""
    args = parse_arguments()

    modules_dir = Path(args.modules_dir)
    num_connections = args.connections

    # Validate arguments
    if num_connections < 1:
        print("Error: Number of connections must be at least 1", file=sys.stderr)
        sys.exit(1)

    # Load modules from directory
    try:
        modules = load_modules_from_directory(modules_dir)
    except FileNotFoundError:
        print(f"Error: Directory not found: {modules_dir}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if not modules:
        print(f"Error: No modules found in {modules_dir}", file=sys.stderr)
        sys.exit(1)

    # Generate random connections
    try:
        connections = generate_random_connections(modules, count=num_connections)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Format and display output
    output = format_patch(connections, include_title=True)
    print(output)


if __name__ == '__main__':
    main()
