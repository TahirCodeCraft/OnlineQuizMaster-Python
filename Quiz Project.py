# quiz program
import time
# making function
def general_test():
        score = 0
        start_time = time.time()

    # question 1
        question_1 = (input("\n1) What is the capital of canada?\na) Canberra\nb) Berlin\nc) Ottawa\nAns : ").lower())
        option = { 1:'Canberra', 2:'Berlin', 3:'Ottawa'}
        if question_1 == 'c' or question_1 == 'ottawa':
            print("Your answer is correct!")
            score += 1
        else:
            print(f"Your answer is incorrect! The correct answer is {option[3]}.")

    # question 2
        question_2 = (input("\n2) Which animal do not make any sound?\na) Starfish\nb) Turtle\nc) Zebra\nAns : ").lower())
        option = { 1:'Starfish', 2:'Turtle', 3:'Zebra'}
        if question_2 == 'a' or question_2 == 'starfish':
            print("Your answer is correct!")
            score += 1
        else:
            print(f"Your answer is incorrect! The correct answer is {option[1]}.")

    # question 3
        question_3 = (input("\n3) Which is the world's largest flower?\na) Rafflesia\nb) Sun flower\nc) Rose\nAns : ").lower())
        option = { 1:'Rafflesia', 2:'Sun flower', 3:'Rose'}
        if question_3 == 'a' or question_3 == 'rafflesia':
            print("your answer is correct!")
            score += 1
        else:
            print(f"Your answer is incorrect! The correct answer is {option[1]}.")

    # question 4
        question_4 = (input("\n4) Urdu was declared national language of Pakistan in:\na) April 1950\nb) April 1955\nc) April 1954\nAns : ").lower())
        option = { 1:'April 1950', 2:'April 1955', 3:'April 1954'}
        if question_4 == 'c' or question_4 == 'april 1954':
            print("your answer is correct!")
            score += 1
        else:
            print(f"Your answer is incorrect! The correct answer is {option[3]}.")

    # question 5
        question_5 = (input("\n5) How many letters are there in Urdu alphabets:\na) 37\nb) 36\nc) 35\nAns : ").lower())
        option = { 1:'37', 2:'36', 3:'35'}
        if question_5 == 'a' or question_5 == '37':
            print("your answer is correct!")
            score += 1
        else:
            print(f"Your answer is incorrect! The correct answer is {option[1]}.")

    # set timer
        end_time = time.time()
        total = end_time - start_time
        if total <= 50:
                print(f"You got {score} score out of 5")
        else:
                print("Sorry! your time is over")

# making function
def islamic():
        score = 0
        start_time = time.time()

    # question 1
        question_1 = (input("\n1) The term “Islam” means?\na) Submission\nb) Peace\nc) Thankfulness\nAns : ").lower())
        option = { 1:'Submission', 2:'Peace', 3:'Thankfulness'}
        if question_1 == 'a' or question_1 == 'submission':
            print("your answer is correct!")
            score += 1
        else:
            print(f"Your answer is incorrect! The correct answer is {option[1]}.")

    # question 2
        question_2 = (input("\n2) How many Ambiyaa are mentioned in the Qur’aan?\na) 50\nb) 15\nc) 25\nAns : ").lower())
        option = { 1:'50', 2:'15', 3:'25'}
        if question_2 == 'c' or question_2 == '25':
            print("your answer is correct!")
            score += 1
        else:
            print(f"Your answer is incorrect! The correct answer is {option[3]}.")

    # question 3
        question_3 = (input("\n3) What is the first month of the Islamic calendar?\na) Rajjab\nb) Ramadhan\nc) Muharram\nAns : ").lower())
        option = { 1:'Rajjab', 2:'Ramadhan', 3:'Muharram'}
        if question_3 == 'c' or question_3 == 'muharram':
            print("your answer is correct!")
            score += 1
        else:
            print(f"Your answer is incorrect! The correct answer is {option[3]}.")

    # question 4
        question_4 = (input("\n4) During which month is Eid-ul-Adha celebrated?\na) Ramadhan\nb) Dhul-Hijjah\nc) Muharram\nAns : ").lower())
        option = { 1:'Ramadhan', 2:'Dhul-Hijjah', 3:'Muharram'}
        if question_4 == 'b' or question_4 == 'dhul-hijjah':
            print("your answer is correct!")
            score += 1
        else:
            print(f"Your answer is incorrect! The correct answer is {option[2]}.")

    # question 5
        question_5 = (input("\n5) What is the call for prayer called?\na) Adhan\nb) Takbeer\nc) Kalimah\nAns : ").lower())
        option = { 1:'Adhan', 2:'Takbeer', 3:'Kalimah'}        
        if question_5 == 'a' or question_5 == 'adhan':
            print("your answer is correct!")
            score += 1
        else:
            print(f"Your answer is incorrect! The correct answer is {option[1]}.")

    # set timer
        end_time = time.time()
        total = end_time - start_time
        if total <= 50:
                print(f"You got {score} score out of 5")
        else:
                print("Sorry! your time is over")

