#!/usr/bin/env python3
"""Unit tests for utils module (tasks 0-3)."""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_msg):
        with self.assertRaises(KeyError) as ctx:
            access_nested_map(nested_map, path)
        self.assertEqual(str(ctx.exception), expected_msg)


class TestGetJson(unittest.TestCase):
    """Tests for get_json (mocking requests.get)."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        mock_resp = Mock()
        mock_resp.json.return_value = test_payload
        with patch("utils.requests.get", return_value=mock_resp) as mock_get:
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator."""

    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        obj = TestClass()
        with patch.object(TestClass, "a_method") as mocked:
            mocked.return_value = 42
            # Call twice, should use cached value second time
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            mocked.assert_called_once()
