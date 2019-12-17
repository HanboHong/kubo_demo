"""
Unit and regression test for the kubo_demo package.
"""

# Import package, test suite, and other packages as needed
import kubo_demo
import pytest
import sys

def test_kubo_demo_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "kubo_demo" in sys.modules
