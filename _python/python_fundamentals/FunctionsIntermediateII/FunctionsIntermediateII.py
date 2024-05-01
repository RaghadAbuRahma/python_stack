# x = [ [5,2,3], [15,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Bryant'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Andres', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 30} ]


# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(students):
#     for x in range(0, 4, 1):
#         print(students[x].items())

# iterateDictionary(students)


# def iterateDictionary2(key, list):
#     for value in list :
#         print(value[key])

# iterateDictionary2('last_name', students)

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):

    for key in dict.keys():
        print(str(len(dict[key])) + " " + key.upper())
        for item in dict[key]:
            print(item)
        print("\n")
printInfo(dojo)




    








