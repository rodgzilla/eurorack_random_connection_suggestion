import pytest
from module_parser import Module
from connection_generator import Connection, generate_random_connections


class TestConnectionGenerator:
    """Tests for random connection generation"""

    @pytest.fixture
    def sample_modules(self):
        """Create sample modules for testing"""
        return [
            Module(name="VCO", inputs=["pitch", "fm"], outputs=["out", "square"]),
            Module(name="VCA", inputs=["in", "cv"], outputs=["out"]),
            Module(name="LFO", inputs=[], outputs=["sine", "triangle", "square"]),
            Module(name="Mixer", inputs=["in1", "in2", "in3"], outputs=["mix"]),
        ]

    def test_connection_has_required_attributes(self, sample_modules):
        """Test that Connection object has all required attributes"""
        connections = generate_random_connections(sample_modules, count=1)

        assert len(connections) == 1
        connection = connections[0]

        assert hasattr(connection, 'source_module')
        assert hasattr(connection, 'source_output')
        assert hasattr(connection, 'dest_module')
        assert hasattr(connection, 'dest_input')

    def test_generate_single_connection(self, sample_modules):
        """Test generating a single random connection"""
        connections = generate_random_connections(sample_modules, count=1)

        assert len(connections) == 1
        connection = connections[0]

        # Verify connection links valid modules
        assert connection.source_module in sample_modules
        assert connection.dest_module in sample_modules

        # Verify output belongs to source module
        assert connection.source_output in connection.source_module.outputs

        # Verify input belongs to destination module
        assert connection.dest_input in connection.dest_module.inputs

    def test_generate_multiple_connections(self, sample_modules):
        """Test generating N connections"""
        count = 5
        connections = generate_random_connections(sample_modules, count=count)

        assert len(connections) == count

        # Each connection should be valid
        for connection in connections:
            assert connection.source_module in sample_modules
            assert connection.dest_module in sample_modules
            assert connection.source_output in connection.source_module.outputs
            assert connection.dest_input in connection.dest_module.inputs

    def test_no_self_connections(self, sample_modules):
        """Test that modules don't connect to themselves"""
        connections = generate_random_connections(sample_modules, count=20)

        for connection in connections:
            assert connection.source_module != connection.dest_module, \
                f"Self-connection detected: {connection.source_module.name}"

    def test_random_selection(self, sample_modules):
        """Test that connections are actually random (not always the same)"""
        # Generate two sets of connections and verify they're different
        connections1 = generate_random_connections(sample_modules, count=10, seed=42)
        connections2 = generate_random_connections(sample_modules, count=10, seed=99)

        # Convert to comparable format
        conn1_repr = [(c.source_module.name, c.source_output,
                       c.dest_module.name, c.dest_input) for c in connections1]
        conn2_repr = [(c.source_module.name, c.source_output,
                       c.dest_module.name, c.dest_input) for c in connections2]

        # At least some connections should be different
        assert conn1_repr != conn2_repr

    def test_module_with_no_outputs(self):
        """Test handling module with no outputs"""
        modules = [
            Module(name="Source", inputs=[], outputs=["out1", "out2"]),
            Module(name="NoOutput", inputs=["in"], outputs=[]),
            Module(name="Dest", inputs=["in1", "in2"], outputs=["out"]),
        ]

        # Should still generate valid connections (skipping module with no outputs)
        connections = generate_random_connections(modules, count=3)

        assert len(connections) == 3
        for conn in connections:
            # Source should never be NoOutput
            assert conn.source_module.name != "NoOutput"

    def test_module_with_no_inputs(self):
        """Test handling module with no inputs"""
        modules = [
            Module(name="Source", inputs=[], outputs=["out1", "out2"]),
            Module(name="NoInput", inputs=[], outputs=["out"]),
            Module(name="Dest", inputs=["in1", "in2"], outputs=["out"]),
        ]

        # Should still generate valid connections (skipping modules with no inputs as destinations)
        connections = generate_random_connections(modules, count=3)

        assert len(connections) == 3
        for conn in connections:
            # Destination should never be Source or NoInput (no inputs)
            assert conn.dest_module.name not in ["Source", "NoInput"]

    def test_insufficient_modules_for_connections(self):
        """Test error handling when there aren't enough valid modules"""
        # Only one module with both inputs and outputs - can't avoid self-connection
        modules = [
            Module(name="OnlyOne", inputs=["in1", "in2"], outputs=["out1", "out2"]),
        ]

        # Should raise error - can't connect without self-connections
        with pytest.raises(ValueError):
            generate_random_connections(modules, count=1)

    def test_empty_module_list(self):
        """Test error handling with empty module list"""
        with pytest.raises(ValueError):
            generate_random_connections([], count=5)

    def test_deterministic_with_seed(self, sample_modules):
        """Test that same seed produces same connections"""
        connections1 = generate_random_connections(sample_modules, count=5, seed=12345)
        connections2 = generate_random_connections(sample_modules, count=5, seed=12345)

        conn1_repr = [(c.source_module.name, c.source_output,
                       c.dest_module.name, c.dest_input) for c in connections1]
        conn2_repr = [(c.source_module.name, c.source_output,
                       c.dest_module.name, c.dest_input) for c in connections2]

        assert conn1_repr == conn2_repr
