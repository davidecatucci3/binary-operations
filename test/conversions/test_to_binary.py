import unittest
import sys

sys.path.insert(1, '/Users/davidecatucci3/Documents/Documents - Davide’s MacBook Air/coding/projects/binary operations/src/conversions')

from to_binary import to_bin

class TestConversions(unittest.TestCase):
    def test_hex_to_bin(self):
        # Test single-digit hex values
        self.assertEqual(to_bin('0')(), '0000')
        self.assertEqual(to_bin('1')(), '0001')
        self.assertEqual(to_bin('A')(), '1010')
        self.assertEqual(to_bin('F')(), '1111')

        # Test multi-digit hex values
        self.assertEqual(to_bin('10')(), '00010000')
        self.assertEqual(to_bin('1F')(), '00011111')
        self.assertEqual(to_bin('FF')(), '11111111')

        # Test upper and lower case consistency
        self.assertEqual(to_bin('a')(), '1010')
        self.assertEqual(to_bin('fF')(), '11111111')
        self.assertEqual(to_bin('dead')(), '1101111010101101')

        # Test 3-digit hex values
        self.assertEqual(to_bin('1AB')(), '000110101011')
        self.assertEqual(to_bin('999')(), '100110011001')

        # Test 4-digit hex values
        self.assertEqual(to_bin('ABCD')(), '1010101111001101')
        self.assertEqual(to_bin('FFFF')(), '1111111111111111')

        # Test long hex strings
        self.assertEqual(to_bin('123456789ABCDEF')(), '000100100011010001010110011110001001101010111100110111101111')
        self.assertEqual(to_bin('FFFFFFFFFFFFFFFF')(), '1111111111111111111111111111111111111111111111111111111111111111')

        # Test special hex values
        self.assertEqual(to_bin('00')(), '00000000')
        self.assertEqual(to_bin('0001')(), '0000000000000001')

        # Test small hex values padded with zeros
        self.assertEqual(to_bin('000A')(), '0000000000001010')
        self.assertEqual(to_bin('000F')(), '0000000000001111')

        # Test very large hex values
        self.assertEqual(to_bin('FFFFFFFFFFFFFFFFFFFFFFFF')(), '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')

        # More edge cases
        self.assertEqual(to_bin('8000')(), '1000000000000000')  # Power of 2
        self.assertEqual(to_bin('7FFF')(), '0111111111111111')  # Maximum value in 15 bits

        # Random tests
        self.assertEqual(to_bin('2B')(), '00101011')
        self.assertEqual(to_bin('5C')(), '01011100')
        self.assertEqual(to_bin('9D')(), '10011101')
        self.assertEqual(to_bin('E3')(), '11100011')

        # Additional checks with larger hex strings
        self.assertEqual(to_bin('1234ABCD')(), '00010010001101001010101111001101')
        self.assertEqual(to_bin('ABC123')(), '101010111100000100100011')

        # Ensure that leading zeros are retained
        self.assertEqual(to_bin('0123')(), '0000000100100011')

        # Test negative values (should raise an error for hex input)
        with self.assertRaises(ValueError):
            to_bin('-1')()

        # Validate error handling for non-hex characters
        with self.assertRaises(ValueError):
            to_bin('G')()
        with self.assertRaises(ValueError):
            to_bin('XYZ')()
        with self.assertRaises(ValueError):
            to_bin('1.5')()

        # Valid long hex string
        self.assertEqual(to_bin('FEDCBA9876543210')(), '1111111011011100101110101001100001110110010101000011001000010000')
    
    def test_dec_to_bin(self):
        #! Positive and Negative

        # Test small positive numbers
        self.assertEqual(to_bin(0)(), '0')
        self.assertEqual(to_bin(1)(), '1')
        self.assertEqual(to_bin(2)(), '10')
        self.assertEqual(to_bin(10)(), '1010')
        self.assertEqual(to_bin(255)(), '11111111')

        # Test negative numbers with 8-bit two's complement
        self.assertEqual(to_bin(-1, n=8)(), '11111111')
        self.assertEqual(to_bin(-128, n=8)(), '10000000')
        self.assertEqual(to_bin(127, n=8)(), '01111111')

        # Test multi-bit positive numbers
        self.assertEqual(to_bin(100)(), '1100100')
        self.assertEqual(to_bin(1024)(), '10000000000')
        self.assertEqual(to_bin(999)(), '1111100111')

        # Test negative numbers with 16-bit two's complement
        self.assertEqual(to_bin(-32768, n=16)(), '1000000000000000')
        self.assertEqual(to_bin(32767, n=16)(), '0111111111111111')

        # Test two's complement for larger negative numbers
        self.assertEqual(to_bin(-1024, n=16)(), '1111110000000000')
        self.assertEqual(to_bin(-100, n=8)(), '10011100')

        # Edge cases for large numbers
        self.assertEqual(to_bin(2**31-1)(), '1111111111111111111111111111111')  # Max 32-bit signed integer
        self.assertEqual(to_bin(-2**31, n=32)(), '10000000000000000000000000000000')  # Min 32-bit signed integer

        # Test powers of 2
        self.assertEqual(to_bin(64)(), '1000000')
        self.assertEqual(to_bin(128)(), '10000000')
        self.assertEqual(to_bin(1024)(), '10000000000')

        # Test very large positive numbers
        self.assertEqual(to_bin(2**63-1)(), '111111111111111111111111111111111111111111111111111111111111111')

        # Test more negative numbers
        self.assertEqual(to_bin(-2, n=8)(), '11111110')
        self.assertEqual(to_bin(-255, n=16)(), '1111111100000001')

        # Ensure correct output for powers of 2 minus one
        self.assertEqual(to_bin(15)(), '1111')
        self.assertEqual(to_bin(31)(), '11111')
        self.assertEqual(to_bin(63)(), '111111')

        # Test random small numbers
        self.assertEqual(to_bin(7)(), '111')
        self.assertEqual(to_bin(18)(), '10010')
        self.assertEqual(to_bin(45)(), '101101')

        # Test random large numbers
        self.assertEqual(to_bin(123456)(), '11110001001000000')
        self.assertEqual(to_bin(654321)(), '10011111101111110001')

        # Test two's complement with large negative numbers
        self.assertEqual(to_bin(-999, n=16)(), '1111110000011001')
        self.assertEqual(to_bin(-123456, n=32)(), '11111111111111100001110111000000')

        # Edge case: Zero in two's complement
        self.assertEqual(to_bin(0, n=16)(), '0000000000000000')

        # Test with negative values and different bit sizes
        self.assertEqual(to_bin(-4, n=8)(), '11111100')
        self.assertEqual(to_bin(-1024, n=32)(), '11111111111111111111110000000000')

        #! Fraction
        
        # Small positive floats
        self.assertEqual(to_bin(0.5)(), '00111111000000000000000000000000')
        self.assertEqual(to_bin(0.25)(), '00111110100000000000000000000000')
        self.assertEqual(to_bin(0.125)(), '00111110000000000000000000000000')
        self.assertEqual(to_bin(0.75)(), '00111111010000000000000000000000')

        # Small negative floats
        self.assertEqual(to_bin(-0.5)(), '10111111000000000000000000000000')
        self.assertEqual(to_bin(-0.25)(), '10111110100000000000000000000000')
        self.assertEqual(to_bin(-0.125)(), '10111110000000000000000000000000')
        self.assertEqual(to_bin(-0.75)(), '10111111010000000000000000000000')

        # Larger positive floats
        self.assertEqual(to_bin(3.141592)(), '01000000010010010000111111011000')
        self.assertEqual(to_bin(2.71828)(), '01000000001011011111100001001101')
        self.assertEqual(to_bin(1.5)(), '00111111110000000000000000000000')
        self.assertEqual(to_bin(1.25)(), '00111111101000000000000000000000')

        # Larger negative floats
        self.assertEqual(to_bin(-3.141592)(), '11000000010010010000111111011000')
        self.assertEqual(to_bin(-2.71828)(), '11000000001011011111100001001101')
        self.assertEqual(to_bin(-1.5)(), '10111111110000000000000000000000')
        self.assertEqual(to_bin(-1.25)(), '10111111101000000000000000000000')

        # Special floating-point numbers
        self.assertEqual(to_bin(0.0)(), '00000000000000000000000000000000')  # Positive zero
        self.assertEqual(to_bin(-0.0)(), '10000000000000000000000000000000')  # Negative zero

        # Positive and negative infinities
        self.assertEqual(to_bin('inf')(), '01111111100000000000000000000000')
        self.assertEqual(to_bin('-inf')(), '11111111100000000000000000000000')

        # NaN (Not a Number)
        # self.assertEqual(to_bin(float('nan'))()[:8], '011111111')  # NaN has many representations

        # Positive denormalized numbers (values smaller than 2^-126)
        self.assertEqual(to_bin(1.4e-45)(), '00000000000000000000000000000001')  # Smallest positive denormalized float

        # Negative denormalized numbers
        self.assertEqual(to_bin(-1.4e-45)(), '10000000000000000000000000000001')  # Smallest negative denormalized float

        # Edge cases for denormalized floats
        self.assertEqual(to_bin(1.175494e-38)(), '00000000011111111111111111111111')  # Largest positive denormalized float
        self.assertEqual(to_bin(-1.175494e-38)(), '10000000011111111111111111111111')  # Largest negative denormalized float

        # Random small floats
        self.assertEqual(to_bin(0.15625)(), '00111110001000000000000000000000')
        self.assertEqual(to_bin(-0.15625)(), '10111110001000000000000000000000')

        # Large positive floats
        self.assertEqual(to_bin(1e10)(), '01001110001011011101011111100000')  # 10 billion in IEEE 754
        self.assertEqual(to_bin(3.4e38)(), '01111111011111111111111111111111')  # Largest positive float

        # Large negative floats
        self.assertEqual(to_bin(-1e10)(), '11001110001011011101011111100000')  # -10 billion in IEEE 754
        self.assertEqual(to_bin(-3.4e38)(), '11111111011111111111111111111111')  # Smallest negative float

        # More random floats
        self.assertEqual(to_bin(1.23456)(), '00111111100111100001101011100000')
        self.assertEqual(to_bin(-1.23456)(), '10111111100111100001101011100000')

        # Tests for precision issues (float approximations)
        self.assertEqual(to_bin(0.3333333333333333)(), '00111110101010101010101010101011')  # Closest binary representation of 1/3
        self.assertEqual(to_bin(-0.3333333333333333)(), '10111110101010101010101010101011')  # Closest binary representation of -1/3

        # Very large numbers and edge of precision
        self.assertEqual(to_bin(1.17549435e-38)(), '00000000100000000000000000000000')  # Just normalized
        self.assertEqual(to_bin(-1.17549435e-38)(), '10000000100000000000000000000000')

        # Tests for precision on very small and very large floats
        self.assertEqual(to_bin(5.960464e-8)(), '00110111100000000000000000000000')  # Small number close to zero
        self.assertEqual(to_bin(3.4028235e+38)(), '01111111011111111111111111111111')  # Largest normal float

        # Test random floating numbers
        self.assertEqual(to_bin(12.75)(), '01000001010011000000000000000000')
        self.assertEqual(to_bin(-12.75)(), '11000001010011000000000000000000')

        # Test large negative float
        self.assertEqual(to_bin(-123456.789)(), '11000111111100010010000011101110')

        # Verify two's complement for floating-point with n-bit precision
        self.assertEqual(to_bin(-999.999, n=32)(), '11000100011110111111000100011111')
        
if __name__ == "__main__":
    unittest.main()