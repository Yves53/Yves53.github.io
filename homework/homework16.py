students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for i in students:
    for k, v in i.iteritems():
        print v,
    print ''

print '\nPART II\n'

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
count = 1
letter = 0
for e in users:
    print e
    for j in range(1):
        for h in users[e]:
            print count, "-",
            for b in h.values():
                letter += len(b)
                print b, '-',
            print letter, ''
            letter = 0
            count += 1
    print ''
    count = 1


