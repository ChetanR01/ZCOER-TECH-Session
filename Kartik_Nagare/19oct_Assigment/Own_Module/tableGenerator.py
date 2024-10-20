class table:   
    def number(self,num):
        self.t_number = num 
        print(f"Your Table of {self.t_number} Created\n")
        for i in range (1,11):
            print(f"{self.t_number} * {i} = {self.t_number*i}")

if __name__ == "__main__": # is add because in main it call object two time
    t1 = table().number(5)