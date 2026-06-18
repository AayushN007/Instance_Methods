class demo:
    def __init__(self):
        self.a = 10
        self.b = 20
    def disp(self,x,y):
        z = x + y
        return z
    
dl = demo()
print(dl.a)
print(dl.b)

n1 = 100
n2 = 200

result = dl.disp(n1,n2)
print(result)