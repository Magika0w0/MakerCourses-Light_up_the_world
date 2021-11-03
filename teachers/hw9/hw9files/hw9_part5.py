import json

if __name__ == '__main__':
    f = open('businesses.json') ##list of dictionaries
    input_ = raw_input("Enter a category ==> ")  ##asking for the user input category
    print input_
    cutoff = raw_input("Cutoff for displaying categories => ")  ##asking for user input cutoff number
    print cutoff
    
    cats = [] ##list of categories associated with the input
    for business in f:  ##searching throught the business file
        business = json.loads(business)  ##turns a line in the business file into a dictionary
        if input_ in business['categories']:  ##if the user input is found in the business's category list,the category list will be added to the list 'cats'
            cats.append(business['categories'])
    if len(cats) == 0:
        print "Searched category is not found"
    else:
        counts = {}  ##dictionary consisting of number of category names as keys and appearences as values
        for catlist in cats:  ##looping through cats
            for category in catlist:  ##looping through every category list in cats
                if input_ != category:  ##taking out every appearance of the input because its not a co-occurence
                    counts[category] = 0  ##creating a list consisting of [category name,count number]
       
        for key in counts:     ##increasing a categories' count for each time it appears
            for business in cats:
                if key in business: 
                    counts[key] += 1
        print "Categories co-occurring with",input_+":"
        a = False  ##boolean for when no categories' counts are above the cutoff
        for key in sorted(counts):  ##printing the counts above the cutoff
            if counts[key] >= int(cutoff):
                string = key+":"
                print string.rjust(30),counts[key]
                a = True
        if a == False:
            print "None above the cutoff"