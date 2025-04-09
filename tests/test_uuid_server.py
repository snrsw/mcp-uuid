#!/usr/bin/env python3
import asyncio
import unittest
import uuid
from unittest.mock import MagicMock

from uuid_server.main import generate_multiple_uuid4, generate_uuid4


class TestUuidServer(unittest.TestCase):
    """Test cases for UUID Server."""

    def setUp(self) -> None:
        """Set up test fixtures."""
        self.ctx = MagicMock()

    def test_generate_uuid4(self) -> None:
        """Test generate_uuid4 function returns a valid UUID4."""
        # Run the coroutine
        result = asyncio.run(generate_uuid4(self.ctx))

        # Check that the result is a string
        self.assertIsInstance(result, str)

        # Check that the result is a valid UUID
        try:
            uuid_obj = uuid.UUID(result)
            self.assertEqual(uuid_obj.version, 4)
        except ValueError:
            self.fail("Result is not a valid UUID")

    def test_generate_multiple_uuid4(self) -> None:
        """Test generate_multiple_uuid4 function returns the correct number of UUIDs."""
        # Test with default count
        result = asyncio.run(generate_multiple_uuid4(self.ctx))
        self.assertEqual(len(result), 1)

        # Test with specific count
        count = 5
        result = asyncio.run(generate_multiple_uuid4(self.ctx, count))
        self.assertEqual(len(result), count)

        # Check that all results are valid UUIDs
        for uuid_str in result:
            self.assertIsInstance(uuid_str, str)
            try:
                uuid_obj = uuid.UUID(uuid_str)
                self.assertEqual(uuid_obj.version, 4)
            except ValueError:
                self.fail(f"Result {uuid_str} is not a valid UUID")

    def test_generate_multiple_uuid4_invalid_count(self) -> None:
        """Test generate_multiple_uuid4 function raises error for invalid count."""
        # Test with count < 1
        with self.assertRaises(ValueError):
            asyncio.run(generate_multiple_uuid4(self.ctx, 0))

        # Test with count > 100
        with self.assertRaises(ValueError):
            asyncio.run(generate_multiple_uuid4(self.ctx, 101))


if __name__ == "__main__":
    unittest.main()
