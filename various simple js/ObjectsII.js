var users = {
    'Students': [
        {first_name: 'Michael', last_name: 'Jordan'},
        {first_name: 'John', last_name: 'Rosales'},
        {first_name: 'Mark', last_name: 'Guillen'},
        {first_name: 'KB', last_name: 'Tonel'}
    ],
    'Instructors': [
        {first_name: 'Michael', last_name: 'Choi'},
        {first_name: 'Martin', last_name: 'Puryear'}
    ]
};

for (var name in users) {
    console.log(name);
    var i = 0;
            for (i = 0; i < users[name].length; i++) {
                console.log((i + 1) + " - " + users[name][i].first_name + " " + users[name][i].last_name +
                    " - " + (users[name][i].first_name.length + users[name][i].last_name.length));
    }
}


