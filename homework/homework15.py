user = {
    "name": 'Yves',
    "age": 30,
    "country": 'Cameroon',
    "fav_lang": 'Python'
}


def print_dict(dictionary):
    print "My name is", dictionary['name']
    print "My age is", dictionary['age']
    print "My country of birth is", dictionary['country']
    print "My favorite language is", dictionary['fav_lang']


print_dict(user)
