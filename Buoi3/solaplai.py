my_list = input("Nhập danh sách các phần tử ").split()

count_dict = {}
for item in my_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

for key, value in count_dict.items():
    if value > 1:
        print(f"Số {key} xuất hiện {value} lần.")