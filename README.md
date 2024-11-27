This project tries to emulate the game Donkey Kong. After following the steps marked by the project sprints, we have achieved to successfully program a fully 
functional version of the game. The code has been designed taking into account the techniques learned in class such as object oriented techniques or encapsulation


We have created 8 classes in order to have a cleaner code and to have the program well organised.

● Board Class:
The Board Class is the skeleton of the project. It is the class designated to store all the data we have from other classes and make the game work. 
This class is divided in 3 different methods:
  - __init__: Which initialises all of the object that are going to be in the board
  - update : It acts as a loop until the user presses Q (exiting the game).
  - draw : This method draws all of the items in the board game by adding the sprites on the right position

● Constants Class:
In this class we inserted all the initial values, constants and positions of all the elements of the game. 
Also the different images that were going to be drawn in the board. For instance, the initial position for Mario is at the 1st platform on the left.

● Plat Class:
In this class we wrote how did the initial values of the platforms should behave (be bigger than 0 in the case of the positions of x and of y), 
and we could use an image. We knew we were going to create a tuple list at the “board Class” were we were going to insert all the different positions of the platforms

● Ladders Class:
In this class we wrote how did the initial values of the ladders should behave (be bigger than 0 in the case of the positions of x and of y),
and we could use an image. We knew we were going to create a tuple list at the “board Class” were we were going to insert all the different positions of the ladders

● Mario Class:
This class is the one that controls Mario and its behaviour. Here we can find Mario's movement, the methods to check whether we should use
the gravity or not, the methods that check it’s position in relation to the barrels...

● Barrels Class:
This class controls the barrels behaviour, the direction it is going, if it is on a ladder or the direction it should take after falling to the next platform.

● Princess Class:
In this class we check if the positions of the princess are the correct ones and we add a method to make her “scream” the word help randomly.

