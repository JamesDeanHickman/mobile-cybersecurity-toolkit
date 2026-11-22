
import unittest
import tempfile
from pathlib import Path

from file_integrity import calculate_hash


class TestFileIntegrity(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_file = Path(self.temp_dir.name) / "test.txt"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_identical_files_produce_identical_hashes(self):
        self.test_file.write_text("Cybersecurity testing")
        first_hash = calculate_hash(self.test_file)
        second_hash = calculate_hash(self.test_file)

        self.assertEqual(first_hash, second_hash)

    def test_modified_file_produces_different_hash(self):
        self.test_file.write_text("Original content")
        original_hash = calculate_hash(self.test_file)

        self.test_file.write_text("Modified content")
        modified_hash = calculate_hash(self.test_file)

        self.assertNotEqual(original_hash, modified_hash)

    def test_sha256_digest_has_correct_length(self):
        self.test_file.write_text("Integrity check")
        result = calculate_hash(self.test_file)

        self.assertEqual(len(result), 64)

    def test_missing_file_raises_error(self):
        missing_file = Path(self.temp_dir.name) / "missing.txt"

        with self.assertRaises(FileNotFoundError):
            calculate_hash(missing_file)


if __name__ == "__main__":
    unittest.main()
