#soal nomor 1
def perhitungan(a, b):
    c = a + b
    d = a - b
    print(c,d)
    return
perhitungan(40,10) 

#soal nomor 2
def response(txt):
  return txt.upper()
response('myskill')

#soal nomor 3
data = int(input("Masukkan Data : "))

if data % 2 == 0 :
  print(data,"Bilangan Genap")
else:
  print(data,"Bilangan Ganjil")

#soal nomor 4
lst=["koala", "kucing", "rubah", "panda", "tupai", "kemalasan", "penguin", "lumba-lumba"]
for x in lst:
  print(x)

#soal nomor 5
a = 1
while(a<10):
  print(a)
  a+=1

#soal nomor 6
i = 9
f= lambda z : z*11
print(f(i))

#soal nomor 7
x = lambda a,b:a*b
print(x(5, 6))

#soal nomor 8
i = 0
while(i<10):
  i+=1
  print(i)
  if(i==3):
    break

#soal nomor 9
for i in range(5):
  print(i)

#soal nomor 10
colors = ['blue','red','green','yellow']
for a in(colors):
  print(colors.index(a),a)