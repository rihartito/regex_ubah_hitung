'''
buatlah sebuah fungsi untuk mengubah "#" menjadi persebaya dan hitunglah
ada berapa "#" yang muncul di kalimat tersebut berdasarkan inputan user



Input: Kalimat = inputan user kalimat

Proses:
import re
membuat fungsi
melakukan re.sub # persebaya
melaukan loop re.findall # 

Output:
menampilkan perubahan # menjadi persebaya
menghitung # yang ad pada kalimat 
'''
import re

def ngubah(kalimat):
    kata = re.sub("#","Persebaya",kalimat)
    jumlah = 0
    for i in re.findall("#",kalimat):
        jumlah += 1
    print("Hasilnya adalah :",kata)
    print("Jumlah # pada kalimat tersebut adalah :",jumlah)

kalimat = str(input("Masukkan kalimat: "))
ngubah(kalimat)





