import unittest
import pandas as pd
import os
from utils.file_operations import save_to_csv

class TestFileOperations(unittest.TestCase):
    def test_save_to_csv(self):
        df = pd.DataFrame({'test': [1, 2, 3]})
        file_path = 'test.csv'
        save_to_csv(df, file_path)
        self.assertTrue(os.path.exists(file_path))
        os.remove(file_path)  # Clean up after test

if __name__ == '__main__':
    unittest.main()
