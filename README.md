# 1. Prediction of the baseball players selected for the hall of fame: is this player going to be recognized?

## 1.1. Dataset Description

The data was collected by Sean Lahman and was purchased on his page at the following link:

http://www.seanlahman.com/files/database/readme2017.txt

Sean Lahman is an investigative reporter who has collected a large amount of information about the teams that are part of the major leagues in the United States.

The National Baseball Hall of Fame and Museum located in New York is where all the history of this sport in the United States can be found. To be elected to the Hall of Fame, the following criteria must be met:

•	Competed in at least ten seasonsRetired for at least five seasons

•	Approval by a selection committee to be included on the ballot (usually players who have played ten or more years are considered worthy)

•	Must not be on the ineligible list (this means the player must not be expelled from baseball)

•	Considered elected if they receive at least 75% of the votes in the election

•	A player remains on the ballot if they receive at least 5% of the votes and remain for a maximum of 10 years

•	With this knowledge, the goal of this project was to build a machine learning model that can accurately predict if a Major League Baseball player will be voted into the Hall of Fame.

![image](https://user-images.githubusercontent.com/43154438/229946924-1848cde3-753e-4751-9c9d-e6aa5c3fbf15.png)

Figure 1: the files needed to make this project

The files were copied to the root folder of the project for easier access. Each row represents the data of a baseball player, including information pertaining to a single season. The player is identified by a unique code, which we will use to identify them in our analysis. Here’s a brief explanation of the contents of each file:

•	AllstarFull.csv contains information about whether the player played in a Major League Baseball All-Star game or not.

•	Appearances.csv contains the number of games the player participated in while active.

•	AwardsPlayers.csv contains information about awards the players have received over time, such as Most Valuable Player, Rookie of the Year, Gold Glove, Silver Slugger, and World Series MVP.

•	Batting.csv contains the player’s offensive statistics, including batting information, divided by year.

•	Fielding.csv contains information about the player’s defense, such as assists, errors committed, and double plays.

•	HallOfFame.csv contains information about whether the player received votes or not to become part of the Hall of Fame, as well as additional details such as manager and coaching staff information.

•	People.csv contains the corresponding code, player’s name, and all personal information.

The files were copied to the root folder of the project for easier access. Each row represents the data of a baseball player, including information pertaining to a single season. The player is identified by a unique code, which we will use to identify them in our analysis. Here’s a brief explanation of the contents of each file:

•	AllstarFull.csv contains information about whether the player played in a Major League Baseball All-Star game or not.
•	Appearances.csv contains the number of games the player participated in while active.
•	AwardsPlayers.csv contains information about awards the players have received over time, such as Most Valuable Player, Rookie of the Year, Gold Glove, Silver Slugger, and World Series MVP.
•	Batting.csv contains the player’s offensive statistics, including batting information, divided by year.
•	Fielding.csv contains information about the player’s defense, such as assists, errors committed, and double plays.
•	HallOfFame.csv contains information about whether the player received votes or not to become part of the Hall of Fame, as well as additional details such as manager and coaching staff information.
•	People.csv contains the corresponding code, player’s name, and all personal information.

## 1.2. Project Objectives

Once the dataset has been obtained, it undergoes processing, analysis, and a model is created to predict which player will make it to the Hall of Fame. Each of the data sets in CSV files are collected strategically to have the data arranged appropriately before being entered into the Machine Learning model, and given that there are several data tables, the preprocessing involves several steps that may seem extensive.

![image](https://user-images.githubusercontent.com/43154438/229947077-c6b967a7-ae81-4111-89ea-8aef250c1f0b.png)

Figure 2: image that represents the union of different tables (datasets) that is what we did in this project

Next, some of the specific processes that were done with some of the data: Since the Batting dataset does not show the total game statistics, but rather the statistics by played year, we sum up all the data since we are interested in the total statistics. These statistics include: games played, at-bats, runs scored, doubles, etc. This process is performed through a summation in a for loop where according to the player’s identification, the corresponding statistical variables are summed up and this way all the information from the played years will be stored. The same explained in the previous paragraph is the same thing that is done for the rest of the files, as what we need are the final statistics.

Although for the case of awards dealing with the AwardsPlayers dataset, instead of a values accumulator, a counter is used for each award so that it can count the number of different awards each player has and the same occurs with the AllstarFull dataset where the number of All-Star games played by each player is counted.

From the information obtained in the HallOfFame.csv file, the dependent variable was obtained for the Machine Learning model, as this is where the player’s votes to be part of the Hall of Fame are located. The rest of the information such as the managers and coaching staff are deleted as they are not important.

These are some of the graphs of important feature relevance:

![image](https://user-images.githubusercontent.com/43154438/229947227-0292bc84-370b-4d65-977f-1e60014d4337.png)

Figure 3: histograms that represent the number of votes per player depending on variables such as: number of races, number of Home Runs, number of years played, and number of appearances in the All-Star game.

