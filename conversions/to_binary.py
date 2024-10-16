class to_bin:
    def __init__(self, from_base):
        self.from_base = from_base

        self.is_valid() # check if from_base is valid

        self.convert() # execute conversion

    def is_valid(self):
        # check if the type of from_base is an int or str
        if isinstance(str, self.from_base) or isinstance(int, self.from_base):
            pass

    def convert(self):
        print(type(self.from_base))

        return 

    def hex_to_bin(self):
        pass

    def dec_to_bin(self):
        pass

    def custom_base_to_bin(self):
        pass

# hex to bin
x1 = '4DG5'
x2 = '0x345D'
x3 = hex(12)

res1 = to_bin(x1)
res2 = to_bin(x2)
res = to_bin(x3)

# dec to bin

# custom base to  bin

# bin to bin