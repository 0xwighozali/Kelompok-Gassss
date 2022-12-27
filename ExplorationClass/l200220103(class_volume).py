class volume:
    def __init__(self,  r, t, p, l, s):
        self.r = r
        self.t = t
        self.p = p
        self.l = l
        self.t = t
        self.s = s
    
    def v_tabung(self):
        return 3.14*self.r**2*self.t

    def v_balok(self):
        return self.p*self.l*self.t

    def v_kubus(self):
        return self.s**3


volume1 = volume(10, 16, 30, 20, 15)
print ("volume tabung :", volume1.v_tabung())
print ("volume balok :",volume1.v_balok())
print ("volume kubus :",volume1.v_kubus())



