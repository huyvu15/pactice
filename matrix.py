# matrix
# nhân  ma trận
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# duyệt qua hàng của X
for i in range(len(X)):
    # duyệt qua cột của Y
    for j in range(len(Y[0])):
        # duyệt qua các hàng của Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for r in result:
    print(r)

'''
# cộng 2 ma trận
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

#Duyệt qua từng hàng
for i in range(len(X)):
   #Duyệt qua từng cột
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)
'''

'''
# ma trận chuyển vị:
X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]
# duyệt qua các hàng
for i in range(len(X)):
    # duyệt qua các cột
    for j in range(len(X)):
        result[j][i] = X[i][j]
for i in result:
    print(i)

'''
