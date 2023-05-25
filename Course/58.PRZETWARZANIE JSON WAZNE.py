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

    
print(get_keys_with_top_values(complitedTaskFrequencyByUser))
        



