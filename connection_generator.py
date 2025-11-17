"""Random connection generator for modular synthesizer patches."""

import random
from typing import List, Optional
from dataclasses import dataclass
from module_parser import Module


@dataclass
class Connection:
    """Represents a patch cable connection between two modules."""
    source_module: Module
    source_output: str
    dest_module: Module
    dest_input: str

    def __repr__(self):
        return f"{self.source_module.name} [{self.source_output}] → {self.dest_module.name} [{self.dest_input}]"


def generate_random_connections(
    modules: List[Module],
    count: int,
    seed: Optional[int] = None
) -> List[Connection]:
    """
    Generate random patch connections between modules.

    Args:
        modules: List of Module objects to connect
        count: Number of connections to generate
        seed: Optional random seed for deterministic results

    Returns:
        List of Connection objects

    Raises:
        ValueError: If module list is empty or insufficient modules for connections
    """
    if not modules:
        raise ValueError("Cannot generate connections: module list is empty")

    # Set random seed if provided
    if seed is not None:
        random.seed(seed)

    # Filter modules that can be sources (have outputs)
    source_modules = [m for m in modules if m.outputs]

    # Filter modules that can be destinations (have inputs)
    dest_modules = [m for m in modules if m.inputs]

    if not source_modules:
        raise ValueError("No modules with outputs available")

    if not dest_modules:
        raise ValueError("No modules with inputs available")

    # Check if there's at least one valid source-dest pair (no self-connections)
    valid_pairs = []
    for src in source_modules:
        for dst in dest_modules:
            if src != dst:
                valid_pairs.append((src, dst))

    if not valid_pairs:
        raise ValueError(
            "Insufficient modules for connections: "
            "need at least 2 different modules with compatible inputs/outputs"
        )

    connections = []

    for _ in range(count):
        # Pick a random valid source-dest pair
        source, dest = random.choice(valid_pairs)

        # Select random output from source
        output = random.choice(source.outputs)

        # Select random input from destination
        input_port = random.choice(dest.inputs)

        # Create connection
        connection = Connection(
            source_module=source,
            source_output=output,
            dest_module=dest,
            dest_input=input_port
        )

        connections.append(connection)

    return connections
