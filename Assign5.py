from nltk.chat.util import Chat, reflections
import random

#Rule-based Chatbot using NLTK library

def gen_rand_bal():
    x = random.randint(0,500)
    return x

rules = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?\n",]
    ],
    [
        r"hi|hey|hello",
        ["Hello, WELCOME TO CALLNET SERVICES!\n", "Hey there, WELCOME TO CALLNET SERVICES!\n", ]
    ],
    [
        r"(.*)need(.*)help(.*)",
        ["How can I help? View Plans, Complaints, Check number balance?\n","What would you like to explore today?\n"]
    ],
    [
        r"(.*)show(.*)plans(.*)|(.*)plans(.*)",
        ["Prepaid: \nRs. 199 : 1.5GB/day : Unlimited local Calls : 28 days validity;\n"
         "Rs. 259 : 2GB/day : Unlimited local Calls : 28 days validity;\n"
         "Rs. 399 : 3GB/day : Unlimited local Calls : 56 days validity;\n"
         "Postpaid: \nRs. 399 : 40GB + 150GB: Unlimited Local Calls : Amazon Prime Video (1-yr Subscription)\n"
         "Rs. 499 : 50GB + 160GB: Unlimited Local Calls : Amazon Prime Video, Hotstar (1-yr Subscription)\n"
         "Rs. 999 : 100GB + 250GB: Unlimited Local Calls : Amazon Prime Video, Hotstar Premium, Netflix (1-yr Subscription)\n"]
    ],
    [
        r"(.*)problem(.*)|(.*)network(.*)issues(.*)|(.*)issues(.*)",
        
        ["Please call on our help line: 99988 99988 / 99988 99989 / 99988 99990\n"]
    ],
    [
        r"(.*)balance(.*)",
        ["Your balance is: Rs. {}\n".format(gen_rand_bal())]
    ],
    
    [
        r"quit|bye|gtg",
        ["Bye take care. See you soon :)\n","It was nice talking to you. See you soon :)\n"]
    ],
    
]


def chat():
    print("Hi! I'm Ric, your personal CALLNET assistant.")
    chat = Chat(rules, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()
