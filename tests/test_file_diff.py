import unittest
import os
import difflib

class TestFileDiff(unittest.TestCase):
    def test_file_diff(self):
        # Define file paths
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        expected_file = os.path.join(parent_dir, 'files', 'expected-array.json')
        generated_file = os.path.join(parent_dir, 'files', 'generated_array.json')

        # Read contents of both files
        with open(expected_file, 'r') as f:
            expected_content = f.readlines()
        
        with open(generated_file, 'r') as f:
            generated_content = f.readlines()

        # Compare the contents
        diff = list(difflib.unified_diff(expected_content, generated_content, fromfile='expected-array.json', tofile='generated_array.json'))
        
        # The test passes if there's no diff
        self.assertEqual(len(diff), 0, f"Files have differences:\n{''.join(diff)}")

if __name__ == '__main__':
    unittest.main()