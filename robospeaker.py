import os 
if __name__=="__main__":
    pass
    print("Welcome to RoboSpeaker Created by Vivek")
    while True:
        x = input("What you want me to speak? ")
        if x=="q":
            os.system("Say 'bye bye friend'")
            break
        command = f"say {x}"  #f is a self input string 
        os.system(command)