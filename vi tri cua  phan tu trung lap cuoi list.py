# my_tuple = input().split(" ")
# print(my_tuple)

# # print(my_tuple.count("1"))
# # print(my_tuple.index("1"))

# my_tuple1 = list(my_tuple)

# if "30" not in my_tuple1:
#     print("NOT FOUND")
# elif my_tuple1.count("30") ==1:
#     print("FOUND only one time at index: ",my_tuple1.index("30"))
# elif my_tuple1.count("30") >= 2:
#     a = my_tuple1.count("30")
#     print(f"FOUND {a} times")
#     print("The first occurrence is at index: ",my_tuple1.index("30"))
#     # print("And the last occurrence is at index: {0}".format(my_tuple1.rindex("30")))    
        

my_tuple = input().split(" ")
print(tuple(my_tuple))



if "30" not in my_tuple:
    print("NOT FOUND")
elif my_tuple.count("30") ==1:
    print("FOUND only one time at index:",my_tuple.index("30"))
elif my_tuple.count("30") >= 2:
    a = my_tuple.count("30")
    print(f"FOUND {a} times")
    print("The first occurrence is at index:",my_tuple.index("30"))
    my_tuple.reverse()
    print("And the last occurrence is at index:",len(my_tuple)-my_tuple.index("30")-1) 















