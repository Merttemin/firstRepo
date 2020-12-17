class kullanıcı():
    def __init__(self,kullanıcılar = {"mert":"123"},kullanıcı_adı="mert",şifre="123"):
        self.kullanıcı_adı = kullanıcı_adı
        self.şifre = şifre
        self.kullanıcılar = kullanıcılar
    def kayıt(self):
        x = input("kullanıcı adı oluşturunuz:")
        y = input("şifre oluşturunuz:")
        self.kullanıcılar[x] = y
    def giriş(self):
        kullanıcı_adı1 = input("Kullanıcı adınız:")
        şifre1 = input("şifreniz:")  
        if (kullanıcı_adı1 in self.kullanıcılar):
            if (self.kullanıcılar[kullanıcı_adı1] == şifre1):
                print("giriş başarılı")
            else:
                print("giriş başarısız")
        else:
            print("böyle bir kullanıcı adı bulunamadı")
                   
kullanıcı = kullanıcı()

print("""
1. Kayıt = 1

2. Giriş = 2  

3. Çıkış = 3
""")

while True:
    a = input("işlem seçiniz:")
    if (a == "1"):
        kullanıcı.kayıt()
    elif (a == "2"):
        kullanıcı.giriş()
    elif (a == "3"):
        print("çıkılıyor")
        break
    else:
        print("yanlış işlem seçtiniz")
