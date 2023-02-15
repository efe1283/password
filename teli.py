haneler = int(input("Kaç haneli bir şifre istersiniz: "))
dosya_yolu = input("Dosya yolunu girin: ")

with open(dosya_yolu, "w") as f:
    for i in range(10**(haneler-1), 10**haneler):
        sifre = str(i)
        uygun = True
        for ch in sifre:
            if ch < '1' or ch > '9':
                uygun = False
                break
        if uygun:
            f.write(sifre + "\n")
