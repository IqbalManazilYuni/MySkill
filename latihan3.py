#soal nomor 1
jumlah_ayam = 10
print(jumlah_ayam)

#soal nomor 2
new = str(jumlah_ayam)
print(new)
print(type(new))

#soal nomor 3
new2 = float(new)
print(new2)
print(type(new2))

#soal nomor 4
color_list = ["Red","Green","White" ,"Black"]
x = color_list[0]
y = color_list[3]
print(x,y)

#soal nomor 5
# membuat list
lst = [11, 5, 17, 18, 23, 50]
lst.sort(reverse=True)
print(lst)

#soal nomor 6
lst = [11, 5, 17, 18, 23, 50]
del lst[1:5]
print(lst)

#soal nomor 7
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
from collections import Counter as ct
new = ct(d1) + ct(d2)
print(new)

#soal nomor 8
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}

d3 = dict()
d3.update(d1)
d3.update(d2)
print(d3)

#soal nomor 9
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection(set2)

#soal nomor 10
tuple1 = (10, 20, 30, 40, 50)
hasil = reversed(tuple1)
hasil = tuple(hasil)
print(hasil)