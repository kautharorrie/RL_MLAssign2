Assignment 2 - Reinforcement Learning
CSC3022F - 2023
FourRooms

Kauthar Orrie - ORRKAU001

Notes:
 - Scenarios 1 and 2 takes <30seconds
 - Scenario 3 will take longer to run because it has a bigger number of epochs
 - the final image for the optimal path will be saved to image.png, this can be changed in line 131 or alternatively the last few lines in the file

File included in submission: 
	- FourRooms.py
	- Scenario1.py:
		- first Scenario where the agent is only picking up one package (red) from
		the grid-world. Goal is to find the optimal path to the 1 package
	- Scenario2.py:
		- second Scenario where the agent is picking up all 3 packages (red, blue, green) from
		the grid-world in any order. Goal is to find the optimal path to all 3 packages
	- Scenario3.py:
		- second Scenario where the agent is picking up all 3 packages (red, blue, green) from
		the grid-world in any a specified order --- red -> green -> blue. Goal is to find the optimal path to all 3 packages
		in that order
	- makefile:
		- builds the virtual environment and installs the required packages 
	- requirements.txt:
		- included to use with the makefile, stores the sames of the required packages
	- app.py:

How to run my program:
	- build virtual environment by running the command:
		>> make
		
	- activate the virtual environment by running the command:
		>> source ./venv/bin/activate 

	- deactivate the virtual environment by running the command "deactivate" 

	- to run any of the programs while virtual environment is running:
		>> python3 Scenario1.py
		>> python3 Scenario2.py
		>> python3 Scenario3.py 		