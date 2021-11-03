import json

if __name__ == '__main__':
    list = []
    f = open("files/businesses.json")
    for l in f.readlines():
        line = json.loads(l)  # dict
        list.append(line)

    print("Enter a category ==>")
    sousuode_category = input()  # Food
    # print(research_cat)

    print("Cutoff for displaying categories => ")
    cutoff = input()
    # print(cutoff)

    count_dict = dict()

    for business in list:  # search_category = Food
        sousuode_category_daquan = business['categories']
        if sousuode_category in sousuode_category_daquan:
            for xianzaide_category in sousuode_category_daquan:
                if xianzaide_category == sousuode_category:
                    suoyoude_biz = count_dict.keys()
                    if xianzaide_category in suoyoude_biz: #出现过了
                        count_dict[xianzaide_category] += 1  # count + 1
                    else: #没出现过
                        count_dict[xianzaide_category] = 1  # 第一次出现在dict 自带出现一次 所以 初始 count 是 1

    print("Categories co-occurring with", sousuode_category)
    isEmpty = True
    for xianzaide_category in count_dict.keys():
        if count_dict[xianzaide_category] > int(cutoff) - 1:
            print(xianzaide_category, ": ", count_dict[xianzaide_category])
            isEmpty = False
    if isEmpty:
        print("None above the cutoff")
