class to_bin:
    def __init__(self, from_base, n=0, prec=32):
        '''
        from_base: number to convert
        n: number of bits in wich youn want your binary number
        prec: in case you wan to convert a fractional number, the IEEE 754 has 3 formats (16, 32 or 64) bits
        '''

        self.from_base = from_base
        self.n = n
        self.prec = prec

    @staticmethod
    def add_one(a: str) -> str:
        '''
        add 1 to a binary number 

        a: binary number
        '''

        res = ''

        b =  '1'.zfill(len(a)) # binary number 1

        carry = '0' # carried bit during sum

        for i, j in zip(a[::-1], b[::-1]):
            if i == '1' and j == '1' and carry == '0':
                res += '0'

                carry = '1'
            elif i == '1' and j == '1' and carry == '1':
                res += '1'

                carry = '1'
            elif ((i == '1' and j == '0') or (i == '0' and j == '1')) and carry == '0':
                res += '1'
            elif ((i == '1' and j == '0') or (i == '0' and j == '1')) and carry == '1':
                res += '0'

                carry = '1'
            elif i == '0' and j == '0':
                res += carry

                carry = '0'
  
        res = res[::-1]

        return res
    
    @ staticmethod
    def dec_part_to_bin(x: int):
        ''''
        convert decimal part to binary (first method that doesn't work for very small numbers)

        x: decimal number 
        '''

        res = ''
        viewed = [] # list of numbers already seen, used to understand when there is a cycle 

        while x != 0 and x not in viewed:
            viewed.append(x)
       
            x *= 2

            if x < 1:
                res += '0'
            else:
                res += '1'

                x -= 1

        return res

    def dec_part_to_bin_2(self, x: int):
        ''''
        convert decimal part to binary (second method that work for very small numbers)

        x: decimal number
        '''

        res = ''

        close_x = 0 # number that has to be as close as possible to x
        count_ones = 0

        len_m = {
            16: 10,
            32: 23,
            64: 55
        }
        
        prec_m = len_m[self.prec] # precison of mantissa, for very small fractions like 0.000002341, until when calculate bits

        i = 1
        
        while count_ones < prec_m:
            power = pow(2, -i)
    
            if power + close_x < x:
                res += '1'

                close_x += power

                count_ones += 1
            elif power + close_x > x:
                res += '0'
            else:
                return '1'
        
            i += 1
 
        return res
    
    def bit_ext(self, x: str, type: str):
        '''
        does a binary extension

        x: binary number
        type: s(igned) or u(nsigned)
        '''

        bit_to_ext = self.n - len(x) 

        pre = '1' * bit_to_ext if type == 's' else '0' * bit_to_ext

        x = pre + x

        return x
    
    def dec_to_bin_unsigned(self, x: str) -> str:
        '''
        convert decimal positive number to binary unsigned 

        x: decimal number
        '''

        if x == 0:
            return '0'
        
        res = ''

        while x > 0:            
            if x % 2 == 0:
                res += '0'
            else:
                res += '1'

            x //= 2
            
        res = res[::-1]

        return res

    def check_type(self) -> str:
        '''
        check if the number is positive, negative or float, to understand if you have to
        convert it to unsigned (u), signed (s) or fraction (f)
        '''

        type = ''

        if isinstance(self.from_base, int):
            if self.from_base < 0:
                type = 's'
            else:
                type = 'u'
        else:
            type = 'f'

        return type

    def __call__(self):
        '''
        check if the number is valid and convert it

        valid numbers:
            - hex (str)
            - dec (int)

        invalid numbers:
            - bin (if you passed 1101 it will read as 1101 base 10)
            - boolean
            - list
            - ...
        '''
   
        # check if the number is valid
        if isinstance(self.from_base, str):
            res = self.hex_to_bin()

            return res
        elif isinstance(self.from_base, int) or isinstance(self.from_base, float):
            # check if is not boolean, because True is considered also as int (1)
            if not isinstance(self.from_base, bool):
                type = self.check_type()

                res = self.dec_to_bin(type)
              
                return res
            else:  
                print('ERROR: Boolean is not valid')

                return False
        else:
            print('ERROR: Invalid number')

            return False

    def hex_to_bin(self) -> str:
        '''
        convert hex to bin
        '''

        res = ''

        # correspnding decimal of hex number
        dic = {
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15
        }

        # remove 0x prefix that can be before a hex number
        if self.from_base.startswith('0x'):
            self.from_base = self.from_base[2:]

        for i in self.from_base:
            i = i.upper()
        
            if i.isdigit():
                res += self.dec_to_bin_unsigned(i)
            else:
                res += self.dec_to_bin_unsigned(dic[i])
        
        # does bit extension if lenght extended number is greater then actual number
        if self.n > len(res):
            res = self.bit_ext(res, 'u')
   
        return res

    def dec_to_bin(self, type='u') -> str:
        '''
        convert dec to bin

        type: u(nsigned), s(igned) or f(raction)
        '''

        res = ''

        if type == 'u':
            res = self.dec_to_bin_unsigned(self.from_base)

            # does bit extension if lenght extended number is greater then actual number
            if self.n > len(res):
                res = self.bit_ext(res, 'u')
        elif type == 's':
            abs_val = abs(self.from_base)
     
            res = self.dec_to_bin_unsigned(abs_val)
        
            l_res = list(res)

            res = ''.join(['0' if i == '1' else '1' for i in l_res])

            res = self.add_one(res)

            if res[0] == '0':
                res = '1' + res
            
            # does bit extension if lenght extended number is greater then actual number
            if self.n > len(res):
                res = self.bit_ext(res, type)
        elif type == 'f':
            str_from_base = str(abs(self.from_base))
            
            # if number is too small or too big
            if 'e' in str_from_base:
                idx_e = str_from_base.index('e')

                str_exp = str_from_base[idx_e + 1:]
                
                if str_exp[0] == '-':
                    if '.' not in str_from_base:
                        str_from_base = format(self.from_base, f'.{int(str_from_base[idx_e + 2:])}f')
                    else:
                        idx_point = str_from_base.index('.')

                        x = len(str_from_base[idx_point + 1:idx_e])
            
                        str_from_base = format(self.from_base, f'.{int(str_from_base[idx_e + 2:]) + x}f')
                else:
                    str_from_base = format(self.from_base, '.0f')
         
            int_part, dec_part = str_from_base.split('.')

            len_e = {
                16: 5,
                32: 8,
                64: 11
            }

            len_m = {
                16: 10,
                32: 23,
                64: 55
            }

            # check special cases
            if int(int_part) == 0 and int(dec_part) == 0:
                s = '0'
                e = '0' * len_e[self.prec]
                m = '0' * len_m[self.prec]
            else:
                # convert integer part and decimal part to binary
                bin_int_part = to_bin(int(int_part))()
             
                if int(int_part) >= 1:
                    bin_dec_part = self.dec_part_to_bin(float(dec_part) * pow(10, -len(str(dec_part))))
                else:
                    bin_dec_part = self.dec_part_to_bin_2(float(dec_part) * pow(10, -len(str(dec_part))))
           
                bin_num = bin_int_part + '.' + bin_dec_part
                print(bin_num)
                if bin_num[0] == '1':
                    idx_dot = bin_num.index('.')

                    moves = idx_dot - 1

                    shifted_bin_num = bin_num[0] + '.' +  bin_num[2:]
                else:
                    idx_dot = bin_num.index('.')
                    idx_one = bin_num.index('1')

                    moves = idx_one - idx_dot
             
                    shifted_bin_num = bin_num[moves + 1] + '.' +  bin_num[moves + 2:]

                    moves = -moves

                print(shifted_bin_num)
                bias = {
                    16: 5,
                    32: 127,
                    64: 1023
                }

                # s(ign), e(xponent) and m(antissa)
                s = '1' if self.from_base < 0 else '0'
            
                e = moves
                e += bias[self.prec]
                e = to_bin(e)()

                if len(e) < len_e[self.prec]:
                    bit_to_add = len_e[self.prec] - len(e)

                    e = '0' * bit_to_add + e
                elif len(e) > len_e[self.prec]:
                    print('ERROR: Exponent too large')

                    return False
            
                m = shifted_bin_num[2:]
        
                # truncate mantissa if exceeded (is not rounding)
                if len(m) > len_m[self.prec]:
                    m = m[:len_m[self.prec]:]
            
                # fill with 0's the mantissa   
                m = m + ('0' * (len_m[self.prec] - len(m)))

            res += s + '|' + e + '|' + m
        
        return res

print(to_bin(0.0000000000000001)())

'''
!PROBLEMS!

- rounding or truncate?
- precison of mantissa for small number
- +inf, -inf and NaN
'''