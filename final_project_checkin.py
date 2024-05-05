#import statements
import pandas as pd
import random
from argparse import ArgumentParser
import sys

class Akinator:
        def __init__(self):
         self.player_name = ""
         self.player_answers = []
         self.num_questions_asked = 0
         self.max_questions_before_guess = 10
         self.dataset = None  # Initialize the dataset
         
         def __repr__(self):
            return f"Your animal is {self.player_answers[0]}, a {self.player_answers[1]}, and lives in {self.player_answers[0]}"
        
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
            answer (start_game): A start_game object that is used to call the
            start_game function. Then used to filter through the dataset
            dataset (dataframe): The dataframe that contains the database this
            function will filter through in order to return the final match

         Returns:
            str: A statement that prints the name of the final match animal into the
            terminal
        
         Side effects:
            Prints questions that have to take a user input and a final statement
            into the terminal
         """
         questions = self.question_file
         answer = start_game(dataset)
         filtered_df = dataset.loc[(dataset["Color"] == answer["color"]) and 
                            (dataset["Diet"] == answer["diet"]) and (dataset["Habitat"]
                            == answer["habitat"])]
         final_match_list = filtered_df["Animal"].tolist()
         final_match = ""
         tries = 0
         while final_match == "":
             final_question = input(f"Is the animal a {final_match_list[0]}?: ")
             if final_question == "no":

                final_match_list.pop(0)
                tries += 1
                if tries == 3:
                    #keep track of total score, maybe have an attribute in init
                    #that initializes the variable so that it can be used throughout
                    #have a score keeper method too
                    return f"I give up!"
             elif final_question == "yes":
                final_match = final_match_list[0]
                return f"The animal you're thinking of is: {final_match}"
        
        
    #question format function (Mohammad)
        def question_file(self):
         '''
         Selects and formats a question from predefined categories based on the game state.

         This method selects a random category from the list of question categories. If the number of questions asked
         is below a certain threshold, it formats a question to ask the player.
        
         Returns:
            None. The function prints a question to the console for the user to answer.
         '''
    #List of categories the computer guesses from 
         question_categories = ["Color", "Diet", "Habitat"]
            

    # Select a random characteristic to ask about
         characteristic = random.choice(question_categories)

         print(f"Is it {characteristic.lower()}")



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
         if response.lower() == "yes":
            self.num_questions_asked += 1
            print(f"The number of questions asked is {self.num_questions_asked}")
         elif response.lower() == "no":
            self.num_questions_asked += 1
            print(f"The number of questions asked 9s {self.num_questions_asked}")
         else:
            raise ValueError("invalid input. Please answer either yes or no.")

def repeat_game():
    """
    Asks the player if they want to play the game again.
    If yes, resets the game parameters and starts the game again.
    If no, prints a farewell message and exits the program.
    """
    while True:
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == "yes":
            # Reset game parameters 
            start_game()
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
        akinator.player_input()
        p_answers = akinator.player_answers
        
        questions = [[("Is it Black?: ", "Black"), ("Is it White?: ", "White"), ("Is it Brown?: ", "Brown"),
                        ("Is it Yellow?: ", "Yellow"), ("Is it Gray?: ", "Gray"),("Is it Orange?: ", "Orange"), 
                        ("Is it Tan?: ", "Tan"), ("Is it Pink?: ", "Pink"), ("Is it Green?: ", "Green")],
                [("Is it an Herbivore?: ", "Herbivore"), ("Is it a Carnivore?: ", "Carnivore"), ("Is it a Ommnivore?: ", "Ommnivore"), ("Is it a Insectivore?: ", "Insectivore")],
                [("Does it live in the Grasslands?: ", "Grasslands"), ("Does it live in the Arctic?: ", "Arctic"), 
                ("Does it live in the Savannas?: ", "Savannas"), ("Does it live in the Rainforest?: ", "Rainforests"), 
                ("Does it live in the Forest?: ", "Forests"), ("Does it live in the Ocean?: ", "Oceans"), ("Does it live in Coastal Waters?: ", "Coastal Waters"),
                ("Does it live in the Mountains?: ", "Mountains"),("Does it live in the Desert?: ", "Deserts")]
                ]
        
        akinator.question_file()
        akinator.match_question(p_answers, dataset)
        
        for arr in questions:
            for (q,k) in arr:
               answer = input(f" {q} ")
               if answer.lower() == "yes":
                  akinator.player_answers.append(k)
                  break
        
        akinator.gamestate(answer)
        print("Player answers:", akinator.player_answers)
        
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

