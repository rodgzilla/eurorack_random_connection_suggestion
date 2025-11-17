import pytest
import os
from pathlib import Path
from module_parser import parse_module_file, load_modules_from_directory, Module


class TestModuleParser:
    """Tests for module parser functionality"""

    @pytest.fixture
    def test_modules_dir(self):
        """Return path to test modules directory"""
        return Path(__file__).parent / "fixtures" / "test_modules"

    @pytest.fixture
    def test_vco_path(self, test_modules_dir):
        """Return path to test VCO module"""
        return test_modules_dir / "test_vco.md"

    @pytest.fixture
    def test_vca_path(self, test_modules_dir):
        """Return path to test VCA module"""
        return test_modules_dir / "test_vca.md"

    @pytest.fixture
    def test_no_inputs_path(self, test_modules_dir):
        """Return path to module with no inputs"""
        return test_modules_dir / "test_no_inputs.md"

    def test_parse_single_module_file(self, test_vco_path):
        """Test parsing a single markdown file with frontmatter"""
        module = parse_module_file(test_vco_path)

        assert module is not None
        assert module.name == "test_vco"
        assert isinstance(module.inputs, list)
        assert isinstance(module.outputs, list)

    def test_extract_inputs_and_outputs(self, test_vco_path):
        """Test extracting inputs and outputs arrays from frontmatter"""
        module = parse_module_file(test_vco_path)

        assert "pitch" in module.inputs
        assert "fm" in module.inputs
        assert "sync" in module.inputs
        assert len(module.inputs) == 3

        assert "out" in module.outputs
        assert "square" in module.outputs
        assert len(module.outputs) == 2

    def test_module_with_no_inputs(self, test_no_inputs_path):
        """Test handling module with missing inputs (only outputs)"""
        module = parse_module_file(test_no_inputs_path)

        assert module is not None
        assert module.name == "test_no_inputs"
        assert module.inputs == []  # Should default to empty list
        assert len(module.outputs) == 2
        assert "clock" in module.outputs
        assert "gate" in module.outputs

    def test_load_all_modules_from_directory(self, test_modules_dir):
        """Test parsing all markdown files in a directory"""
        modules = load_modules_from_directory(test_modules_dir)

        assert len(modules) >= 3  # At least our 3 test modules
        module_names = [m.name for m in modules]
        assert "test_vco" in module_names
        assert "test_vca" in module_names
        assert "test_no_inputs" in module_names

    def test_invalid_directory_path(self):
        """Test handling invalid directory path"""
        with pytest.raises((FileNotFoundError, ValueError)):
            load_modules_from_directory("/nonexistent/path")

    def test_module_has_all_required_attributes(self, test_vca_path):
        """Test that Module object has all required attributes"""
        module = parse_module_file(test_vca_path)

        assert hasattr(module, 'name')
        assert hasattr(module, 'inputs')
        assert hasattr(module, 'outputs')

    def test_empty_frontmatter(self, tmp_path):
        """Test handling file with empty or invalid frontmatter"""
        # Create a test file with no frontmatter
        test_file = tmp_path / "empty.md"
        test_file.write_text("# Just a heading\n\nNo frontmatter here.")

        module = parse_module_file(test_file)

        # Should still create a module with empty inputs/outputs
        assert module is not None
        assert module.inputs == []
        assert module.outputs == []
