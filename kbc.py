import random
i = 1
questions = ["Who is the Father of our Nation?", "Who was the first President of India?", "Who is known as Father of Indian Constitution?", "Who was the first Prime Minister of India?", "Who invented Computer?", "Who wrote the National Anthem – Jana Gana Mana?"]
answers = ["Mahatma Gandhi", "Dr. Rajendra Prasad", "Dr. B. R. Ambedkar", "Jawaharlal Nehru", "Charles Babbage", "Rabindra Nath Tagore"]
options=[]
while True:
    quesno=random.randint(0, len(questions) - 1)
    print(f"Question {i} : ")
    i+=1
    print(questions[quesno])
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
    choosen = int(input("Please enter your answer number : "))
    if choosen<=4:
        ans = options[choosen-1]
    else:
        print("Ayoo please choose a number between 1 and 4 only")
    if quesno == ans:
        print("Damn you nailed it!!!")
        print("-"*10)
        print("-"*10)
    else:
        print("Ouch youu lost")
        break
    questions.pop(quesno)
    answers.pop(quesno)
    options.clear()