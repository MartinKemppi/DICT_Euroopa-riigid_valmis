from OmaMoodul import *

sõnastik={}
while True:
    menu=input("\n0-välju\n1-loeme failist \n2-Salvestame failisse \n3-Tekst helisse\n4-Vaata sõnastiku\n5-Näita riigi ja tema pealinna\n6-Paranda viga sõnastikus\n7-Test\n")
    if menu=="0":
        break
    if menu=="1":
        sõnastik=Loe_failist("riigid_pealinnad.txt")
    elif menu=="2":
        Kirjuta_failisse("riigid_pealinnad.txt")
    elif menu=="3":
        print()
    elif menu=="4":
        vaata_sõnastiku("riigid_pealinnad.txt")
    elif menu=="5":
        riik_ja_pealinn_näita("riigid_pealinnad.txt")
    elif menu=="6":
        paranda("riigid_pealinnad.txt")
    elif menu=="7":
        test("riigid_pealinnad.txt")
        
