# WayOfTheCard #
A randomized card game in all senses of the word. It possesses random rules, random cards, and random pictures.

## Website ##
https://juicyslew.github.io/WayOfTheCard/

## Authors ##
MJ McMillen 				Github: MJ-McMillen
Nick Sherman			  Github: NickShermeister
Nate Sampo: 			  Github: natesampo
Will Derksen:       Github: juicyslew
Jeremy Ryan:        Github: jeremycryan


## Description ##

For this project we are making a randomly generated card game based on card games like Hearthstone and Magic the Gathering. Both the rules and the cards are being randomly generated. So far, we have created a Hearthstone knock off with randomly generated cards.

In the beginning of each game, each player receives  a deck of randomly generated cards. These cards are split into two general categories: “dudes” and “dos”. The whole point of the game is to play cards to kill the other player. The “dude” cards called minions can be deployed to attack the other opponent and do cards have some effect on the board. There is a limit to the power of the cards you can deploy each turn. Each player starts with two points called mana. Every turn you get one additional mana to spend on cards. The more destructive cards cost more mana so they can only be played towards the end of the game making the game more interesting.

This structure is based on Hearthstone and Magic The Gathering

A brief outline of everything that you can see on the screen:

* Minions are the “dudes” in our game who can attack other minions or your opponent’s character
* The minion with a shield on it is a “taunt” minion; this minion must be destroyed before the opponent’s hero can be attacked.

We have a User Interface that displays cards with randomly generated pictures on them. There are animations that represent different special effects that act on each card.

Currently, our game actions are run through the command line and the actions appear on the screen.

## Getting Started ##
Required Software:
	1. Python 3
	2. PIL Image Library
	3. pygame
	4. Numpy
	5. Download Github

### How to Install in Ubuntu ###
	1. In command line type
	 * sudo pip3 install Pillow
	 * sudo apt-get build-dep python-pygame
	 * sudo apt-get install python-dev
	 * sudo pip3 install pygame
	 * sudo pip3 install numpy
	2. Download Github: https://help.ubuntu.com/lts/serverguide/git.html	.
			sudo apt install git
	3. clone repository
				git clone https://github.com/juicyslew/WayOfTheCard.git
	4. find the way of the card folder in your computer
	5. In the command line type: python3 Game.py
	6. Enjoy!

### How to Install in Windows ###
1. Register for Github
2. Click the green 'Clone or Download' button in the GitHub repository.
3. Click 'Download ZIP'
4.	Right click on the downloaded zipped folder and click 'Extract All'
5. Select an easily accessible location to extract the files to, and confirm the extraction (Remember this location!)
6. Install Python 3 by downloading and running the Windows Executable Installer (Under Files in https://www.python.org/downloads/release/python-361/).
	* Make sure to check the  box that says 'Add Path' in the Installer.
9. Open the terminal by clicking on the Windows button in the bottom left corner, typing 'Command Prompt', right clicking on it and hitting 'Run as Administrator'
10. If you checked the 'Add Path' box in the installer, 'python' will be your file path. If not, find the location of your Python 3 install and copy the location of 'python.exe'
11. Paste this file path into the terminal (should look something like this 'C:\Python36\python.exe'
12.	Add a space and type '-m pip install Pillow' after the file path. Press Enter
13. Repeat steps 7-9, however replace 'Pillow' with 'pygame'
14. Repeat step 13 but replace 'pygame' with 'numpy'
15. Again repeat steps 7 and 8, and add a space after the Python file path
16. Find the location of your WayOfTheCard install and copy the location of 'Game.py'
17. Paste this file path into the terminal after your Python file path
18. Should look something like this: 'C:\Python36\python.exe C:\Users\Nate\Desktop\WayOfTheCard\Game.py'
19. Press Enter to Launch the Game
20. Enjoy!



## Usage ##
1. Run Game.py in the command line
2. Options for Arena mode and Random rule generation will appear
3. It will ask to confirm randomly generated player names.
4. The Game field will appear in a separate window.
5. go through your turns in the command line to move the cards around the field
6. to close, press control+c in the command line.



## License ##

Copyright (c) 2017 Miranda J. McMillen Nichlos C. Sherman Nathan J. Sampo, William N. Derksen, and Jeremy C. Ryan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sub-license, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
