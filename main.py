import os

print("Welcome to Robo Speaker created by Nafi")
while(True):
    x=input("Enter what you want to say ")
    if(x=="Stop"):
        os.system("say 'Bye Bye Friend' ")
        break
    else:
        command=f"say {x}"
        os.system(command)