# Data formatting 

for ease of consistency and being able to read the data into the simulator, our strategies need to be in the following format.

# File format
Theres 5 files that need to be found to be properly loaded into each strategy chart.
```
hard.csv - hard hand actions
soft.csv - soft hand actions
split.csv - soft hand actions
surrender.csv - if the player should surrender
insurance.csv - checks to see if the player wants insurance
```
Each row represents a dealer's card, and each column represents the players card. The dealer card is absent from the data storage. The order for the rows is as follows
2,3,4,5,6,7,8,9,10,A

e.g., Row 2 (indexed on 0) represents a dealer having a 4.
For hard and soft hands for each combination of dealer card and player count, there are 3 actions that are desired.
D - Double
S - Stand
H - Hit

For surrender, split  hands and insurance, each combination of dealer card and player coutn simply has 
Y - Yes (either split or surrender)
N - No

The base Player object performs its action by reading in this order:
1. check surrender. If N
2. Check split. If N
3. Check if hand is soft. If soft, check soft for action
4. If hand is hard, check hard for action

The player additionally has a method to check if the player wants insurance.

This player may be extended for more functionality.

