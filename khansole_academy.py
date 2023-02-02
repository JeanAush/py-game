"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""
#Jean Esther.py

import random
MIN_RANDOM=10 #Minimum random number to be printed.
MAX_RANDOM=99 #maximum random number to be printed.


"""
This program gives a sample of random addition problems  to the user
and the user gives answers to each.
If any answer given by the user is wrong,the correct answer is printed.
"""



def problem():
    num1=random.randint(MIN_RANDOM,MAX_RANDOM)
    num2=random.randint(MIN_RANDOM,MAX_RANDOM)
    answer=(num1)+(num2)
    problem=str("What is "+str(num1)+"+"+str(num2))
    print(problem)
    your_answer=float(input("your answer:"))
    NUM=your_answer==answer
    #if your answer is equal to the expected answer
    if NUM:
        print("Correct! You've gotten 1 correct in a row.")
        #if not equal,the user is told the answer is incorrect and the correct answer is printed.
    else:
        print("Incorrect.The expected answer is "+str(answer))






def main():
    for i in range(5):
        problem()
    print("Congratulations! you've mastered addition.")









    # This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
