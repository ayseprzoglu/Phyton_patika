#Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
#Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.

l= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
n_list=[]

def cevir(a):
    for k in a:
        if isinstance(k,list):
            cevir(k)
        else:
            n_list.append(k)

cevir(l)
print(n_list)


#Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
#Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.

l=[[1, 2], [3, 4], [5, 6, 7]]
n_l=[]
def rvrs(a):
    a=a[::-1]
    for i in a:
        if isinstance(i,list):
            b=i[::-1]
            n_l.append(b)
        else:
            n_l.append(i)
    return n_l
  
cevap=rvrs(l)
print(cevap)
