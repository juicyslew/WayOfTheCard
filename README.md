# WayOfTheCard
A randomized card game in all senses of the word.

Background and context: (3-5 minutes) 

For this project we are making a randomly generated card game based on card games like Hearthstone and Magic the Gathering. Both the rules and the cards are being randomly generated. So far, we have created a Hearthstone knock off with randomly generated cards. 
	
In the beginning of each game, each player receives  a deck of randomly generated cards. These cards are split into two general categories: “dudes” and “dos”. The whole point of the game is to play cards to kill the other player. The “dude” cards called minions can be deployed to attack the other opponent and do cards have some effect on the board. There is a limit to the power of the cards you can deploy each turn. Each player starts with two points called mana. Every turn you get one additional mana to spend on cards. The more destructive cards cost more mana so they can only be played towards the end of the game making the game more interesting. 

This structure is based on Hearthstone. An outline of the Hearthstone UI is below. 

<img src="https://github.com/juicyslew/WayOfTheCard/blob/master/hearthStone.png" width="600">

A brief outline of everything that you can see on the screen:

Weapons (not currently implemented) are equippable items that can only be equipped to your hero, allowing your hero to attack an enemy.
Minions are the “dudes” in our game who can attack other minions or your opponent’s character
The minion with a shield on it is a “taunt” minion; this minion must be destroyed before the opponent’s hero can be attacked.
A hero power is not something we not are implementing (at least not yet); it costs 2 mana and is something that can be used recurringly.

Currently our random generation is limited to player names, card names, card costs, and card effects. We also do not have a UI currently. Eventually we also want to randomize rules and include random semi-random pictures mined from the top google images result to add another layer of fun to our game.

