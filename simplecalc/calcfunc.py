class Calculate:
    
    def __init__(self,a,b):
        if type(int(a))!=int and type(int(b))!=int:
            raise TypeError("Either or both inserted numbers were not an integer")
        self.a=int(a)
        self.b=int(b)
        
        
    
    def add(self):
        s=self.a+self.b
        return s

    def sub(xyz):  
        s=xyz.a-xyz.b
        return s

    def mul(abc):
        m=abc.a*abc.b
        return m

    def div(v):
        d=v.a/v.b
        return d




