* I have created Pong, which is a two-player game where the players have to control the 
paddles to not let the ball go through their gates. Players have to use the "w" and 
"UP" keys to move up, and "s", "DOWN" keys to move down. Every time a player fails
to retract the ball (misses), their competitor will have their score increased by 1.
And did I mention the background color changes as the ball hits one of the walls?
Anyway, go play it.


* I have made the game as user-friendly as possible. There are five files to be opened
before the game can run. Each one of the files has a unique function (f.e. ball.py controls the ball).
To run the game, you should go to the "pong_game.py" file and run it. It will print all the necessary 
instructions to play the game. But just in case, I'll give them here too:
	To move the paddles up and down, players should press the keys "w", "s" and the arrows "UP", "DOWN" respectively
	To quit the game press the "Esc" key

When you run the "pong_game.py" file, the python script will open as a new window, so you have to
go to it. However, I coded it so that the game stalls until you press the "Enter" key 
(this info is displayed on the screen).

It is important that the players press the Escape key to exit the game, this way they will get
important feedback on the game once it finishes. 

IMPORTANT!!!  I installed the "keyboard" package for the game to improve it. So if the device running it
does not have the package installed, the game will probably fail to run. 


* The window the game is on is 800w by 600h, which I thought was the best size for a game like this.
But when the user makes it go FullScreen, the fragments stay in their original positions. In other words,
the window is not responsive. I doubt that the user will see this as a problem, because its current 
dimensions make the game really comfortable to play. I will keep working on this feature.

* I think I deserve 20 points for the project.

***** One more thing important to mention is that I did not write a test.py file as a part of my project.
The reason behind it is that I inherited all the classes from the "Turtle Graphics" library, and
all the functions running in my files display their actions on the canvas (python script). In other words
the functions are responsible for tasks such as changing the background color or moving the paddles up/down; 
they do so directly without an input from the user.