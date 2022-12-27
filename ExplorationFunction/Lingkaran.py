import xlwt

class Lingkaran(object):
    pi = 3.14
    def __init__(self,jarijari):
        self.r = jarijari

    def keliling(self):
        K = 2 * self.pi * self.r
        return K

    def luas(self):
        L = self.pi * self.r ** 2
        return L

ling1 = Lingkaran(4)
print("Jari-jari lingkaran:", ling1.r)

K = ling1.keliling()
L = ling1.luas()
print("Keliling lingkaran:", K)
print("Luas lingkaran:", L)



