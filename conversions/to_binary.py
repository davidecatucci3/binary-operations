class to_bin:
    def __init__(self, from_base):
        '''
        from_base: number to convert
        '''

        self.from_base = from_base

    @staticmethod
    def add_one(a, b):
        '''
        add 1 to a binary number 
        '''

        res = ''

        b =  b.zfill(len(a))

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
    
    @staticmethod
    def dec_to_bin_unsigned(x):
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

    def check_type(self):
        '''
        check if the number is positive or negative,
        to understand if you have to convert it to unsigned (u) or signed (s)
        '''

        type = ''

        if self.from_base < 0:
            type = 's'
        else:
            type = 'u'

        return type

    def is_dec(self):
        '''
        check if a number is decimal
        '''
        
        if str(abs(self.from_base)).isdigit():
            return True
            
        return False

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
        elif isinstance(self.from_base, int):
            # check if is not boolean, because True is considered also as int (1)
            if self.is_dec():
                type = self.check_type()

                res = self.dec_to_bin(type)
              
                return res
            else:  
                print('ERROR: Boolean is not valid')

                return False
        elif isinstance(self.from_base, float):
            pass
        else:
            print('ERROR: Invalid number')

            return False

    def hex_to_bin(self):
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
                res += self.dec_to_bin(i)
            else:
                res += self.dec_to_bin(dic[i])
   
        return res

    def dec_to_bin(self, type='u', from_base=None):
        '''
        convert dec to bin
        '''

        res = ''

        # use this method because i need to re-use dec_to_bin() in hex_to_bin()
        if from_base == None:
            from_base = self.from_base
        
        if from_base == 0:
            return '0'

        if type == 'u':
            res = self.dec_to_bin_unsigned(self.from_base)
        elif type == 's':
            abs_val = abs(self.from_base)
     
            res = self.dec_to_bin_unsigned(abs_val)
        
            l_res = list(res)

            res = ''.join(['0' if i == '1' else '1' for i in l_res])

            res = self.add_one(res, '1')

            if res[0] == '0':
                res = '1' + res
         
        return res
