import numpy as np

lt=[1,2,3,5]
my_array=np.array(lt)
print(my_array)
print(type(my_array))

lt1=[1,2,3,4,5]
lt2=[6,7,8,9,10]
lt3=[11,12,13,14,15]

my_array1=np.array([lt1,lt2,lt3])
print(my_array1)
print(type(my_array1))
print(my_array1.shape)
print(my_array1[2][4])

sum=0
lsty=[]
for ele in my_array1:
    for i in ele:
     if i%2==0:
       lsty.append(i)
print(lsty)


print(lsty[4])