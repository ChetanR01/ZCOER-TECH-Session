
class num:

    def __init__(self,my_int):
        self.input_int=my_int

    def reverse(self):
        inp_to_str=str(self.input_int)
        reverse_str=inp_to_str[::-1]
        return int(reverse_str)
    
a1=num(12345)
print(a1.reverse())
