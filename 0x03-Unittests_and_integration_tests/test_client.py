#!/usr/bin/env python3
"""Unit and integration tests for client.GithubOrgClient (tasks 4-8)."""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
import fixtures
import utils
import client


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mocked_get_json):
        mocked_get_json.return_value = {"login": org_name}
        gh = client.GithubOrgClient(org_name)
        self.assertEqual(gh.org, {"login": org_name})
        mocked_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        with patch.object(client.GithubOrgClient, "org", new_callable=PropertyMock) as mocked_org:
            mocked_org.return_value = payload
            gh = client.GithubOrgClient("google")
            self.assertEqual(gh._public_repos_url, payload.get("repos_url"))

    @patch("client.get_json")
    def test_public_repos(self, mocked_get_json):
        mocked_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        with patch.object(client.GithubOrgClient, "_public_repos_url", return_value="https://api.github.com/orgs/google/repos") as mocked_url:
            gh = client.GithubOrgClient("google")
            repos = gh.public_repos()
            self.assertEqual(repos, ["repo1", "repo2"])
            mocked_url.assert_called_once()
            mocked_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        gh = client.GithubOrgClient("org")
        self.assertEqual(gh.has_license(repo, license_key), expected)


@parameterized_class(("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
                     [(fixtures.org_payload, fixtures.repos_payload,
                       fixtures.expected_repos, fixtures.apache2_repos)])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos using fixtures."""

    @classmethod
    def setUpClass(cls):
        # Patch utils.requests.get so utils.get_json (used by client) gets fixture data
        def _side_effect(url, *args, **kwargs):
            mock_resp = Mock()
            if url.endswith("/orgs/google"):
                mock_resp.json.return_value = cls.org_payload
            elif url.endswith("/repos") or url.endswith("/orgs/google/repos"):
                mock_resp.json.return_value = cls.repos_payload
            else:
                mock_resp.json.return_value = {}
            return mock_resp

        cls.get_patcher = patch("utils.requests.get", side_effect=_side_effect)
        cls.get_patcher_started = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        gh = client.GithubOrgClient("google")
        self.assertEqual(gh.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        gh = client.GithubOrgClient("google")
        self.assertEqual(gh.public_repos(license_key="apache-2.0"), self.apache2_repos)
