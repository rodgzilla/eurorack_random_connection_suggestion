import pytest
import sys
from pathlib import Path
from unittest.mock import patch
from io import StringIO
import patch_generator


class TestCLI:
    """Tests for command-line interface"""

    @pytest.fixture
    def test_modules_dir(self):
        """Return path to test modules directory"""
        return Path(__file__).parent / "fixtures" / "test_modules"

    def test_main_with_default_arguments(self, test_modules_dir, capsys):
        """Test running with default arguments"""
        test_args = ['patch_generator.py', '--modules-dir', str(test_modules_dir)]

        with patch.object(sys, 'argv', test_args):
            try:
                patch_generator.main()
                captured = capsys.readouterr()
                output = captured.out

                # Should output connections
                assert "→" in output
                # Should have numbered list
                assert "1." in output
            except SystemExit:
                pass

    def test_main_with_custom_connection_count(self, test_modules_dir, capsys):
        """Test specifying custom number of connections"""
        test_args = [
            'patch_generator.py',
            '--modules-dir', str(test_modules_dir),
            '--connections', '3'
        ]

        with patch.object(sys, 'argv', test_args):
            try:
                patch_generator.main()
                captured = capsys.readouterr()
                output = captured.out

                # Should have 3 connections
                lines = [line for line in output.split('\n') if line.strip() and '.' in line and '→' in line]
                assert len(lines) == 3
            except SystemExit:
                pass

    def test_main_with_short_arguments(self, test_modules_dir, capsys):
        """Test using short argument flags"""
        test_args = [
            'patch_generator.py',
            '-d', str(test_modules_dir),
            '-n', '2'
        ]

        with patch.object(sys, 'argv', test_args):
            try:
                patch_generator.main()
                captured = capsys.readouterr()
                output = captured.out

                # Should have 2 connections
                lines = [line for line in output.split('\n') if line.strip() and '.' in line and '→' in line]
                assert len(lines) == 2
            except SystemExit:
                pass

    def test_main_with_invalid_directory(self, capsys):
        """Test error handling with invalid directory"""
        test_args = [
            'patch_generator.py',
            '--modules-dir', '/nonexistent/directory'
        ]

        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                patch_generator.main()

            # Should exit with error code
            assert exc_info.value.code != 0

            captured = capsys.readouterr()
            error_output = captured.err or captured.out

            # Should have error message
            assert "error" in error_output.lower() or "not found" in error_output.lower()

    def test_main_with_help_flag(self, capsys):
        """Test --help flag shows usage information"""
        test_args = ['patch_generator.py', '--help']

        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                patch_generator.main()

            # Help should exit with 0
            assert exc_info.value.code == 0

            captured = capsys.readouterr()
            help_output = captured.out

            # Should show usage information
            assert "usage" in help_output.lower() or "help" in help_output.lower()
            assert "--modules-dir" in help_output or "-d" in help_output
            assert "--connections" in help_output or "-n" in help_output

    def test_parse_arguments_defaults(self):
        """Test argument parser returns correct defaults"""
        test_args = ['patch_generator.py']

        with patch.object(sys, 'argv', test_args):
            args = patch_generator.parse_arguments()

            assert args.modules_dir == "Modules"
            assert args.connections == 5

    def test_parse_arguments_custom_values(self, test_modules_dir):
        """Test argument parser handles custom values"""
        test_args = [
            'patch_generator.py',
            '--modules-dir', str(test_modules_dir),
            '--connections', '10'
        ]

        with patch.object(sys, 'argv', test_args):
            args = patch_generator.parse_arguments()

            assert args.modules_dir == str(test_modules_dir)
            assert args.connections == 10

    def test_output_includes_title(self, test_modules_dir, capsys):
        """Test that output includes a title"""
        test_args = [
            'patch_generator.py',
            '--modules-dir', str(test_modules_dir),
            '--connections', '2'
        ]

        with patch.object(sys, 'argv', test_args):
            try:
                patch_generator.main()
                captured = capsys.readouterr()
                output = captured.out

                # Should have title
                assert "Patch" in output or "patch" in output
            except SystemExit:
                pass

    def test_valid_connection_format_in_output(self, test_modules_dir, capsys):
        """Test that output has correct connection format"""
        test_args = [
            'patch_generator.py',
            '--modules-dir', str(test_modules_dir),
            '--connections', '1'
        ]

        with patch.object(sys, 'argv', test_args):
            try:
                patch_generator.main()
                captured = capsys.readouterr()
                output = captured.out

                # Should have module names and arrow
                assert "[" in output  # Brackets for ports
                assert "]" in output
                assert "→" in output  # Arrow symbol
            except SystemExit:
                pass
