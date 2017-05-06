# WayOfTheCard #
A randomized card game in all senses of the word. Below is our architectural review overview. 

## NOTE: WE HAD ACCIDENTALLY OVERWRITTEN THIS IN OUR README INSTEAD OF SAVING IT AS AN OLD DOCUMENT. TO SEE THE ORIGINAL COMMIT, SEE https://github.com/juicyslew/WayOfTheCard/blob/335dbc2847a0cbadf8cc43679d8c66eb8559e53a/README.md ##

## Background and context: (3-5 minutes) ##

For this project we are making a randomly generated card game based on card games like Hearthstone and Magic the Gathering. Both the rules and the cards are being randomly generated. So far, we have created a Hearthstone knock off with randomly generated cards. 
	
In the beginning of each game, each player receives  a deck of randomly generated cards. These cards are split into two general categories: “dudes” and “dos”. The whole point of the game is to play cards to kill the other player. The “dude” cards called minions can be deployed to attack the other opponent and do cards have some effect on the board. There is a limit to the power of the cards you can deploy each turn. Each player starts with two points called mana. Every turn you get one additional mana to spend on cards. The more destructive cards cost more mana so they can only be played towards the end of the game making the game more interesting. 

This structure is based on Hearthstone. An outline of the Hearthstone UI is below. 

<img src="https://github.com/juicyslew/WayOfTheCard/blob/master/hearthStone.png" width="600">

A brief outline of everything that you can see on the screen:

* Weapons (not currently implemented) are equippable items that can only be equipped to your hero, allowing your hero to attack an enemy.
* Minions are the “dudes” in our game who can attack other minions or your opponent’s character
* The minion with a shield on it is a “taunt” minion; this minion must be destroyed before the opponent’s hero can be attacked.
* A hero power is not something we not are implementing (at least not yet); it costs 2 mana and is something that can be used recurringly.

Currently our random generation is limited to player names, card names, card costs, and card effects. We also do not have a UI currently. Eventually we also want to randomize rules and include random semi-random pictures mined from the top google images result to add another layer of fun to our game.

## Game Demo (5 minutes + 3-4 minutes questions) ##

Play our game to see it work! Ask questions as necessary.

Sample cards generated are below.

<img src="https://github.com/juicyslew/WayOfTheCard/blob/master/Sample%20Card%20One.png" width="200">

<img src="https://github.com/juicyslew/WayOfTheCard/blob/master/Sample%20Card%20Two.png" width="200">

<img src="https://github.com/juicyslew/WayOfTheCard/blob/master/Sample%20Card%20Three.png" width="200">

## Future Work/Questions (3 minutes + 5 minutes question) ##

The largest part of our project that still needs to completed is the graphics and user interface. Ideally, the final game will use pygame to show cards on the field and be controlled using mouse clicks or drag-and-drop. In addition, we will implement some amount of random generation of base game rules, rather than just having random cards being generated in the context of a standard game.
	In addition, we can expand the game’s implemented ability effects, triggers, and other card attributes to make a more varied play experience. These effects can be based on common card effects in Magic or Hearthstone, and can interact with player hands and discard piles rather than just with creatures and life totals.

## Free Play and Feedback (remainder of time) ##

At this point, feel free to play around with our code. Ask any and all questions and if you have any suggestions feel free to tell us.

Possible things you may want to discuss:

* Discuss how to get random images for cards
* Discussed RGB value based on descriptive for a saved dictionary of pictures
* Could smash together pictures for different things
* Feedback about scope of the project
* Feedback about rules/how to give them
* Wishlist for UI 
* Randomness of rules: How much would you figure out vs. the game tell?
