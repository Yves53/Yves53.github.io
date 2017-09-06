def type_checker(val):
    if type(val) == int:
        if val < 100:
            print "That's a small number"
        else:
            print "That's a big number"
    elif type(val) == str:
        if len(val) < 50:
            print "Short sentence"
        else:
            print "Long sentence"
    elif type(val) == list:
        if len(val) < 10:
            print "Short list"
        else:
            print "Big list"
    else:
        print "I wasn't coded to deal with this type!"


type_checker("Rubber baby buggy bumpers")

