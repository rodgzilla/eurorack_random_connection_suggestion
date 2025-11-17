"""Output formatter for displaying patch connections."""

from typing import List
from connection_generator import Connection


def format_connection(connection: Connection) -> str:
    """
    Format a single connection as a readable string.

    Args:
        connection: Connection object to format

    Returns:
        Formatted string in the format "Module1 [output] → Module2 [input]"
    """
    return (
        f"{connection.source_module.name} [{connection.source_output}] "
        f"→ {connection.dest_module.name} [{connection.dest_input}]"
    )


def format_patch(connections: List[Connection], include_title: bool = True) -> str:
    """
    Format a complete patch as a numbered list of connections.

    Args:
        connections: List of Connection objects
        include_title: Whether to include a title header

    Returns:
        Formatted string with numbered list of connections
    """
    if not connections:
        return ""

    lines = []

    if include_title:
        lines.append("Random Patch Suggestion:")
        lines.append("")

    for i, connection in enumerate(connections, start=1):
        formatted_connection = format_connection(connection)
        lines.append(f"{i}. {formatted_connection}")

    return "\n".join(lines)
