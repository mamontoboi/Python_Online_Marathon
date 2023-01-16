# Create function file_parser. If function is called with 2 arguments it must count the number of
# occurrences string in a file, in case of 3 arguments it must replace string in a file to new string
#
# first argument - path to file
#
# second argument - find string
#
# third argument - replace string
#
# Function must returned string with count of occurrences or count of replaced strings
#
# Example:
#
# file_parser("file.txt", 'x', 'o')-> Replaced 8 strings
# file_parser("file.txt", 'o') -> Found 8 strings
# Please, create class ParsesTest and write unittest for file_parser function uses mock object

import re
import unittest
from unittest.mock import patch, mock_open


def file_parser(file_name, *args):
    if len(args) == 1:
        letter = args[0]
        with open(file_name, 'r') as f_name:
            reader = f_name.read()
            return f"Found {reader.count(letter)} strings"

    elif len(args) == 2:
        init_string, replace_string = args
        with open(file_name, 'r') as f_name:
            reader = f_name.read()
            data = re.subn(init_string, replace_string, reader)
        with open(file_name, 'w') as f_name:
            f_name.write(data[0])

        return f"Replaced {data[1]} strings"


class ParserTest(unittest.TestCase):
    def test_open_file_find(self):
        with unittest.mock.patch('builtins.open', unittest.mock.mock_open(read_data="Hello!, world!")) as mocked_file:
            self.assertEqual(file_parser(mocked_file, "o"), 'Found 2 strings')

    def test_file_parser_replace(self):
        with patch('builtins.open', mock_open(read_data="Hello!, world!")) as mocked_file:
            self.assertEqual(file_parser(mocked_file, "o", "b"), 'Replaced 2 strings')


if __name__ == '__main__':
    unittest.main()
