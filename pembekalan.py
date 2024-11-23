# a = 5 % 3 # 3 * 1 = 3 // 2
# print(a) 

# shorthand if else
# a=2
# b=330
# print('A') if a>b else print('B')

# lemari = ['jam tangan', 'laptop', 'sepatu'] # Jam Tangan, Laptop, Kacamata, Sepatu
# lemari.append('baju')
# lemari.insert(2, 'kacamata')
# lemari.remove('baju')
# popped_list = lemari.pop(1)
# print(popped_list)
# # print(lemari[5])
# print(lemari)

# for i in [1, 'dua', 3]: # 1, 'dua', 3 (Stop)
#     print(i) # 1, 'dua', 3
# print('Selesai') # Selesai
#1
#'dua'
#3
#'selesai

# for a in range(1, 10, 3):
#     print(a)
# print('Sudah Beres')

# for i in range(1,11): # 1, 2, 3
#     for j in range(1,11): # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 / Stop
#         k = i*j 
#         print (k, end=' ') # 3, 6, 9, 12, 15, 18, 21, 24, 27, 30
#     print() # Menambahkan kolom Baru

# a = 0
# while a <= 3:
#     print(a)
#     a += 1

# lemari = ['Baju', 'Celana', 'Topi', 'Jam Tangan']
# lemari.append('Kacamata')
# lemari.insert(3, 'Jaket')
# lemari.remove('Kacamata')
# kotak = lemari.pop(4)
# print(lemari) # Baju, Celana, Topi, Jaket
# print(kotak)

j = 1
while(j<=10): # 1, 2, 3
    k = 1
    while(k<=10): # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        print(j*k, end=" ") # 3, 6, 9, 12, 15, 18, 21, 24, 27, 30
        k+=1
    print()
    j+=1
