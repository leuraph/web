"""Test permalinks to website."""

import pytest
import os

root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")


@pytest.mark.parametrize("page", [
    "code-of-conduct",
    "fenics17",
    "fenics18",
    "fenics19",
    "fenics-2021",
    # TODO: update this test if permalinks work
    # "google-summer-of-code-2017",
    # "google-summer-of-code-2018",
    "people-of-fenics",
])
def test_permalinks(page):
    """Test that permalink exists."""
    assert os.path.isfile(os.path.join(
        root_dir,
        os.path.join(page, "index.md")))