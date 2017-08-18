import os
import glob
import unittest

from isatools import isatab

class TestISA(unittest.TestCase):

    datasets = []

    def setUp(self):
        self.datasets = glob.glob("cmso*/isa")

    def tearDown(self):
        pass

    def test_paserISAtab(self):
        for d in self.datasets:
            print("parsing %s" % d)

            with open(os.path.join(os.path.abspath(d), "i_Investigation.txt"), 'r') as input_sampletab:
                ISA = isatab.load(input_sampletab)
                self.assertEqual(len(ISA.studies), 1)


if __name__ == '__main__':
    unittest.main()

