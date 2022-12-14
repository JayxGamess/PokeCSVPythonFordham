#Jason Mathew Homework IX - Final Project
#Welcome to my Project! It is different from the Proposal. I have created a tool to have a Pokemon, from 1st to 8th Generation, picked at random for you. You tell which generation would you like to see, and it will select a random Pokemon from 1st to 8th Gen.
#If requested, a list can be shown with some of the Pokemon. I was not able to figure out how to conduct Pagination on Pandas and Python by the time this was finished.
#The CSV being used in this assignment was found on Kaggle.com, and was made by the user Mario Tormo Romero. You can find the source here: https://www.kaggle.com/datasets/mariotormo/complete-pokemon-dataset-updated-090420
import random
import pandas as pd
#Random is being imported for the usage of this being a randomizer, pandas is being imported as it's part of being a dataframe in CSV
pokemonList = 'D:/Graduate/Fall 2022/Python/archive/Pokedex520.csv'
#CSV is included on Blackboard. the 5/20 refers to the last time it was updated according to Kaggle, so it is on the most recent version.
pokemonDf = pd.read_csv(pokemonList, encoding = 'utf-8')
# def randomPokemon():
#     randomChoice = random.choice(tuple(pokemonGenDf))
#     print(randomChoice)
# Attempted to make this function work. but I kept receiving a value that wasn't readable easily. Such as <function randomPokemon at 0x000001E76B2EED40>
try:
    genChoice = int(input('Which generation of Pokemon would you to randomly select from? Please use a number from 1 to 8. If you want to see a list from each generation, type 0. To exit, press 9\n>>'))
except ValueError:
        genChoice = int(input('You did not type a number in. Please type a number from 1 to 8 please.\n>>'))
#Asking the user for which generation they would like to see. If they try to use any string, they'll receive this notification and one more opportunity type a number in. If they type a number greater than 9, there is an if statement handling that.
while genChoice == 0:
    try:
        genList = int(input('Which generation of Pokemon do you want to see a list for? Please use a number from 1 to 8\n>>'))
        if genList == 0 or genList >= 9:
            genChoice = int(input('You did not enter a value from 1 to 8 in. Please type a number from 1 to 8 in please. If you want to see a list from each generation, type 0. To exit, press 9 \n>>'))
        else:
            pokeList = pokemonDf['name'][pokemonDf['generation'] == genList]
            print(pokeList)
            genChoice = int(input('Would you like to see another generation of Pokemon? Type 0. If you know which generation you would like to use for the randomizer, select a number from 1 to 8. To exit, press 9.\n>>'))
    except ValueError:
        print('You did not type a number in. Please type a number from 1 to 8 please.')
    except IndexError:
        genChoice = int(input('You did not enter a value from 1 to 8 in. Please type a number from 1 to 8 in please. If you want to see a list from each generation, type 0. To exit, press 9 \n>>'))
#The while loop is used for the condition that the user asks to see a list of the Pokemon from each generation. The user will input a number from 1 to 8, and if they don't, will be directed to do so. The list will be loaded from Pandas Dataframe showing just the name and the
# number on the Pokemon Index. Afterwards, they are asked if they are ready to select a generation, want to see more lists, or exit the program.
#I am going to argue that my usage of Pandas to create a list is sufficient for data structures.
if genChoice == 9:
    print('Thank you for checking out the Pokemon selector!')
# The choice to exit the program.
elif genChoice > 9:
    genChoice = int(input('You entered a number for a generation that is not available. Please try a number from 1 to 8. If you want to see a list from each generation, type 0. To exit, press 9 \n>>'))
# This if statement is here in case a user tries to place a number that is higher than 9, given that any number 9 and below serve a function.
else:
    pokemonGenDf = pokemonDf['name'][pokemonDf['generation'] == genChoice]
    try:
        randomPokemon = random.choice(tuple(pokemonGenDf))
        print('The randomly selected Pokemon of choice for you is', randomPokemon,', congratulations on your new Pokemon!')
    except IndexError:
        print('Error. Pokemon Generation was out of Range')
#Prints out the results of the choice made by the user. 