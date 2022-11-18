#program permainan gunting,batu, paku, dan kertas yang dimainkan oleh dua orang
#kedua pemain melakukan inputan kemudia kondisi pada program akan melakukan perbandingan untuk melihat siapa yang menang


inputan1 = input ("masukkan inputan pertama:")
inputan2 = input ("masukkan inputan kedua:")

#output batu
if inputan1 == "gunting" and  inputan2 == "batu":
    print ("batu")
elif inputan1 == "batu" and  inputan2 == "gunting":
    print ("batu")
elif inputan1 == "paku" and  inputan2 == "batu":
    print ("batu")
elif inputan1 == "batu" and  inputan2 == "paku":
    print ("batu")
    
#output paku    
elif inputan1 == "gunting" and  inputan2 == "paku":
    print ("paku")
elif inputan1 == "paku" and  inputan2 == "gunting":
    print ("paku")
elif inputan1 == "kertas" and  inputan2 == "paku":
    print ("paku")
elif inputan1 == "paku" and  inputan2 == "kertas":
    print ("paku")
    
#output kertas
elif inputan1 == "kertas" and  inputan2 == "batu":
    print ("kertas")
elif inputan1 == "batu" and  inputan2 == "kertas":
    print ("kertas")

#output gunting
elif inputan1 == "kertas" and  inputan2 == "gunting":
    print ("gunting")
elif inputan1 == "gunting" and  inputan2 == "kertas":
    print ("gunting")

#output tambahan
elif inputan1 == inputan2:
    print ("ulangi lagi")
else:
    print("invalid data")
            

