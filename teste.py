import unittest
import subprocess

from diskspace import diskspace

class TestClass(unittest.TestCase):

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def test_subprocess_check(self):
        string = 'du -d 1'
        rawstring = diskspace.subprocess_check_output(string)
        self.assertEqual(subprocess.check_output(string.strip().split(' ')),
                         rawstring)

    def test_byte_type(self):
        block = 0
        labeltype = diskspace.bytes_to_readable(block)[-1:]
        self.assertEqual(labeltype, 'B')
