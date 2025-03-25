# Imports the random module to allow selecting random elements from lists

import random 

# Welcome message. 
# Explains the game to users.
# The \n in a string is known as the newline character.

print("Welcome to Python Mad Libs!\nIt's learning time")
print("Answer the following questions to create your very own silly story.\n") 

# Gather user inputs
# Prompts the user to enter an adjective, noun, verb, or adverb 
# Stores the response in the variable (adj,n,v,or adverb)

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")

# Build the story using an f-string
# Uses f-strings to insert user inputs into a sentence structure.
# The \n adds a line break to improve formatting

story = (
    f"Today, I saw a {adjective} {noun} that decided to {verb} {adverb}.\n"
    "I couldn't believe my eyes!"
)

# Display the completed story
print("\nHere is your story:")
print(story)

# This function will generate a random story using predefined templates.

def generate_random_story():
    """Generates a random story from predefined templates."""

# The docstring """Generates a random story from predefined templates.
# """ is a comment that describes the function’s purpose.
# It helps users and developers understand what the function does.

    templates = [
# It is a list containing three dictionaries.
# Each dictionary represents a different type of story structure.
# Inside each dictionary, "structure" defines the type of story, and "elements" contains lists of possible words to use.
        {
             "structure": "character_action_location",
            "elements": {
                "characters": ["a brave mouse", "a mischievous dog", "a curious cat", "a quirky squirrel"],
                "actions": ["searched for a pot of gold", "drew a portrait of the sky", "solved a mysterious puzzle", "climbed a tall tree"],
                "locations": ["in a dark swamp", "on a sunny beach", "inside a hidden castle", "atop a fiery volcano"],
            },
        },
        {
            "structure": "problem_solution",
            "elements": {
                "problems": ["the town's water supply was gone", "all the stars disappeared from the sky", "the school's computers crashed", "the magical door was locked"],
                "solutions": ["a clever inventor built a new well", "a wise owl found a hidden constellation", "a tech-savvy student fixed the network", "a friendly ghost revealed the key"],
            },
        },
        {
            "structure": "journey_transformation",
            "elements": {
                "characters": ["a shy kangaroo", "a funny robot", "a grumpy clown", "a lost time traveler"],
                "journeys": ["traveled to a faraway land", "sailed across the ocean blue", "flew through a ravaging storm", "journeyed to the past"],
                "transformations": ["became a mad scientist", "found a loving family", "learned to tie his shoes", "returned with ancient knowledge"],
            },
        },
    ]

# The random.choice() function selects a random element from the templates list. 
# Each template defines a structure for a story and contains elements like characters, actions, locations, problems, solutions, journeys, and transformations.
   
    selected_template = random.choice(templates)
    story = ""

# An empty string story is initialized to hold the generated story.
# The code checks the structure key of the selected template to determine how to construct the story.
# For "character_action_location" Structure
# if Statement: Checks if the structure of the selected template is "character_action_location". If this condition is true, 
# generating a story where a character performs an action in a specific location.​
# elif Statements: If the if condition is false, the program evaluates the elif conditions sequentially

    if selected_template["structure"] == "character_action_location":
        char = random.choice(selected_template["elements"]["characters"])
        action = random.choice(selected_template["elements"]["actions"])
        location = random.choice(selected_template["elements"]["locations"])
        story = f"Once upon a time, {char} {action} {location}."

    elif selected_template["structure"] == "problem_solution":
        problem = random.choice(selected_template["elements"]["problems"])
        solution = random.choice(selected_template["elements"]["solutions"])
        story = f"There was a time when {problem}. But then, {solution}."

    elif selected_template["structure"] == "journey_transformation":
        char = random.choice(selected_template["elements"]["characters"])
        journey = random.choice(selected_template["elements"]["journeys"])
        transformation = random.choice(selected_template["elements"]["transformations"])
        story = f"{char} {journey} and {transformation}."

# The constructed story is returned as the output of the function.​

    return story 

# Generate and print a random story
print("\nRandom Story:")
print(generate_random_story())

# Loop to generate and print multiple stories
print("\nHere are three more random stories:")

# The underscore _ is a convention used in Python to indicate that the loop variable.
# It is intentionally being ignored;repeat the loops.
for _ in range(3):
    print(generate_random_story())

def generate_princess_frog_story():
    """Generates a story about a princess and a frog."""

    princess_names = ["Cindy", "Elizabeth", "Nicole", "Stephanie"]
    frog_adjectives = ["slimy", "shiny", "bald", "tiny"]
    frog_actions = ["asked for a kiss", "wanted to play hopscotch", "demanded a seat at the head of the royal table", "needed help finding his lily pad"]
    princess_reactions = ["was overjoyed", "was curious", "was amused", "was kind"]
    story_outcomes = ["the frog turned into a prince", "the princess received her first kiss", "they became husband and wife", "the frog and princess lived happily ever after"]

    princess = random.choice(princess_names)
    frog_adj = random.choice(frog_adjectives)
    frog_act = random.choice(frog_actions)
    princess_react = random.choice(princess_reactions)
    outcome = random.choice(story_outcomes)

    story = f"Princess {princess} was walking in the forest when a {frog_adj} frog {frog_act}. She {princess_react}. In the end, {outcome}."

    return story

# Generate and print a princess and frog story
print("\nPrincess and Frog Story:")
print(generate_princess_frog_story())
