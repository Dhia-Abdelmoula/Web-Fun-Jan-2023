# #-------Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]
# #1
# x[1][0]=15
# print(x)
# #2
# students[0]['last_name']="bryant"
# print(students)
# #3
# sports_directory['soccer'][0]='Andres'
# print(sports_directory)
# #4
# z[0]['y']=30
# print(z)

#-------Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list) :
    for i in range (len(some_list)):
        for j in some_list[i]:
            print(j+' - '+some_list[i][j])
iterateDictionary(students)
#-------Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for i in range (len(some_list)):
        print(some_list[i][key_name])
iterateDictionary2('first_name',students)
#-------Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh','Amy', 'Eduardo', 'Josh'],
#    'instructorsg': ['Michael', 'Amy', 'Eduardo', 'Josh'],
   
}
def printInfo(some_dict):
    for key in dojo :
        print(len(dojo[key]),key)
        for i in range(len(dojo[key])):
            print (dojo[key][i])
printInfo(dojo)




