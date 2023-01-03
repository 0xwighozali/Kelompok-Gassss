class Tabung(object):
    
    def _init_(self, jejari, tinggi):
        self.r = jejari
        self.t = tinggi
        
    def luas_alas(self):
        L = 3.14*self.r ** 2
        return L
    
    def Luas_selimut(self):
        S = 2 * 314 * self.r*self.t
        
    def volume(self):
        V = 3.14 * self.r ** 2 * self.t
        
j = Tabung(5, 8)
print(j.luas_alas)
print(j.t)

class Balok(object):
    
    def _init_(self, panjang, lebar, tinggi):
        self.p = panjang
        self.l = lebar
        self.t = tinggi
        
    def luas_alas(self):
        L = self.p * self.l
        return L
    
    def Luas_selimut(self):
        S = 2 * (self.p * self.l + self.l * self.t + self.t * self.p)
        
    def volume(self):
        V = self.p * self.l * self.t
        
B = Balok(5, 8)
print(B.luas_alas)

class Kubus(object):
    
    def _init_(self, sisi):
        self.s = sisi
        
    def luas_alas(self):
        L = self.s * self.s
        return L
    
    def Luas_selimut(self):
        S = 6 * self.s ** 2
        
    def volume(self):
        V = self.s ** 3
        
K = Kubus(5)
print(K.luas_alas)

class Bola(object):
    
    def _init_(self, jejari):
        self.r = jejari
        
    
    def Luas_selimut(self):
        S = 4 * 3.14 * self.r ** 2
        
    def volume(self):
        V = 3/4 * 3.14 * self.r ** 3
        
Bo = Bola(5)
print(Bo.volume)


class jajargenjang(object):
    
    def _init_(self, alas,tinggi,):
        self.a = alas
        self.t = tinggi
    
    def luas_jajargenjang(self):
        L = self.a * self.t
        return L
jg = jajargenjang(5)
print(jg.luas_jajargenjang)
    

class Trapesium(object):
    
    def _init_(self,sisi,tinggi,):
        self.s = sisi
        self.t = tinggi
    
    def luas_Trapesium(self):
        L =0.5*(self.s + self.s) * self.t
        return L
T = Trapesium(5)
print(T.luas_Trapesium)
    


