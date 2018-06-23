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
        self.assertIsNotNone(rawstring)

    def test_min_byte_type(self):
        block = 0
        labeltype = diskspace.bytes_to_readable(block)
        self.assertEqual(labeltype[-1:], 'B')
        self.assertEqual(labeltype, '0.00B')

    def test_kbyte_type(self):
        block = 1000
        labeltype = diskspace.bytes_to_readable(block)
        self.assertEqual(labeltype[-2:], 'Kb')

    def test_megabyte_type(self):
        block = 100000
        labeltype = diskspace.bytes_to_readable(block)
        self.assertEqual(labeltype[-2:], 'Mb')

    def test_gibabyte_type(self):
        block = 10000000
        labeltype = diskspace.bytes_to_readable(block)
        self.assertEqual(labeltype[-2:], 'Gb')
