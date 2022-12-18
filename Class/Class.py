import xlwt

class jajarGenjang(object):
    def __init__(self, alas, sisi, tinggi):
        self.a = alas
        self.s = sisi
        self.t = tinggi

    def keliling(self):
        K = 2 * (self.a + self.s)
        return K

    def luas(self):
        L = self.a * self.t
        return L
    
genjang1 = jajarGenjang(6, 8, 4)


K = genjang1.keliling()
L = genjang1.luas()

print('Keliling Jajar Genjang : ', K)
print ('Luas Jajar Genjang : ', L)
    
