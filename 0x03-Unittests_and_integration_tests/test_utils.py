#!/usr/bin/env python3
"""
Unittests for the utils module.

This file contains unit tests for:
- access_nested_map
- get_json
- memoize decorator
"""

import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for the access_nested_map function."""

    def test_access_nested_map(self):
        """Test correct access for valid paths."""
        test_cases = [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
        for nested_map, path, expected in test_cases:
            with self.subTest(nested_map=nested_map, path=path):
                self.assertEqual(access_nested_map(nested_map, path), expected)

    def test_access_nested_map_exception(self):
        """Test KeyError is raised for invalid paths."""
        test_cases = [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ]
        for nested_map, path in test_cases:
            with self.subTest(nested_map=nested_map, path=path):
                with self.assertRaises(KeyError):
                    access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Unit tests for the get_json function."""

    @patch("utils.requests.get")
    def test_get_json(self, mock_get):
        """Test get_json returns mocked payload."""
        test_payload = {"payload": True}
        mock_get.return_value.json.return_value = test_payload
        url = "http://example.com"

        result = get_json(url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Unit tests for the memoize decorator."""

    def test_memoize(self):
        """Test that memoize caches result and calls method once."""
        class TestClass:
            """Test helper class for memoize."""

            def a_method(self):
                """Return 42."""
                return 42

            @memoize
            def a_property(self):
                """Return cached result of a_method."""
                return self.a_method()

        obj = TestClass()
        with patch.object(obj, "a_method", return_value=42) as mock_method:
            result1 = obj.a_property
            result2 = obj.a_property

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
        mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
