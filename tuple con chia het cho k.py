# Vẫn còn chưa xong
test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]
K = int(input())    

def test(K, test_list):
    a = list(filter(lambda sub: all(ele % K == 0 for ele in sub), test_list))
    print(a)

# kind 2
# def test(K, test_list):
#     list1 = [tuple for tuple in test_list if all(x % K == 0 for x in tuple)]
#     print(list1)


test(K,  test_list)