# Final-Project

## Files in the repository:

**Animal Dataset.csv**
    -The dataset used in program. Contains "Animal", "Color", "Diet", "Habitat"
columns. Players will pick an animal from the dataset to guess.

**final_project_checkin.py**
    -The project's main program. Runs a game between the player and a bot who
tries to guess what animal the player is thinking of from the dataset.

**score_keeper.txt**
    -A text file that keeps track of the score across instances of all games.

## How to run the program on the command line:

**On Windows:** python final_project_checkin.py Animal_Dataset.csv

**On Mac:** python3 final_project_checkin.py Animal_Dataset.csv

## How to use the program:

The program is used to play a game against the Akinator bot. 

Before playing a game, make sure to pick an animal found in the 
Animal_Dataset.csv, as if you choose the characteristics of an animal that isn't
in the database, it returns "No animal found in database!"

The user is initially asked to input their name into the terminal. After doing
so, the user is prompted with questions about the animal's characteristics like
its color, diet, and habitat. Once all of these are answered, guesses are made
by Akinator. The user can either say yes or no when asked if Akinator is making
the right guess. If Akinator cannot make the correct guess in 3 tries or runs
out of animals to guess before it makes 3 guesses, it will give up and the user
gets a point. If Akinator guesses correctly, it gets a point. After the end of
a round, the user can choose to see a bar plot representation of the previous
round's score. Then, the user is asked if they would like to play again. If they
answer yes, the game start over again from the beginning. If they answer no,
the user is asked if they would like to see the total score between them and
Akinator across all games. If they answer yes, the total score is printed into
the terminal and if they answer no, the program prints the name of the person
that won the previous round and then states "Thank you for playing! Goodbye."
before exiting.

## How to interpret the output of the program:

The answers that the user makes throughout a round is output into the terminal
so that the user remembers what their answers are. It also outputs the number
of questions asked. There will always only be 3 questions asked before Akinator
makes a guess, so it shows the user how much longer they have been the end of
the round.

## Attribution:

|Method/function|Primary Author|Techniques demonstrated|
|---------------|--------------|-----------------------|
|_repr_         |Johnathan Hill|Magic method           |
|player_input   |Shafiqat Alao |f-string               |
|match_question |Shahil Paudel |Pandas, list comprehension|
|game_over      |Mohammad      |Data visualization     |
|question_file  |Mohammad      |None                   |
|gamestate      |Colin Thompson|Conditional expression |
|show_score     |Shahil Paudel |None                   |
|repeat_game    |Mohammad      |Key function           |
|start_game     |Johnathan Hill|Sequence unpacking     |
|parse_args     |Colin Thompson|ArgumentParser class   |
|__init__       |Shafiqat Alao |Keyword Argument       |
