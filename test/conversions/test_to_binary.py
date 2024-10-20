import unittest
import random
import sys

sys.path.insert(1, '/Users/davidecatucci3/Documents/Documents - Davide’s MacBook Air/coding/projects/binary operations/src/conversions')

from string import ascii_lowercase, ascii_uppercase, digits
from to_binary import to_bin


def decimal_to_twos_complement(n):
    if n < 0:
        n = (1 << 16) + n  

    return format(n, '017b')

def make_test_dec_to_bin():
    pass

def make_test_hex_to_bin():
    global ascii_lowercase, ascii_uppercase

    ascii_lowercase = ascii_lowercase[:6]
    ascii_uppercase = ascii_uppercase[:6]

    x = list(ascii_lowercase + ascii_uppercase + digits)

    len_hex_number = random.randint(1, 10)

    hex_number = ''.join(random.choices(x, k=len_hex_number))

    return hex_number

def make_test_frac_to_bin():
    pass

class TestConversions(unittest.TestCase):
    def test_dec_to_bin(self):
        for dec_number in range(-101, 101):
            if dec_number >= 0:
                bin_number = bin(dec_number)[2:].zfill(16)
            else:
                bin_number = decimal_to_twos_complement(dec_number)[1:]
         
            self.assertEqual(to_bin(dec_number, n=16)(), bin_number)
    
    '''
    def test_hex_to_bin(self):
        for _ in range(100):
            hex_number = make_test_hex_to_bin()
            bin_number = bin(int(hex_number, 16))[2:]
     
            self.assertEqual(to_bin(hex_number)(), bin_number)
    '''
    '''
    def test_dec_to_IEE754(self):
        self.assertEqual(to_bin(0.15625)(), '00111110001000000000000000000000')
        self.assertEqual(to_bin(-0.15625)(), '10111110001000000000000000000000')
        self.assertEqual(to_bin(3.141592)(), '01000000010010010000111111011011')
        self.assertEqual(to_bin(-3.141592)(), '11000000010010010000111111011011')
    '''

if __name__ == "__main__":
    unittest.main()