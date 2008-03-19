import unittest

from pymarc import MARCReader

class Encode(unittest.TestCase):

    def test_encode_decode(self):
        # get raw data from file 
        original = file('test/one.dat').read()
        # create a record object for the file
        reader = MARCReader(file('test/one.dat'))
        record = reader.next()
        # make sure original data is the same as 
        # the record encoded as MARC
        raw = record.as_marc21()
        self.assertEqual(original, raw)

def suite():
    test_suite = unittest.makeSuite(Encode, 'test')
    return test_suite

if __name__ == '__main__':
    unittest.main()
