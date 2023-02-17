import turkishnlp
import re

tool = turkishnlp.detector.TurkishNLP()

alfabe = """[a,b,c,ç,d,e,f,g,ğ,h,ı,i,j,k,l,m,n,o,ö,p,r,s,ş,t,u,ü,v,y,z
          ,A,B,C,Ç,D,E,F,G,Ğ,H,I,İ,J,K,L,M,N,O,Ö,P,R,S,Ş,T,U,Ü,V,Y,Z]"""


class Turkce():
        
    def seperator(self,sozcuk: str):
        kelimenin_harfleri = re.findall(alfabe, sozcuk)
        harf_sayisi = len(kelimenin_harfleri)

        sorgu1 = self.yabanci_kelime(sozcuk)
        sorgu2 = self.ardisik_unlu(sozcuk)  
        sorgu3 = self.ardisik_unsuz(sozcuk)
        sorgu4 = self.ozel_unluler(sozcuk)

        if(harf_sayisi == 2):

            if(sorgu1 == 1):
                return True
            elif(sorgu1 == 0):
                return False
            else:
                return "Yabancı kelime sorgusunda hata meydana geldi!!!"
        
        elif(harf_sayisi == 3):
            
            if(sorgu1 == 1):
                
                if(sorgu2 == 1):

                    if(sorgu3 == 1):
                        return True
                    elif(sorgu3 == 0):
                        return False
                    else:
                        return "Ardışık ünsüz sorgusunda hata meydana geldi!!!"   

                elif(sorgu2 == 0):
                    return False
                else:
                    return "Ardışık ünlü sorgusunda hata meydana geldi!!!"

            elif(sorgu1 == 0):
                return False
            else:
                return "Yabancı kelime sorgusunda hata meydana geldi!!!"

        else:

            if(sorgu1 == 1):
                
                if(sorgu2 == 1):

                    if(sorgu3 == 1):
                        
                        if(sorgu4 == 1):
                            return True
                        elif(sorgu4 == 0):
                            return False
                        else:
                            return "Özel ünlü sorgusunda hata meydana geldi!!!"

                    elif(sorgu3 == 0):
                        return False
                    else:
                        return "Ardışık ünsüz sorgusunda hata meydana geldi!!!"   

                elif(sorgu2 == 0):
                    return False
                else:
                    return "Ardışık ünlü sorgusunda hata meydana geldi!!!"
                    
            elif(sorgu1 == 0):
                return False
            else:
                return "Yabancı kelime sorgusunda hata meydana geldi!!!"

    def yabanci_kelime(self,sozcuk: str):
        yabanci_harfler = re.search("[q,w,ğ,j,x,Q,W,Ğ,J,X]", sozcuk)

        if yabanci_harfler:
            return 0
        else:
            return 1

    def ardisik_unlu(self,sozcuk: str):
        kelimenin_harfleri = re.findall(alfabe, sozcuk)
        sayi = 0

        for i in kelimenin_harfleri:
            sorgu = re.search("[a,e,ı,i,o,ö,u,ü,A,E,I,İ,O,Ö,U,Ü]", i)

            if sorgu:
                sayi = sayi + 1
            else:
                sayi = 0

            if(sayi == 2):
                break

        if(sayi == 2):
            return 0
        else:
            return 1

    def ardisik_unsuz(self,sozcuk: str):
        sayi = 0
        harfler = re.findall(alfabe, sozcuk)
        hece_harfleri = []
        hece_harfleri.append(harfler[0])
        hece_harfleri.append(harfler[1])

        for i in hece_harfleri:
            sorgu = re.search("[a,e,ı,i,o,ö,u,ü,A,E,I,İ,O,Ö,U,Ü]",i)

            if sorgu:
                sayi = 0
            else:
                sayi = sayi + 1

        if(sayi == 2):
            return 0
        else:
            return 1

    def ozel_unluler(self,sozcuk: str):
        sorgulanan_kelime = tool.syllabicate_sentence(sozcuk)
        harf_sayisi = len(sorgulanan_kelime[0])
        sorgulanacak_hece = []
        sayi = 0
        for i in range(1,harf_sayisi,1):
            sorgulanacak_hece.append(sorgulanan_kelime[0][i])

        for k in sorgulanacak_hece:
            sorgu = re.search("[o,ö,O,Ö]",k)

            if sorgu:
                sayi = 2
            else:
                sayi = 1

            if(sayi == 2):
                break

        if(sayi == 2):
            return 0
        else:
            return 1