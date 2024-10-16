class to_bin:
    def __init__(self, from_base):
        self.from_base = from_base

    def is_dec(self):
        '''
        check if a number is decimal
        '''
        
        if str(self.from_base).isdigit():
            return True
            
        return False

    def __call__(self):
        '''
        check and convert number

        valid numbers:
            - hex (str)
            - dec (int)
            - custom base

        invalid numbers:
            - bin: not checked the validity, because if you passed 1101 base 2 it will read as 1101 base 10
            - boolearn
            - list
            - ...
        '''
   
        # check if the type of from_base is an int or str
        if isinstance(self.from_base, str):
            res = self.hex_to_bin()

            return res
        elif isinstance(self.from_base, int):
            # check if is not boolean, because True is considered also as int (1)
            if self.is_dec():
                res = self.dec_to_bin()
              
                return res
            else:  
                print('ERROR: Boolean is not valid')

                return False
        else:
            print('ERROR: Invalid value')

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

    def dec_to_bin(self, from_base=None):
        '''
        convert dec to bin
        '''

        # use this method because i need to re-use dec_to_bin() in hex_to_bin()
        if from_base == None:
            from_base = self.from_base

        res = ''

        while from_base > 0:            
            if from_base % 2 == 0:
                res += '0'
            else:
                res += '1'

            from_base //= 2
        
        res = res[::-1]
 
        return res

    def custom_base_to_bin(self):
        '''
        convert custom base to bin
        '''

# hex to bin
x5 = hex(12)
x6 = '0x234D'
x7 = '3FSF'

print(to_bin(x5)())

# dec to bin
x1 = 12
x2 = 1
x3 = 0
x4 = 45

print(to_bin(x1)())

# custom base to  bin
