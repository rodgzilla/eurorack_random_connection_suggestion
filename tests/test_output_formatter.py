import pytest
from module_parser import Module
from connection_generator import Connection
from output_formatter import format_patch, format_connection


class TestOutputFormatter:
    """Tests for output formatting"""

    @pytest.fixture
    def sample_connection(self):
        """Create a sample connection for testing"""
        source = Module(name="Maths", inputs=["ch. 1"], outputs=["out 1", "out 2"])
        dest = Module(name="DFAM", inputs=["pitch", "vca eg"], outputs=["out"])
        return Connection(
            source_module=source,
            source_output="out 1",
            dest_module=dest,
            dest_input="pitch"
        )

    @pytest.fixture
    def sample_connections(self):
        """Create multiple sample connections for testing"""
        vco = Module(name="VCO", inputs=["pitch"], outputs=["out", "square"])
        vca = Module(name="VCA", inputs=["in", "cv"], outputs=["out"])
        lfo = Module(name="LFO", inputs=[], outputs=["sine", "triangle"])
        mixer = Module(name="Mixer", inputs=["in1", "in2"], outputs=["mix"])

        return [
            Connection(vco, "out", vca, "in"),
            Connection(lfo, "sine", vca, "cv"),
            Connection(vca, "out", mixer, "in1"),
        ]

    def test_format_single_connection(self, sample_connection):
        """Test formatting a single connection"""
        formatted = format_connection(sample_connection)

        assert isinstance(formatted, str)
        assert "Maths" in formatted
        assert "out 1" in formatted
        assert "DFAM" in formatted
        assert "pitch" in formatted
        assert "→" in formatted

    def test_format_connection_structure(self, sample_connection):
        """Test the exact format of a connection"""
        formatted = format_connection(sample_connection)

        # Expected format: "Module1 [output] → Module2 [input]"
        assert formatted == "Maths [out 1] → DFAM [pitch]"

    def test_format_patch_with_title(self, sample_connections):
        """Test formatting a complete patch with title"""
        formatted = format_patch(sample_connections, include_title=True)

        assert isinstance(formatted, str)
        assert "Random Patch" in formatted or "Patch" in formatted

    def test_format_patch_numbered_list(self, sample_connections):
        """Test that patch is formatted as numbered list"""
        formatted = format_patch(sample_connections, include_title=False)

        lines = formatted.strip().split('\n')

        # Should have 3 lines (one per connection)
        assert len(lines) == 3

        # Each line should start with a number
        assert lines[0].startswith("1.")
        assert lines[1].startswith("2.")
        assert lines[2].startswith("3.")

    def test_format_patch_includes_all_connections(self, sample_connections):
        """Test that all connections are included in the output"""
        formatted = format_patch(sample_connections, include_title=False)

        # Check all modules are mentioned
        assert "VCO" in formatted
        assert "VCA" in formatted
        assert "LFO" in formatted
        assert "Mixer" in formatted

        # Check connection details
        assert "[out]" in formatted
        assert "[sine]" in formatted
        assert "[in]" in formatted

    def test_format_empty_patch(self):
        """Test formatting an empty patch"""
        formatted = format_patch([], include_title=False)

        assert isinstance(formatted, str)
        # Should either be empty or have a message
        assert len(formatted.strip()) == 0 or "no connections" in formatted.lower()

    def test_format_patch_with_special_characters(self):
        """Test formatting connections with special characters in names"""
        source = Module(name="Channel-1", inputs=[], outputs=["out / main"])
        dest = Module(name="Mix (L/R)", inputs=["input 1"], outputs=[])

        connection = Connection(source, "out / main", dest, "input 1")
        formatted = format_connection(connection)

        assert "Channel-1" in formatted
        assert "out / main" in formatted
        assert "Mix (L/R)" in formatted
        assert "input 1" in formatted
        assert "→" in formatted

    def test_format_patch_complete_output(self, sample_connections):
        """Test complete patch output with title"""
        formatted = format_patch(sample_connections, include_title=True)

        lines = formatted.strip().split('\n')

        # Should have at least 4 lines (title + 3 connections)
        assert len(lines) >= 3

        # Verify structure
        assert any("1." in line for line in lines)
        assert any("→" in line for line in lines)
