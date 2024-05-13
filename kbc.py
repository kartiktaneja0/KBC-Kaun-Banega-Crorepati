# Create a program capable of displaying questions to the user like KBC. 
# Use List data type to store the questions and their correct answers. 
# Display the final amount the person is taking home after playing the game.

import random
i = 1
questions = ["Who is the Father of our Nation?", "Who was the first President of India?", "Who is known as Father of Indian Constitution?", "Who was the first Prime Minister of India?", "Who invented Computer?", "Who wrote the National Anthem – Jana Gana Mana?"]
answers = ["Mahatma Gandhi", "Dr. Rajendra Prasad", "Dr. B. R. Ambedkar", "Jawaharlal Nehru", "Charles Babbage", "Rabindra Nath Tagore"]
correct_ans = 0
prize_amount = 0
options=[]
prize_amounts = [5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,500000000]
while True:
    quesno=random.randint(0, len(questions) - 1)
    print("-"*10)
    print(f"Question {i} : ")
    i+=1
    print(questions[quesno])
    print("-"*10)
    while True:
        option = random.randint(0, len(answers)-1)
        if option in options or option==quesno:
            continue
        else:
            options.append(option)
        if len(options)==3:
            break
    options.insert(random.randint(0,3), quesno)
    print("1. ", answers[options[0]])
    print("2. ", answers[options[1]])
    print("3. ", answers[options[2]])
    print("4. ", answers[options[3]])
    print("'Type 5 to use lifelines'")
    choosen = int(input("Please enter your answer number : "))
    print("-"*10)
    if 1<=choosen<=4:
        ans = options[choosen-1]
    if choosen==5:
        print("""-----LIFELINE MENU-------""")
        print("1. 50-50")
        life=int(input("Please enter the lifeline you want to use: "))
        if life==1:
            ab=0
            while True:
                popp = options[random.randint(0,3-ab)]
                if popp == quesno:
                    continue
                else:
                    options.remove(popp)
                    ab+=1
                if len(options)==2:
                    break
            print(questions[quesno])
            print("-"*10)
            print("1. ", answers[options[0]])
            print("2. ", answers[options[1]])
            choosen = int(input("Please enter your answer number : "))
            print("-"*10)
            ans = options[choosen-1]            
    else:
        print("Ayoo please choose a number between 1 and 4 only")

    if quesno == ans:
        print("Damn you nailed it!!!")
        correct_ans+=1
        prize_amount = prize_amounts[correct_ans-1]
        print(f"Congratulations! You won {prize_amount} INR")
    else:
        print("Ouch youu lost")
        prize_amount = prize_amounts[correct_ans-1]
        print(f"Dont't worry! You will still take {prize_amount} INR with yourself")
        print("-"*10)
        break
    questions.pop(quesno)
    answers.pop(quesno)
    options.clear()