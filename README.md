# POINT-PERSPECTIVE-TOOL

## Demo
Demo Video: <https://youtu.be/BK8Besf3P_E>

## GitHub Repository
GitHub Repo: <https://github.com/Crow3765/point-perspective-tool>

## Description
### Purpose
    The point-perspective-tool is a Python-written program that helps 
artists figure out the perspective of their illustration or drawing. It is 
designed to help users expedite the layout phase of the creative process 
without needing to fiddle with the, at times, confusing perspective rulers of 
our drawing programs (if they even have one in the first place, that is).

### Files
    In the root directory of the program, the user can find this 'README.md' 
file alongside the 'requirements.txt' file, which contains the names of the 
pip-installable 3rd party libraries that this program requires in order for 
it to function.
    Aside from that, we can also find the src folder directory, which contains
the python file 'project.py' and an assets folder, containing two images that 
are used directly within the program: 'border.png' and 'vanishing_point.png'. 
The first image is used as a border within the program window, it is meant to 
emulate the workspaces found in every drawing application, with its buttons 
located off to the side and a canvas featured prominently in its center. The 
second image is used in creating the vanishing points in the program. It was 
created to simplify the code and make it unnecessary to repeatedly call the 
pygame.draw method to form the grid.

### Features
#### Vanishing Point Grid
    The program is able to create up to a maximum of three point perspective
grids by right-clicking directly onto the canvas with your trackpad or mouse.
If you attempt to right-click over the border, or anywhere else that is not 
within the canvas' bounds, you will be unable to create a vanishing point. 
This is so that a user can add more lines to the vanishing point during the 
creative process without obstruction.

#### Compositional Box
    On the left hand side of the border, a button with a square symbol can be
found. If you left-click on this button, a rectangle will appear over the 
canvas. This rectangle can be used for compositional purposes. The user can
create the box first and then place the vanishing point(s) around it to ensure
that they are properly spaced out, or the user can place the points on the 
screen and adjust the box as needed afterwards.
    With the arrow keys, the user can move the box to whichever point on the
canvas, and with cmd + the arrow keys, you can adjust the size of the box.
With this, you can figure out the approximate size of your illustration or
drawing and also use it during the creative process to know which point the 
lines are leading up to.

#### Save Perpesctive Grid
    Using cmd + s, you can save only the canvas to your device. When saved,
the image will fall under the src folder as 'point-perspective-guidelines.png'
and will re-write itself if the keys are pressed again later on.
    When the keys are pressed, text will appear in the bottom-left corner of 
the program to inform the user on whether or not the image was saved and where 
it was saved. This text will disappear approximately two seconds after the 
keys were first pressed, and will reappear if the keys are pressed once more, 
with the image being saved there on afterwards.

### Future Areas of Improvement
    There are a few areas that could be improved on, and generally, I believe 
the entire program could be really improved on as a whole. I mainly wished I 
had gotten the re-color gridlines feature working as I had previously hoped 
and planned to do. However, I could not get the code to properly work, so 
instead I just opted to alter the vanishing point image to feature thinner 
lines for easier readability.
    I also wished I could have figured out a way to reset the program without
needing to exit out of it as after creating the vanishing points, you will be 
unable to move or edit them further. Thus, if you make a mistake, you will 
have to relaunch the program again.
    For the button(s), I should have seperated them from the background, that
way, I could have used the seperated image for the '.collidepoint()' function,
instead of needing to create boxes over them just for the buttons to work. 
Lastly, the compositional box feature could be improved on as well as the
keys need to be pressed repeatedly in order for the box to grow, shrink, or
move, instead of being held down as I had previously wanted.