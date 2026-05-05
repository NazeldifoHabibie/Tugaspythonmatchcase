print("While Loop")
Hitungan = 0
while (Hitungan < 9):
  print ("Hitungannya adalah: ", Hitungan)
  Hitungan = Hitungan + 1

print ("Selesai")
print(""".
.
Loop For""")

angka = [1,2,3,4,5]
for x in angka:
  print(x)

buah = ["alpukat", "jambu", "pisang"]
for makanan in buah:
  print ("Saya suka makan", makanan)
  

print(""".
.
Nested Loop""")
i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j = j + 1

    if j > (i / j):
        print(i, "itu hasilnya")

    i = i + 1

print("Good bye!")




