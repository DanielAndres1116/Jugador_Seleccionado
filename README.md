# 1. Prediction of the baseball players selected for the hall of fame: is this player going to be recognized?

## 1.2. Dataset Description

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


