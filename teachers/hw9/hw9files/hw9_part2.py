'''
Author: Aaron Taylor Email:tayloa5@rpi.edu

    Purpose:This program asks the user for a business, then returns
    reviews. If the business is not found or the business has no reviews,
    it will return a statement stating each.
'''
import json
import textwrap
if __name__ == '__main__':
    r = open('reviews.json')  ##opening the reviews file
    b = open('businesses.json') ##opening the business file
    name = raw_input('Enter a business name => ')
    print name
    
    id_codes = [] ##list of ids for the requested business
    for business in b:  ##searching through the business file
        business = json.loads(business) 
        if name == business['name']:
            id_codes.append(business['business_id'])
    if len(id_codes) == 0 :
        print "This business is not found"
    else:
        all_reviews = [] ##list of reviews for requersted business
        for review in r:  ##searching through the review file
            review = json.loads(review)
            for id_ in id_codes:
                if id_ in review['business_id']:
                    all_reviews.append(review['text'])
        if len(all_reviews) == 0:
            print "No reviews for this business is found"
        else:
            for i in range(len(all_reviews)):
                if len(all_reviews) > 2:  ##taking into an account multiple locations
                    print "Review %s:" %(i+1)
                    string = textwrap.wrap(all_reviews[i],replace_whitespace=False) ##textwrap.wrap returns a list
                    for i in string:
                        print '   '+i
                else:
                    print "Review %s:" %(i+1)
                    string = textwrap.wrap(all_reviews[i],replace_whitespace=False)
                    for i in string:
                        print '   '+i