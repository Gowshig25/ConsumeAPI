from src.consumeAPI.get_data import get_data_from_API
from src.consumeAPI.post_data import user_input


def MenuTemplate():
    print("----------------------")
    print("   Enter the choices  ")
    print("                       ")
    print("   1. Get The Data     ")
    print("   2. Post the Data    ")
    print("   3. Exist    ")

flag=True

while(flag):
    MenuTemplate()
    choice=int(input())
    if(choice==1):
        get_data_from_API()
    elif(choice==2):
        user_input()
    else:

        flag=False