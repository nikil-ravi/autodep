"""
Simple sanity tests for lean-interact integration.
Tests basic reflexivity and arithmetic to verify Lean 4 is working.
"""

import pytest
from lean_interact import AutoLeanServer, Command, LeanREPLConfig, TempRequireProject
from lean_interact.interface import LeanError


@pytest.fixture
def lean_server():
    """Create a Lean server for testing."""
    repl_config = LeanREPLConfig(
        project=TempRequireProject(lean_version="v4.8.0", require="mathlib")
    )
    return AutoLeanServer(repl_config)


def test_reflexivity(lean_server):
    """Test basic reflexivity theorem."""
    code = """
theorem refl_test (x : Nat) : x = x := rfl
"""
    result = lean_server.run(Command(cmd=code.strip()), timeout=30)

    assert not isinstance(result, LeanError), f"Lean error: {result.error_message}"
    assert result.lean_code_is_valid(allow_sorry=False), "Code should be valid"


def test_basic_arithmetic(lean_server):
    """Test basic arithmetic theorem."""
    code = """
theorem add_zero (n : Nat) : n + 0 = n := rfl
"""
    result = lean_server.run(Command(cmd=code.strip()), timeout=30)

    assert not isinstance(result, LeanError), f"Lean error: {result.error_message}"
    assert result.lean_code_is_valid(allow_sorry=False), "Code should be valid"
