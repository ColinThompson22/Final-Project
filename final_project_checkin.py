#import statements
import pandas as pd
import random
from argparse import ArgumentParser
import sys
import matplotlib.pyplot as plt



class Akinator:
   def __init__(self, **kwargs):
      """Initialize the Akinator game object.


        Attributes:
           player_input (str): The name of the player.
           player_answers (list): A list to store player's answers during the game.
           num_questions_asked (int): Counter to keep track of the number of questions asked.
           max_questions_before_guess (int): Maximum number of questions to ask before guessing.
           dataset (DataFrame or None): The dataset containing animal information.
           score (dict): Dictionary to keep track of player and Akinator scores during the game.
                         Example: {"Player score": [score], "Akinator score": [score]}
           **kwargs: Additional keyword arguments to initialize attributes.
                     Example: player_input="John", max_questions_before_guess=15
       """
      
      self.inp = kwargs.get("player_input", "")
      self.player_answers = []
      self.num_questions_asked = 0
      self.max_questions_before_guess = kwargs.get("max_questions_before_guess", 10)
      self.dataset = kwargs.get("dataset", None)
      self.score = {"Player score": [0], "Akinator score": [0]}

         
   def __repr__(self):
       return f"Your animal is {self.player_answers[0]}, a {self.player_answers[1]}, and lives in {self.player_answers[2]}"
        
#player method (Shafiqat)
   def player_input(self, **kwargs):
      """Prompt the player for their name and welcome them to the Akinator Game.

      This function displays a welcome message for the Akinator Game and prompts 
      the player to enter their name.
      The player's name is then returned as the result of the function.

      Keyword Args:
        player_name (str): Name of the player (if passed as a keyword argument).

      Returns:
         str: The name entered by the player.
         """
      
      print("Welcome to the Akinator Game!")
      print("Please answer the following questions with yes or no.")
      inp = kwargs.get("player_name", None)
      if inp:
          self.inp = inp
      else:
          inp = input("Please enter your name: ")
          self.inp = inp
          print(f"Welcome {self.inp} to the Akinator Game!")
          return self.inp

    #match question function (Shahil)
   def match_question(self, dataset):
      """Matches questions to answers taken from the start_game function and asks
      the final question in order to make the final match.

         Args:
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
                            print("I give up!")
                            self.score["Player score"] = [x+1 for x in 
                                                    self.score["Player score"]]
                            self.game_over(dataset)
                            final_match = "N/A"
                    except IndexError:
                        print("No more animals to guess! I give up!")
                elif final_question == "yes":
                    final_match = final_match_list[0]
                    print(f"The animal you're thinking of is: {final_match}")
                    self.score["Akinator score"] = [x+1 for x in 
                                                       self.score["Akinator score"]]
                    self.game_over(dataset)

    #keep_score method (Shahil)
   def keep_score(self):
       """Keeps the scores of every instance of the game by writing into a
       text file called "score_keeper.txt"
       
       Side effects:
            Writes into score_keeper.txt
       """
       with open("score_keeper.txt", "a", encoding = "utf-8") as f:
          f.write(
             f"{self.score['Player score'][0]} - "
             f"{self.score['Akinator score'][0]}\n"
             )

   def game_over(self, dataset):
       """
         Ends the current game session, plots the score graph, writes the scores into a file, and offers the option to replay.

         Args:
            dataset (DataFrame): The DataFrame used for the game session.

          Side effects:
          - Writes to 'score_keeper.txt' appending the current scores at the end of the file.
          - Modifies the score attribute of the instance to record the latest game results.
       """
       df = pd.DataFrame.from_dict(self.score)
       graph_request = input(f"Would you like to see the current score?: ")
       df.plot.bar()
       plt.show() if graph_request.lower() == "yes" else ""
       self.keep_score()
       repeat_game(self, dataset)
           
        
    # question format function (Mohammad)
   def question_file(self, questions):
      '''
      Selects and prints a question to the console based on the current game state and a predefined set
      of question categories.


    Args:
        questions (list of tuple): A list of tuples where each tuple contains a
                        set of related questions and associated category. 
                        Each tuple is structured (question_str, category_str).
    Returns:
        None. 

    Side effects:
        - Modifies internal state by selecting a  question based on the game state.
        - Prints a question to the console for the user to answer which affects the console's output state.
    """
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

# show_score function (Shahil)
def show_score(filepath):
    """Shows the total score between the player and Akinator if the player
    says that they would like to see it. Total score calculated by adding all
    the scores for player and Akinator from the score_keeper file separately.

    Args:
        filepath (.txt file): Path to the file, in this case, the score_keeper
        file.
    Side effects:
        Asks the user if they would like to see the total score and prints
        the score to the terminal.
    """
          
    

# repeat game (Mohammad)
def repeat_game(obj, dataset):
    """
    Offers the player the option to play the game again. If the player chooses to continue, 
    the game parameters are reset and the game restarts. If the player chooses to end, 
    it displays the final scores and exits the program.

    Args:
        obj (Akinator): The game object instance that contains the current game state.
        dataset (DataFrame): The DataFrame that the game uses for querying animal data.

    Side Effects:
        - Inputs from the user determine whether the game restarts or ends.
        - Modifies the game state by resetting parameters if the game restarts.
        - Writes the final scores to the console if the game ends.
        - Exits the program if the player decides not to continue.

    Returns:
        None
   """
    while True:
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == "yes":
            # Reset game parameters 
            start_game(dataset)
        elif play_again == "no":
           # Assume self.score is structured like: {"Player score": [value], "Akinator score": [value]}
         show_score("score_keeper.txt")
         player_score = obj.score["Player score"][0]          
         akinator_score = obj.score["Akinator score"][0]

         max_score = max(player_score, akinator_score)

         if max_score == player_score:
            print(f"The highest score is by the Player with {max_score}.")
            print("Thank you for playing! Goodbye.")
            sys.exit() 
         elif max_score == akinator_score:
            print(f"The highest score is by Akinator with {max_score}.")
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
        repeat_game(akinator, dataset)
        show_score("score_keeper.txt")
        
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

