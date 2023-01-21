# sắp xếp từ điển theo giá trị
list = [{"name": "Hung", "point": 10},
       {"name": "Giang", "point": 10},
       {"name": "Hieu", "point": 9}]

sorted_list = sorted(list, key = lambda x: (x["point"], x["name"]))

print(sorted_list)