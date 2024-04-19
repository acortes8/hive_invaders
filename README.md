# Hive Invaders
2D arcade-style game, based on Space Invaders, using Python and Tkinter. A player-controlled entity, represented by a bee sprite, shoots down enemy wasps using honey-spit projectiles. Wasps move horizontally across the screen in waves, working their way down the screen. Implements collision detection, game-over conditions, and victory conditions. Game-over if any wasp touches the bottom of the screen. Victory if all wasps are destroyed. Player is prompted with"play again or quit" when either condition is met. If play-again is selectioned, both of the two color-type of wasps will have their "difficulty" increased, one more-so than the other, making wasps move with greater speed. Object-oriented programming principles to organize code into modular classes for bees, wasps, and projectiles. With additionally incorporated randomization for enemy color-type spawn locations and custom-made sprites to enhance gameplay.  

Skills: Python · Tkinter · Object-Oriented Programming (OOP) · Event Handling · Collision Detection · Thonny  

Game-play:  
1. Enemy wasps move from one side of the screen to the other. Once any of them collide with the edge of the screen they will all switch directions and work their way to the other side of the screen. Everytime they collide with the edge, they also move down. This repeats until any of the wasps make it to the bottom of the screen, shoot them down before they make it there.  
![image](https://github.com/acortes8/hive_invaders/assets/46253800/2418ae6c-6459-4442-a670-943eb633790b)  
![image](https://github.com/acortes8/hive_invaders/assets/46253800/b843ee91-9b27-48d4-8084-11e42f915b9d)  
2. Use the arrow keys to move left or right.  
![image](https://github.com/acortes8/hive_invaders/assets/46253800/35f1eca1-f63b-4459-8fb0-4cf63927c81b)   
3. Press space bar to fire a projectile, if it collides with a wasp, the wasp will be destroyed. Anticipate their movement and destroy all wasps before they make it to the bottom of the screen.  
![image](https://github.com/acortes8/hive_invaders/assets/46253800/2ad1b240-f854-43ae-ade4-9165580f72a0)  
4. If you lose, a prompt will appear, letting you know of your defeat, and asking if you would like to play again or quit.  
![image](https://github.com/acortes8/hive_invaders/assets/46253800/1893822a-812e-4480-af8f-2b272635cfd4)  
6. If you win, by destroying all wasps, a prompt will appear, letting you know of your victory, and will ask the former question again.  
![image](https://github.com/acortes8/hive_invaders/assets/46253800/b52c1c66-b89f-43e3-b28f-04923ae70b25)  
7. If you select play again, the difficulty of the game will increase. Both the red and blue wasps will move faster now, but the blue in particular will be even faster than the red. Making the task of landing shots more difficult, and giving you less time before they reach the bottom of your screen.  
![image](https://github.com/acortes8/hive_invaders/assets/46253800/86e755c3-f379-4eea-ad43-3da042918fa2)  

How to run:  
1. Having python downloaded and installed on your computer, double-click the python file in the downloaded, and unzipped, project file. Game should now run. Important to note, the png sprite files in the project folder need to remain in that folder for the game to run, as their pathing is relative.  
![image](https://github.com/acortes8/hive_invaders/assets/46253800/24def92b-db56-4dc6-bbc5-986e86454d23)  

