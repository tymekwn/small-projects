#QuizApp
import random

def operation(filename):                                                        #Opens the file and decides the operation
    op = input("Would you like to write, append to or read a quiz? [w,a,r]")
    read_quiz(op,filename) if op == "r" else add_quiz(op,filename)

def present(all_lines):                                                         #Presents the questions
    questions = int(input("How many questions?"))
    if questions > len(all_lines): questions = len(all_lines)
    else: pass
    for _ in range(questions):
        question,answer = random.choice(list(all_lines.items()))
        user = input(question)
        print("Correct!") if user.lower() == answer.lower() else print("Wrong!")

def read_quiz(op,filename):                                                     #Organises questions into a dictionary
    all_lines = {}
    with open (filename,op) as f:
        fullscript = f.readlines()
        for i in fullscript:
            i = i.replace("\n","").split(",")
            all_lines[i[0]] = i[1]
    present(all_lines)
   
def getnew():                                                                   #Gets new questions and answers
    new = {}
    while True:
        question = input("Input a question, or [STOP] to stop.") 
        if question.upper() == "STOP": return new
        else:
            answer = input("Input an answer to your question.")
            new[question] = answer

def add_quiz(op,filename):                                                      #Writes the new questions and answers to the file
    newlines = getnew()
    with open(filename, op) as f: 
        for question,answer in newlines.items():
            f.write(f"{question},{answer}\n")

def main():                                                                     #Main function
    operation("quiz.txt")
    continue_program = input("Continue general use?[yes/no]")
    return "end" if continue_program.lower() == "no" else main()

if __name__ == "__main__":main()