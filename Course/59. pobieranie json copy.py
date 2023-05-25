import requests
import json

'''''''''
{
    1:11
    2:6
    3:15
}




'''''''''

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def count_Task_Frequency(tasks):
    complitedTaskFrequencyByUser = dict()
    for entry in tasks:
        if(entry['completed'] == True):
            try:
                complitedTaskFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                complitedTaskFrequencyByUser[entry["userId"]] = 1
    return complitedTaskFrequencyByUser
#function that search the largest element        
def get_keys_with_top_values(my_dict):
    return [
        key
        for (key,value) in my_dict.items()
        if value == max(my_dict.values())
    ]


def user_with_top_completed_tasks(complitedTaskFrequencyByUser):
    usersIdWithMaxCompletedAmountOftasks = []
    maxAmountOfCompletedTask = max(complitedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTask in complitedTaskFrequencyByUser.items():
        if(numberOfCompletedTask == maxAmountOfCompletedTask):
            usersIdWithMaxCompletedAmountOftasks.append(userId)
    
    return usersIdWithMaxCompletedAmountOftasks

try: 
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print('Niepoprawny format')
else:
    complitedTaskFrequencyByUser = count_Task_Frequency(tasks)
    print(user_with_top_completed_tasks(complitedTaskFrequencyByUser))

    
userWithTopCompletedTasks = get_keys_with_top_values(complitedTaskFrequencyByUser)


r = requests.get("https://jsonplaceholder.typicode.com/todos")

users = r.json()


#sposob 1 taki se

for user in users:
    if(user["id"] in userWithTopCompletedTasks):
        print(user['id'])
        userWithTopCompletedTasks.remove(user['id'])

#sposob 2 
'''''''''
r = requests.get("https://jsonplaceholder.typicode.com/users?id=5")
user = r.json()
for user in user:
    print(user["name"])

r = requests.get("https://jsonplaceholder.typicode.com/users/5")
user = r.json()
print(user["name"])

for userID in userWithTopCompletedTasks:
    r = requests.get("https://jsonplaceholder.typicode.com/users/5"+str(userID))
    user = r.json()
    print(user["name"])
'''''''''
#sposob 3 

userWithTopCompletedTasks = [5,10]

def change_list_into_conj_of_param(my_list,key='id'):
    conj_param = key + '='

    last_iteration = len(my_list)
    i = 0
    for item in my_list:
        i+=1
        if(last_iteration == i):
            conj_param += str(item)
        else: 
            conj_param += str(item) + "&" + key + '='
        
    
    return conj_param

#conj_param = change_list_into_conj_of_param(userWithTopCompletedTasks,'id')
conj_param = change_list_into_conj_of_param([2,7,4])
    
r = requests.get("https://jsonplaceholder.typicode.com/users", params=conj_param) 

users = r.json()

for user in users:
    print(user['name'])
