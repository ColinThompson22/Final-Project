#import statements
import pandas as pd

#start game function (Johnathan)
def start_game(questions, player_answers):
    """
    Starts the Akinator-style game where the program asks questions to 
    form a guess about which animal the player is thinking of
    
    Args:
        questions(list of lists of tuples): The list of questions the program will ask the player
        player_answers(list): A list that stores the player answers
    
    Side Effects:
        Prints out the player answers as a list called player_answers
    """
    print("This is the akinator style program, the game will try to guess what animal you're thinking about through a series of questions. Please respond with either yes/no!")

    for arr in questions:
        for (q, k) in arr:
            answer = input(f" {q} ")
            if answer.lower() == "yes":
                player_answers.append(k)
                break

questions = [[("Is it Black?: ", "Black"), ("Is it White: ", "White")],
     [("Is it an Herbivore?: ", "Herbivore"), ("Is it a Carnivore: ", "Carnivore")],
      [("Does it live in the Grassland?: ", "Grassland"), ("Does it live in the Arctic: ", "Arctic")]]

player_answers = []

start_game(questions, player_answers)

print("Player answers:", player_answers)


#match question function (Shahil)
def match_question(answer, dataset):
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
    questions = question_format()
    answer = start_game(questions, answer)
    filtered_df = dataset.loc[(dataset[Color] == answer["color"]) and 
                         (dataset[Diet] == answer["diet"]) and (dataset[Habitat]
                          == answer["habitat"])]
    final_match_list = filtered_df["Animal"].tolist()
    final_match = ""
    while final_match == "":
        final_question = input(f"Is the animal a {final_match_list[0]}?: ")
        if final_question == "no":
            final_match_list.pop(0)
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
 question_categories = ["Animal", "Height (cm)", "Weight (kg)", "Color", "Lifespan (years)", "Diet", "Habitat", "Predators", "Average Speed (km/h)", "Countries Found", "Conservation Status", "Family", "Gestation Period (days)", "Top Speed (km/h)", "Social Structure", "Offspring per Birth"]
        

# Select a random characteristic to ask about
characteristic = random.choice(question_categories)

#Format and print the question
#Allows computer to ask the user what certain characteristics are from the categories from the list
computer_question = f"What is the {characteristic) of the animal you're thinking of?"
print(question)
    

#Determines how many quesitons have been asked before guessing 
self.num_questions_asked = 0
self.max_questions_before_guess = 10 
     
# Checks if the limit of questions before guessing has been reached
    if self.num_questions_asked >= self.max_questions_before_guess:
            print("Making a guess...")
    else:
        # Select a random characteristic to ask about
        characteristic = random.choice(question_categories)



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
        self.current_question += 1
    elif response.lower() == "no":
        self.current_question += 1
    else:
        raise ValueError("invalid input. Please answer either yes or no.")
    self.num_questions_asked += 1
    print(f"The number of questions asked is {self.num_questions_asked}")
    print(f"Yhe number of animals left is {len(self.animals)}")
#player method (Shafiqat)
