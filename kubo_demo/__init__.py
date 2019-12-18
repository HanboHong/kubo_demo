"""
kubo_demo
A live demo with Liang group.
"""

# Add imports here
from .kubo import Kubo

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