# making function
def math():
        score = 0
        start_time = time.time()

    # question 1
        question_1 = (input("\n1) How many times you can subtract the number 5 from 25?\na) 3 times\nb) 5 times\nc) 1 times\nAns : ").lower())
        option = { 1:'3 times', 2:'5 times', 3:'1 times'}
        if question_1 == 'c' or question_1 == '1 times':
            print("your answer is correct!")
            score += 1
        else:
            print(f"Your answer is incorrect! The correct answer is {option[3]}.")

    # question 2
        question_2 = (input("\n2) Divide 30 by 1/2 and add 10. What is the answer?\na) 25\nb) 65\nc) 70\nAns : ").lower())
        option = { 1:'25', 2:'65', 3:'70'}
        if question_2 == 'c' or question_2 == '70':
            print("Your answer is correct!")
            score += 1
        else:
            print(f"Your answer is incorrect! The correct answer is {option[3]}.")

    # question 3
        question_3 = (input("\n3) What is three fifth of 100?\na) 3\nb) 5\nc) 60\nAns : ").lower())
        option = { 1:'3', 2:'5', 3:'60'}
        if question_3 == 'c' or question_3 == '60':
            print("your answer is correct!")
            score += 1
        else:
            print(f"Your answer is incorrect! The correct answer is {option[3]}.")

    # question 4
        question_4 = (input("\n4) What is 7% equal to?\na) 0.007\nb) 0.07\nc) 0.7\nAns : ").lower())
        option = { 1:'0.007', 2:'0.07', 3:'0.7'}
        if question_4 == 'b' or question_4 == '0.07':
            print("your answer is correct!")
            score += 1
        else:
            print(f"Your answer is incorrect! The correct answer is {option[2]}.")

    # question 5
        question_5 = (input("\n5) What is the value of x if x^2=169?\na) 13\nb) 1\nc) 338\nAns : ").lower())
        option = { 1:'13', 2:'1', 3:'338'}
        if question_5 == 'a' or question_5 == '13':
            print("your answer is correct!")
            score += 1
        else:
            print(f"Your answer is incorrect! The correct answer is {option[1]}.")

    # set timer
        end_time = time.time()
        total = end_time - start_time
        if total <= 50:
                print(f"You got {score} score out of 5")
        else:
                print("Sorry! your time is over")

# starting the program
your_name = input("Enter your name : ")
print(f"Welcome! {your_name} on the quiz.")
ans = "yes"
while ans == "yes":
        while ans == "yes":
        
        # topic selection  
                print("\nWhich type questions do you want?\na) general knowledge\nb) islamic\nc) math")
                topic = (input("Type all if you want all above quizes otherwise enter topic name which gives above : ").lower())
                if topic == "general knowledge" or topic == "a":
                        print("\nYou have a 50 seconds for 5 MCQ's. Your time start now")
                        general_test() 
                        break

                elif topic == "islamic" or topic == "b":
                        print("\nYou have a 50 seconds for 5 MCQ's. Your time start now.")
                        islamic()   
                        break

                elif topic == "math" or topic == "c":
                        print("\nYou have a 50 seconds for 5 MCQ's. Your time start now.")
                        math()
                        break

                elif topic == 'all':
                        print("\nYou have a 50 seconds for each parts. Your time start now.")
                        general_test()                        
                        islamic()
                        math()
                        break
                        
                else:
                        print("Your input is invalid, please try again")

        #controling the program execution.
        ans = (input("\nType yes if you want quiz again otherwise type no for close : ").lower())    
        while ans != 'yes' and ans != 'no':
                print("Your input is invalid! Please try again")
                ans = (input("\nType yes if you want quiz again otherwise type no for close : ").lower())
        if ans == 'no':
            break
print(f"Thanks! {your_name} for given your response.")
        
