import os
import tempfile
import unittest
from unittest.mock import patch
import storage

class TestCSVStorage(unittest.TestCase):
    def test_create_files_adds_headers(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(storage, "DATA_FOLDER", folder):
                storage.create_files()
                for table, headings in storage.HEADERS.items():
                    path = os.path.join(folder, table + ".csv")
                    self.assertTrue(os.path.isfile(path))
                    with open(path, encoding="utf-8") as file:
                        self.assertEqual(file.readline().strip(), ",".join(headings))

    def test_add_and_read_record(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(storage, "DATA_FOLDER", folder):
                storage.create_files()
                row = {
                    "venue_id": "VEN001",
                    "venue_name": "Test Hall",
                    "location": "Monrovia",
                    "capacity": "100"
                }
                storage.add_record("venues", row)
                result = storage.read_data("venues")
                self.assertEqual(result[0]["venue_name"], "Test Hall")

if __name__ == "__main__":
    unittest.main()
