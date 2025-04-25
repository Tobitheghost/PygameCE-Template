<img src="https://raw.githubusercontent.com/Tobitheghost/PygameCE-Template/refs/heads/main/PygameCE%20x%20Tobi.png"/>

# Pygame Template by Tobi Ghost
This is a starting template for Pygame CE. It has a state machine (inspired by [itsthatianguy's](https://github.com/itsthatianguy/youtube/tree/main/pygame-state) [Youtube Video](https://www.youtube.com/watch?v=PZTqfag3T7M&t=228s)). That makes combining "Screens" easy to implement. Menus can be added by inheriting from the State module and adding your new module to `Game.py`. 

## Setup

1. **Getting the Files**
	Clone the repository.

        `git clone https://github.com/Tobitheghost/PygameCE-Template.git`

	Or download the Zip file.


2. **Virtual Environment** 
	To create a virtual environment, go to the **/Games** folder and run the following command. This will create a new virtual environment in a folder named `.venv`:
	
    Windows: 

        `py -m venv .venv`
    
    Mac/Linux: 

        `python3 -m venv .venv`


    Next you will need to Activate the virtual environment. This will put the virtual environment-specific python and pip executables into your shell’s `PATH`.

    Windows:

        `.venv\Scripts\activate`
    
    Mac/Linux:

        `source .venv/bin/activate`

    <details>
        <summary>Tips</summary>
        If you want to switch projects or leave your virtual environment, deactivate the environment with the following command:

        deactivate
    </details>


    Lastly you will download the requirements.

    Windows: 

        `py -m pip install -r requirements.txt`
    
    Mac/Linux: 

        `python3 -m pip install -r requirements.txt`


3. **Running**
    You can now run the program from the **/Games** folder with the following command.

    Windows: 

        `py main.py`
    
    Mac/Linux: 

        `python3 main.py`

## Getting Started
#### Creating 'Screens'.
In the `GAMES\screens\...` folder are some examples of "Screens"; modules that inherit from "State" (`GAMES\screens\state.py:State()`). These Modules are then imported and references from `GAMES\game\game.py` and then added to the dictionary in `Game()` where the key is a string of the name of the "Screen" and the value is the corresponding class.

#### Using Settings.
The default size of the window for the program is 320x180 and is set in `GAMES\game\settings.py` under `SCREEN_WIDTH` and `SCREEN_HEIGHT`. This module is imported into `GAMES\game\game.py` and used when Pygame is initialized. You can also adjust the size by changing the `SCREEN_SCALE`, which is defaulted to 1, and the `SCREEN_WIDTH` and `SCREEN_HEIGHT` will be multiplied by `SCREEN_SCALE` when initializing Pygame. The settings module also holds constants for colors. 

#### Setting Captions.
In `GAMES\game\game.py` the Pygame isntance has a caption that is set to show the frame rate. Changing the caption for the window wont effect the other uses of delta time and the FPS.

---

The pixel art banner was made by Tobi Ghost (me) - [TobiTheGhost.com](https://github.com/itsthatianguy/youtube/tree/main/pygame-state) - I'm not sure what license this should have. If you want to give me credit, that would be cool.