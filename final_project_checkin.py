#import statements
import pandas as pd

#start game function (Johnathan)

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

#game state function (Colin)

#player method (Shafquat)