import json

if __name__ == '__main__':
    list = []
    f = open("files/businesses.json")
    for l in f.readlines():
        line = json.loads(l)  # dict
        list.append(line)

    # print("Enter a category ==>")
    # sousuode_category = input()  # Food
    # # print(research_cat)
    #
    # print("Cutoff for displaying categories => ")
    # cutoff = input()
    # # print(cutoff)

    count_dict = dict()
    list2 = []
    f = open("files/reviews.json")
    for l in f.readlines():
        line = json.loads(l)  # dict
        list2.append(line)

    temp_search_biz = "Browns Brewing Co.: The Taproom"
    # # print(list[0]['business_id'])
    # # print(list[0]['name'])
    #
    i = 1
    for biz_dict in list:
        temp_name = biz_dict['name']
        if temp_name == temp_search_biz:
            for reviews_dict in list2:
              if biz_dict['business_id'] == reviews_dict['business_id']:
                  print(i)
                  i += 1
                  print(reviews_dict['text'])


