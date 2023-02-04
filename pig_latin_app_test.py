import unittest
from pig_latin_app import convert
class TestConvert(unittest.TestCase):
    def test_1st_letter_vowel(self):
        self.assertEqual("appleay", convert("apple"))
    def test_no_vowel(self):
    	self.assertEqual("", convert("bbbl"))
    def test_2nd_letter_vowel(self):
    	self.assertEqual("onkeymay", convert("monkey"))
    def test_3rd_letter_vowel(self):
    	self.assertEqual("eepslay", convert("sleep"))
    def test_upper_case(self):
    	self.assertEqual("andicootbay", convert("Bandicoot"))
    def test_special_char(self):
    	self.assertEqual("", convert("pla!ypus"))
    def test_number(self):
    	self.assertEqual("", convert("do1phin"))
    def test_multi_word(self):
    	self.assertEqual("", convert("dolphin dingo"))

    
if __name__=='__main__':
	unittest.main()
    




