class bendungan():
    def __init__(self,p,l,t):
        self.p = p
        self.l = l
        self.t = t

    def volume(self):
        return self.p*self.l*self.t 


bendungan1 = bendungan(50, 20, 25)
print ("volume air bendungan1:", bendungan1.volume())
    