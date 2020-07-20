class A:
    i = 1
    def foo(self,j:int):
        print ("i = ", j)

class B:
    def __init__(self, a):
        self.a = a
    def test(self):
        self.a.foo(5)
        print (self.a.i)

def main():
    ma = A()
    mb = B(ma)
    mb.test()
	
if __name__ == "__main__":
    main()