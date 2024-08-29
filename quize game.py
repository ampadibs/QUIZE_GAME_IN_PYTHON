import time
import os
import pyfiglet
os.system('color b')
test_banner="QUIZ GAME"
text_banner= pyfiglet.figlet_format(test_banner)
print(text_banner)


correct_answers = ["a","a","b"]    
input_answers=[]
 


def game():
    questions=["1: 10*10  ","2: 20+35 ","3: 50+100 "]
    answers = [["a. 100","b. 120","c. 220","d. 300"],["a. 55","b. 60","c. 75","d. 80"],["a. 200","b. 150","c. 300","d. 320"]]
    
    questions_answers(questions,answers,correct_answers)



def questions_answers(questions,answers,correct_answers):
    for i in range(int(len(questions))):
        print("************************************************")
        print("************************************************")
        print("************************************************")
        print(questions[i])
        print("")
        for j in range(int(len(answers[i]))):
            print(answers[i][j])    
        user_answer=input("SELECT THE OPTION : ")
        input_answers.insert(i,user_answer)
        time.sleep(0.5)
        answer_checking(input_answers[i],i)
        time.sleep(0.5)
        print(" \n ")

def answer_checking(input_answers,j):
    for i in range(1):
        if input_answers==correct_answers[j]:
            print("correct answer")
            
            
        else:
            print("wrong answer")
    print("************************************************")
    print("************************************************")
    print("************************************************")


    


game()

