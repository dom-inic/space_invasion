making an object from a class is called instantiation. instances of a class
a function that is part of a class is called a method
the init method ai a special method python runs automatically whenever we create a new instance based on a certain class. 
the self parameter is required in the method definition  and must come before other parameters.
every method call associated with a class automatically passes self, which is a reference to the instance itself. 
self gives the individual instance access to the attributes and methods in the class.
self is passed automatically so there is no need to pass it. 
any variable prefixed with self is available to every method/function in the class.e.g self.screen = screen will be available to every every function in the class ship, class settings, class bullets and so much more. 
self.screen = screen takes the value stored in the parameter screen and stores it in the variable screen which is then attached to the instance ship being creavariables that are accessible through instances like this are called attributes

when you set an initial value for an attribute you dont need to include a parameter for that attribute. e.g the attribute self.moving_right = False. this attribute has the string False hence no need include a parameter in the init method in the ship class. 
you can use instances as attributes
inheritance
use of another class as an attribute in another class 
rect.centerx.right()
importing classes
from ship import Ship
unittest module for testing codes
try and except to manage errors that might arise when playing the game 
in order for you to begin the game you need to press p which stands for play 
to shoot use the spacebar
to quit the game place the esc button
to move right and left use the right and left arrow keys 
the remaining part is the pausing part which am yet to decide which keyboard button to use since almost every known key by the user is 
already being used for other purposes. but it is currently working with the capslock key . 
also tweaked it to work best with the covid 19 pandemic we have right now. 
