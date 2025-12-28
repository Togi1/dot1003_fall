game_list=[]
my_flag=True

while my_flag:
    user_input=input("Please enter an input: ")
    if user_input != "exit":
        game_list.append(user_input)
    else:
        my_flag=False
def anarya(game_list):
    return game_list[::-1]
print(game_list)
print(anarya(game_list))