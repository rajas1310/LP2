print('Welcome to COVID-19 Expert system')
covidSuspisionCounter=0


severity=0
asym=0
oxylevel=0
temp=0

questions=['What is your body temparature','What is your oxygen level','How many vaccines have you taken','What is your age']
yesnoqs=['Do you have cough and cold','Are you able to recognize smell and taste','Are you suffering from sore throat','Are you suffering from headache','Are you suffering from BP/ diabetes','Have you come in a contact of a Covid suspicious person']

for i in range(6):

    print(yesnoqs[i])
    print()
    ans=input()

    if(i!=1 and ans=='yes'):

        covidSuspisionCounter+=1

    elif(i==1 and ans=='no'):

        covidSuspisionCounter+=1

for i in range(4):

    print(questions[i])
    print()

    if(i==0):
        ans=float(input())

        if(ans>=101.0):
            severity+=2
            covidSuspisionCounter+=1
            temp=1

        elif(ans<101.0 and ans>=99.6):
            severity+=1

        else:
            severity+=0
    if(i==1):
        ans=int(input())

        if(ans>=94):
            severity+=0

        elif(ans<94 and ans>87):
            severity+=1

        else:
            severity+=2
            covidSuspisionCounter+=1
            oxylevel=1

    if(i==2):
        ans=int(input())

        if(ans==0):
            severity+=2

        elif(ans==1):
            severity+=1

        else:
            severity+=0

    if(i==3):
        ans=int(input())

        if(ans>12 and ans<31):
            severity+=0

        elif(ans>31 and ans<51):
            severity+=1

        else:
            severity+=2

if(covidSuspisionCounter>3):
    print('The patient is probably covid positive')
    print()

    if(severity<3):
        print('It looks like the symptoms are mild\nhome quarantine')

    elif(severity>=3 and severity<6):
        print('The patient can get an admission in the general ward')

    else:
        print('The patient looks critical')

else:
    print('It looks like patient is not Covid positive')

print()

if(oxylevel==1):
    print("Keep monitoring patient's oxygen level")
    
if(temp==1):
    print("Keep monitoring patient's body temperature")
    
    
    
    
    
#___________________________________________________________
    # 2
 print("\033[0;32m\033[1mWelcome to Depression Level Prediction System!")

def print_options():
    print("\t(1) Not at all")
    print("\t(2) Several Days")
    print("\t(3) More than half the days")
    print("\t(4) Nearly everyday")

question_list =["Little interest or pleasure in doing things",
                "Feeling down, depressed, or hopeless",
                "Trouble falling or staying asleep, or sleeping too much",
                "Feeling tired or having little energy",
                "Poor appetite or overeating",
                "Feeling bad about yourself or that you are a failure or have let yourself or your family down",
                "Trouble concentrating on things, such as reading the newspaper or watching television",
                "Moving or speaking so slowly that other people could have noticed. Or the opposite being so figety or restless that you have been moving around a lot more than usual",
                "Thoughts that you would be better off dead, or of hurting yourself"
                ]
score = 0

def accept_ans():
    flag = True
    while (flag):
        ans = int(input("Your choice: "))
        if(ans == 1 or ans==2 or ans == 3 or ans ==4):
            flag = False
            # print(ans-1)
            return (ans-1)
        else:
            print("\033[0;31mEnter a valid option!\033[1;37m")
 
def find_results(score):
    print("\n\033[4mSCORE: ", score)
    print("Depression Severity: ", end="")
    if(score in range(1,5)):
        print("Minimal Depression")
    elif(score in range(5,10)):
        print("Mild Depression")
    elif(score in range(10,15)):
        print("Moderate Depression")
    elif(score in range(15,20)):
        print("Moderately Severe Depression")
    elif(score in range(20,28)):
        print("Severe Depression")
    else:
        print("No Depression")
    print("\033[0m")
        
        
def PHQ9test(questions, score):
    for i in range(len(questions)):
        print("\n" ,i+1,". \033[1;34m", questions[i], "\033[1;37m")
        print_options()
        score += accept_ans()
        # print("score= ", score)
    find_results(score)

PHQ9test(questions=question_list, score=score)
    
    
   
