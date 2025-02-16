class Game :
    
    def __init__(self,user,computer):
        self.user = user
        self.computer = computer

    def get_user(self):
      
       
      if  input ("Enter your choice: ") == "r" or "p" or "s":
        #   while result == "r" or "p" or "s":
            result = print("Computer plays: ")
            # return result
      else:
            print("Invalid choice")
            # return False
    get_user()       
       
  

# Game.get_user(self)




#         return self.user
    
#     def get_computer_item(self):
#         return self.computer
    
#     def get_game_result(self, user_item, computer_item):
#         return self.game_result
    
#     def play(self):
#         self.user = input("Enter your choice: ")
#         self.computer = random.choice(['rock', 'paper', 'scissors'])
#         print(f"Computer plays: {self.computer}")

# #         if self.user == self.computer:
# #             self.game_result = "It's a tie!"
# #         elif self.user == 'rock' and self.computer == 'scissors':
# #             self.game_result = "You win!"
# #         elif self.user == 'rock' and self.computer == 'paper':
# #             self.game_result = "You lose!"
# #         elif self.user == 'paper' and self.computer == 'rock':
# #             self.game_result = "You win!"
# #         elif self.user == 'paper' and self.computer == 'scissors':
# #             self.game_result = "You lose!"
# #         elif self.user == 'scissors' and self.computer == 'paper':
# #             self.game_result = "You win!"
# #         elif self.user == 'scissors' and self.computer == 'rock':
# #             self.game_result = "You lose!"

# #         print(self.game_result)
    

    
# #     # def set_user(self, user):
# #     #     self.user = user

# #     # def set_computer(self, computer):
# #     #     self.computer = computer

# #     # def set_game_result(self, game_result):
# #     #     self.game_result = game_result


    
# # def play(self):
# #         self.user = input("Enter your choice: ")
# #         self.computer = random.choice(['rock', 'paper', 'scissors'])
# #         print(f"Computer plays: {self.computer}")

#         # if self.user == self.computer:
#         #     self.game_result = "It's a tie!"
#         # elif self.user == 'rock' and self.computer == 'scissors':
#         #     self.game_result = "You win!"
#         # elif self.user == 'rock' and self.computer == 'paper':
#         #     self.game_result = "You lose!"
#         # elif self.user == 'paper' and self.computer == 'rock':
#         #     self.game_result = "You win!"
#         # elif self.user == 'paper' and self.computer == 'scissors':
#         #     self.game_result = "You lose!"
#         # elif self.user == 'scissors' and self.computer == 'paper':
#         #     self.game_result = "You win!"
#         # elif self.user == 'scissors' and self.computer == 'rock':
#         #     self.game_result = "You lose!"

#         # print(self.game_result)