#!/usr/bin/env python3
"""
Unittests for the client module.

This file contains both unit and integration tests for:
- GithubOrgClient
"""

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized_class

from client import GithubOrgClient
import fixtures


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
                     fixtures.TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient using fixtures."""

    @classmethod
    def setUpClass(cls):
        """Start patcher for requests.get before tests run."""
        cls.get_patcher = patch("requests.get")
        mock_get = cls.get_patcher.start()

        # Mock responses in the order they are called
        mock_get.side_effect = [
            MagicMock(json=lambda: cls.org_payload),
            MagicMock(json=lambda: cls.repos_payload),
        ]

    @classmethod
    def tearDownClass(cls):
        """Stop patcher after tests finish."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos returns the expected repo list."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test filtering repos by license."""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )


if __name__ == "__main__":
    unittest.main()
