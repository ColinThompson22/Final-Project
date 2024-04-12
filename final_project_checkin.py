#import statements

#start game function (Johnathan)

#match question function (Shahil)

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
    question_categories = ["Animal", "Height", "Weight", "Color", "Lifespan (years)", "Diet", "Habitat", "Predators", "Average Speed (km/h)", "Countries Found", "Conservation Status", "Family", "Gestation Period (days)", "Top Speed (km/h)", "Social Structure", "Offspring per Birth"]
        

    # Select a random characteristic to ask about
    characteristic = random.choice(question_categories)

    #Format and print the question
    #Allows computer to ask the user what certain characteristics are from the categories from the list
    question = f"What is the {question_options[random.choice]} of the animal you're thinking of?"
    print(question)

     #Determines how many quesitons have been asked before guessing 
     self.num_questions_asked = 0
     self.max_questions_before_guess = 10 



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
