from io import open

class bot():

    def __init__(self):
        self.response_bot = "hi, my name is ChitChat, and i can talk with you whenever you want!!"
        self.input_user = str()
        self.input_user_1 = self.input_user
        self.first_bot = 0
        self.sentence = "x"

    def response(self):

        while self.input_user != "good bye" and self.input_user != "bye":

            if self.first_bot < 1:
                print(self.response_bot, "\n")

                self.first_bot = +1

            self.input_user = str(input())
            self.input_user_1 = self.input_user
            self.input_user_1 = "".join(filter(str.isalnum, self.input_user_1))

            try:
                self.sentence = open("responses/"+str(self.input_user_1), "r")
                self.response_bot = self.sentence.read()
                self.sentence.close()

                print("\n",self.response_bot,"\n")

            except FileNotFoundError:
                print(f"\ni dont know what to answer ¡you can teach me tho! \nwhat do you want me to say when you say <{self.input_user}>:\n")

                self.sentence = open(str("responses/"+self.input_user_1), "w")
                self.input_new_response = str(input())
                self.sentence.write(self.input_new_response)
                self.sentence.close()

                if self.input_user != "good bye" and self.input_user != "bye":
                    print("\nhi, my name is ChitChat, and i can talk with you whenever you want!!\n")
            except PermissionError:
                print(f"\ni can't answer symbols, so i'm gonna reset:\n\nhi, my name is ChitChat, and i can talk with you whenever you want!!\n")


bot_1 = bot()

bot_1.response()