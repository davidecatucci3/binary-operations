class to_bin:
    def __init__(self, from_base, n=0, prec=32):
        '''
        from_base: number to convert
        n: number of bits in wich youn want you binary number
        prec: in case you convert a fractional number to binary, I need to know the precision 16, 32 or 64 bits
        '''

        self.from_base = from_base
        self.n = n
        self.prec = prec

    @staticmethod
    def add_one(a: str) -> str:
        '''
        add 1 to a binary number 
        '''

        res = ''

        b =  '1'.zfill(len(a))

        carry = '0'

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
        convert decimal part to binary
        '''

        res = ''
        viewed = []

        while x != 0 and x not in viewed:
            viewed.append(x)
       
            x *= 2
            
            x = round(x, 4)

            if x < 1:
                res += '0'
            else:
                res += '1'

                x -= 1
   
        return res
    
    def bit_ext(self, x, type):
        '''
        does a binary extension
        '''

        bit_to_add = self.n - len(x) 

        pre = '1' * bit_to_add if type == 's' else '0' * bit_to_add

        x = pre + x

        return x
    
    def dec_to_bin_unsigned(self, x: str) -> str:
        '''
        convert decimal positive number to binary unsigned 
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
        check if the number is positive or negative,
        to understand if you have to convert it to unsigned (u), signed (s) or fraction (f)
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

        dic = {
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15
        }

        if self.from_base.startswith('0x'):
            self.from_base = self.from_base[2:]

        for i in self.from_base:
            i = i.upper()
        
            if i.isdigit():
                res += self.dec_to_bin_unsigned(i)
            else:
                res += self.dec_to_bin_unsigned(dic[i])
        
        if self.n > len(res):
            res = self.bit_ext(res, 'u')
   
        return res

    def dec_to_bin(self, type='u') -> str:
        '''
        convert dec to bin
        '''

        res = ''

        if type == 'u':
            res = self.dec_to_bin_unsigned(self.from_base)

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
            
            if self.n > len(res):
                res = self.bit_ext(res, type)
        elif type == 'f':
            str_from_base = str(abs(self.from_base))

            int_part, dec_part = str_from_base.split('.')

            # convert integer part anad decimal part to binary
            bin_int_part = to_bin(int(int_part))()
            bin_dec_part = self.dec_part_to_bin(int(dec_part) * pow(10, -len(str(dec_part))))
            
            bin_num = bin_int_part + '.' + bin_dec_part
        
            idx_dot = bin_num.index('.')
   
            bias = {
                16: 5,
                32: 127,
                64: 1023
            }

            len_m = {
                16: 10,
                32: 23,
                64: 55
            }

            # s(ign), e(xponent) and m(antissa)
            s = '1' if self.from_base < 0 else '0'

            e = idx_dot - 1 

            e += bias[self.prec]
            e = to_bin(e)()
          
            m = bin_num[1:]
            m = m.replace('.', '')
       
            # rounding mantissa if exceeded
            if len(m) > len_m[self.prec]:
                m = m[:len_m[self.prec]:]

            # fill with 0's mantissa   
            m = m + ('0' * (len_m[self.prec] - len(m)))

            res += s + e + m
        
        return res

print(to_bin(-5.5182)())
# print(to_bin(0.00000001)())