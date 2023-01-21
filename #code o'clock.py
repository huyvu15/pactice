my_list=[1,2,3,1,2,3,4,1,3,5,6,7,1,3,4,7,8,9,4,6,7,9]
sample_set = set(my_list)

print(sample_set)

my_list2 = [11,22,33,44,55,66,11,33,55]

sample_set2 = set(my_list2)

sample_set3  = list(sample_set2)


sample_set.update(sample_set3)

print(sample_set)

# for  i in sample_set:
        

