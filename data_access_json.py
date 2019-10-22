import json

with open('Datasets/source-data.json') as aj:
    read_content = json.load(aj)

save_data = []

def data_access():

    question_access = read_content['results']
    for question_data in question_access:
        #print(question_data)
        replies_access = question_data['replies']
        for replies_data in replies_access:
            #print(replies_data)
            user_data = replies_data['user']['display_name']
            #print(user_data)
            save_data.append(user_data)

def save_file():
    with open('new_user_name.json', 'w') as file:
        json.dump(save_data, file)

data_access()
save_file()

who = 2
print(save_data[who])
