x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#1111
x[1][0] = 15
  print(x) 
#222
students[0]['last_name'] = "Bryant"
  print(students) 
#33333
sports_directory['soccer'][0] = 'Andres'
  print( sports_directory['soccer'])  
#444444
z[0]['y'] = 30
  print(z) 
#part2
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterate_dictionary(list):
    for i in range(0, len(list)):
        output = ""
        for key,val in list[i].items():
            output += f" {key} - {val},"
        print(output)
#part3
def iterate_dictionary2(key_name,list):
    for i in range(0, len(list)):
        
        for key,val in list[i].items():
            if key == key_name:
                print(val)

