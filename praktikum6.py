# j = 1
# while(j<=10):
#     k = 1
#     while(k<=10):
#         print(j*k, end=" ")
#         k+=1
#     print()
#     j+=1

print()
for i in range(1,11):
    for j in range(1,11):
        k = i*j
        print (k, end=' ')
    print()

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print()