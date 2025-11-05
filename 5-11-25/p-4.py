# 1D,2D AND 3D LISTS
#1D LIST
one_d_list = [1, 2, 3, 4, 5]
print("1D List:", one_d_list)
#2D LIST
two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("2D List:")
for row in two_d_list:
    print(row)
#3D LIST
three_d_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("3D List:")
for matrix in three_d_list:
    for row in matrix:
        print(row)