import random
import time

def ball(name, question):
    sentences = ["Yes - definitely", "It is decidedly so.","Without a doubt.","Reply hazy, try again.","Ask again later.","Better not tell you now.","My sources say no.","Outlook not so good.", "Very doubtful."]
    random_n = random.randint(0,len(sentences)-1)
    reply = sentences[random_n]
    print("{} asks: {}".format(name, question))
    for i in range(random.randint(0,5)):
        time.sleep(1)
        print(".", end='')
    print("\nMagic Ball's answer: {} \n".format(reply))

while 1:
    name = input("Enter name or 'q' to exit: ")
    if name == 'q':
        break

    question = input("Enter question: ")
    while '?' not in question:
        question = input("Insert a '?' at the end to formulate questions: ")
    ball(name, question)

    
print("Exited sucessfully..!")
