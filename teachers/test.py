import json

if __name__ == '__main__':
    list = []
    f = open("files/businesses.json")
    for l in f.readlines():
        line = json.loads(l)  # line is a dict
        list.append(line)

    print(list[0])
    # sousuode_cate = 'Food'
    #
    # count_dict = dict()
    #
    # for temp_business in list:
    #     temp_cate = temp_business['categories']
    #     if sousuode_cate in temp_cate:
    #         # print(temp_cate)/
    #         for item in temp_cate:
    #             # print(item)
    #             if item in count_dict.keys():
    #                 count_dict[item] += 1
    #             else:
    #                 count_dict[item] = 1
    # # print(count_dict)
    #
    # cut_off = 4
    #
    # for key in count_dict.keys():
    #     if key == sousuode_cate:
    #         continue
    #     if count_dict[key] < cut_off:
    #         continue
    #     print(key, count_dict[key])


