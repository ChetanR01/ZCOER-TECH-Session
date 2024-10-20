class reverse:
    def __init__(self, num):
        self.num =num
    def __reverse__(self):
        str1=str(self.num)
        reverse_num=str1[::-1]
        print(int(reverse_num))