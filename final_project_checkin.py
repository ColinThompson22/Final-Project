#import statements

#start game function (Johnathan)

#match question function (Shahil)

#question format function (Mohammad)
def question_file:


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
