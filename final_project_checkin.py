#import statements
import pandas as pd
import random
from argparse import ArgumentParser
import sys
import matplotlib.pyplot as plt



class Akinator:
   def __init__(self):
      self.player_name = ""
      self.player_answers = []
      self.num_questions_asked = 0
      self.max_questions_before_guess = 10
      self.dataset = None  # Initialize the dataset
      self.score = {"Player score": [0], "Akinator score": [0]}
         
   def __repr__(self):
       return f"Your animal is {self.player_answers[0]}, a {self.player_answers[1]}, and lives in {self.player_answers[2]}"
        
#player method (Shafiqat)
   def player_input(self):
      """Prompt the player for their name and welcome them to the Akinator Game.

      This function displays a welcome message for the Akinator Game and prompts 
      the player to enter their name.
      The player's name is then returned as the result of the function.

      Returns:
         str: The name entered by the player."""
        
      print("Welcome to the Akinator Game!")
      print("Please answer the following questions with yes or no.")
      player_input = input(f"Please enter your name: ")
      return player_input 

    #match question function (Shahil)
   def match_question(self, player_answers, dataset):
      """Matches questions to answers taken from the start_game function and asks
      the final question in order to make the final match.

         Args:
            player_answers (start_game): A start_game object that is used to 
            call the start_game function. Then used to filter through the 
            dataset
            dataset (dataframe): The dataframe that contains the database this
            function will filter through in order to return the final match

         Returns:
            str: A statement that prints the name of the final match animal into the
            terminal
        
         Side effects:
            Prints questions that have to take a user input and a final statement
            into the terminal
         """
         
      filtered_df = dataset.loc[(dataset["Color"] == self.player_answers[0]) & 
                            (dataset["Diet"] == self.player_answers[1]) & (dataset["Habitat"]
                            == self.player_answers[2])]
      if filtered_df.empty:
          print(f"No animal found in the database!")
      else:
          final_match_list = filtered_df["Animal"].values.tolist()
          final_match = ""
          tries = 0
          while final_match == "":
                final_question = input(f"Is the animal a {final_match_list[0]}?: ")
                if final_question == "no":
                    try:
                        final_match_list.pop(0)
                        tries += 1
                        if tries == 3 or len(final_match_list) == 0:
                    #keep track of total score, maybe have an attribute in init
                    #that initializes the variable so that it can be used throughout
                    #have a score keeper method too
                            print("I give up!")
                            self.score["Player score"] = [x+1 for x in 
                                                    self.score["Player score"]]
                            final_match = "N/A"
                    except IndexError:
                        print("No more animals to guess! I give up!")
                elif final_question == "yes":
                    final_match = final_match_list[0]
                    print(f"The animal you're thinking of is: {final_match}")
                    self.score["Akinator score"] = [x+1 for x in 
                                                       self.score["Akinator score"]]
                    #Haven't implemented game_over yet
                    self.game_over(dataset)


   def game_over(self, dataset):
       """
       """
       df = pd.DataFrame.from_dict(self.score)
       graph_request = input(f"Would you like to see the current score?: ")
       if graph_request == "Yes" or "yes":
           #this doesn't show up for some reason
         df.plot.bar()
         plt.show()
   
       repeat_game(dataset)
           
        
    #question format function (Mohammad)
   def question_file(self, questions):
      '''
      Selects and formats a question from predefined categories based on the game state.

      This method selects a category from the list of question categories. If the number of questions asked
      is below a certain threshold, it formats a question to ask the player.
        
      Returns:
      None. The function prints a question to the console for the user to answer.
      '''
      for tup in questions:
         first, second = tup
         # first_tup= tup[0]
            

    # Select a random characteristic to ask about
      characteristic = random.choice(first)

      print(characteristic)



    #game state function (Colin)
   def gamestate(self, response):
        """A method that will update the gamestate of the game and 
        find the number of questions already asked and number of animals
        guesses.
            
        Args:
            resposne(str): The response of the user 
        Raises:
         ValueError: raises error when incorrect input is put in
        Side effects:
         The function prints out two f strings and modifies the values
         of current_question attribute."""
        self.num_questions_asked += 1 if response.lower() in ["yes", "no"] else 0
        print(f"The number of questions asked is {self.num_questions_asked}")

def repeat_game(dataset):
    """
    Asks the player if they want to play the game again.
    If yes, resets the game parameters and starts the game again.
    If no, prints a farewell message and exits the program.
    """
    while True:
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == "yes":
            # Reset game parameters 
            start_game(dataset)
        elif play_again == "no":
            print("Thank you for playing! Goodbye.")
            sys.exit()  # Exit the program
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

#start game function (Johnathan)
def start_game(dataset):
        """
        Starts the Akinator-style game where the program asks questions to 
        form a guess about which animal the player is thinking of
        
        Side Effects:
            Prints out the player answers as a list called player_answers
        """
        dataset = pd.read_csv("Animal Dataset.csv")
        akinator = Akinator()
        player_answers = akinator.player_input()
        
        questions = [[("Is it Black?: ", "Black"), ("Is it White?: ", "White"), ("Is it Brown?: ", "Brown"),
                        ("Is it Yellow?: ", "Yellow"), ("Is it Gray?: ", "Gray"),("Is it Orange?: ", "Orange"), 
                        ("Is it Tan?: ", "Tan"), ("Is it Pink?: ", "Pink"), ("Is it Green?: ", "Green")],
                [("Is it an Herbivore?: ", "Herbivore"), ("Is it a Carnivore?: ", "Carnivore"), ("Is it a Ommnivore?: ", "Ommnivore"), ("Is it a Insectivore?: ", "Insectivore")],
                [("Does it live in the Grasslands?: ", "Grasslands"), ("Does it live in the Arctic?: ", "Arctic"), 
                ("Does it live in the Savannas?: ", "Savannas"), ("Does it live in the Rainforest?: ", "Rainforests"), 
                ("Does it live in the Forest?: ", "Forests"), ("Does it live in the Ocean?: ", "Oceans"), ("Does it live in Coastal Waters?: ", "Coastal Waters"),
                ("Does it live in the Mountains?: ", "Mountains"),("Does it live in the Desert?: ", "Desert"), ("Does it live in the Plains?: ", "Plains"), ("Does it live in the Tundra?: ", "Tundra")]
                ]
        
        
        
        for arr in questions:
            for (q,k) in arr:
               answer = input(f" {q} ")
               if answer.lower() == "yes":
                  akinator.player_answers.append(k)
                  akinator.gamestate(answer)
                  print("Player answers:", akinator.player_answers)
                  break
        
        print(repr(akinator))
        
        akinator.match_question(player_answers, dataset)
        repeat_game(dataset)
        
def parse_args(argslist):
    """Parses the command line arguments
       
       Args:
       argslist(list of str)= a list of arguments from the command line
       
       Returns:
       namespcae= returns the parsed arguments as a namespace"""
    parser= ArgumentParser()
    parser.add_argument("dataset", help= "a datatset full of animal info")
    return parser.parse_args(argslist)
if __name__ == "__main__":
    args= parse_args(sys.argv[1:])
    start_game(args.dataset)

