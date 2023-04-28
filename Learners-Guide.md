# Manim Learning Guide:

## Introduction

### What is Manim:
Manim is a powerful Python library for creating mathematical animations. It was created by Grant Sanderson, known as 3Blue1Brown, to make it easier to create engaging educational content. Manim allows you to create complex animations that demonstrate mathematical concepts in a visual and intuitive way.

### Why Manim:
Manim offers several benefits for educators, researchers, and students. It enables the creation of high-quality mathematical animations that can help students visualize difficult concepts. It also offers a lot of flexibility in terms of customization and can be used to create a wide variety of animations. Additionally, since Manim is written in Python, it can easily be integrated with other Python libraries and tools.

### Versions:
ManimCE and ManimGL are Manim versions with different graphics engines and rendering approaches. ManimCE uses Cairo for 2D and renders each frame as a separate image, while ManimGL uses OpenGL for 3D and offers real-time rendering. ManimCE is more comprehensive and user-friendly, while ManimGL is still developing and has fewer features.

### Resources:
The resource I would recommend is the Manim Website and which I used:
https://www.manim.community/


## Basic Animations

### Creating a Scene, Adding Objects to It:
To create a scene, you need to create a new class that inherits from the Scene class. Example:

Picture 1

Created a MyScene class that adds a Circle object to the scene using the self.add() method. You can add any type of object to the scene this way, including shapes, text, and images.

### Animating Over Time
To animate an object over time you use play()Example:

Picture 2

We scale the Circle object to double its size using circle.animate.scale(2) with linear rate function and 2 seconds duration.

### Changing Object Properties
You can change the properties of an object in Manim to create different effects. Example:

Picture 3 

A blue Circle object is created with 50% opacity, then shift(), set_color(), and set_fill() methods are used to animate the Circle's position, color, and opacity properties with the there_and_back rate function over a 2-second duration.

## Animating Text and LaTeX Equations
### Latex:
To animate equations Manim uses LaTex, a language unto itself. I won’t be providing a tutorial on how it works however below are some examples of LaTex:

### Equation:

Picture 4

### Matrix:

Picture 5

### Intergral:

Picture 6

### Greek symbols

Picture 7

### Fraction

Picture 8

## Animating text and LaTeX equations in Manim.

### Text:
The Text object is used to add text to a scene. Example:

Picture 9

We created a Text object with the example of "Hello World!" and then used the Write to animate it.


### Text Properties: 
We can change various properties of a Text object like position, color, opacity, etc. 

Picture 10

A red Text object is created with "Hello World!" and moved to the top edge of the screen. The object is animated by shifting it down, scaling it up, and changing its color to blue.


### LaTeX Equations:
Manim has great support for LaTeX equations. Example:

Picture 11

We created a MathTex object with the LaTeX equation.

Picture 12

Then used Write to animate it.

### Equation Properties: 
We can change various properties of a MathTex object like position, color, opacity, etc. Example:

Picture 13

Above we created a MathTex object with the LaTeX equation. 

Picture 14

The equation text object with yellow color is moved to the top edge of the screen using the to_edge method. The animation scales the object by a factor of 2 and changes its color to red.


## Advanced concepts


The AnimationGroup is used to animate multiple objects simultaneously. You create a list of the objects you want to animate, and then pass the list and the desired animation to an instance of AnimationGroup. Example:

Picture 15

We created a circle and a square, then AnimationGroup and pass the objects (circle and square) and the animation (Create) as arguments. Finally, play the animation using self.play(group).


Using the Transform class for smoothly transitioning between different object configurations:
Transform class enables smooth object transitions. Create initial and final objects, pass them to Transform instance. Example:

Picture 16

Create a circle and square, create initial animation to create the circle, wait using self.wait(), then Transform animation to transform circle into square.

Using Easing Functions to Control the Motion of Objects
Transform class smoothly transitions between different object configurations. To use, create the initial and final objects, then pass them to an instance of Transform. Example:

Picture 17

Create a circle, animate it with several transformations using the there_and_back easing function for smooth back-and-forth motion.



##Data visualization

Manim is a powerful tool for creating animated visualizations from graph plotting, customization, and animated scatterplots to histograms.

### Plotting graphs and charts with Manim:
To plot graphs, create a scene and instantiate an Axes object, which represents Cartesian axes. Use x_range and y_range to specify axis ranges and customize their appearance with x_axis_config and y_axis_config.

Picture 18

Create an Axes object with x and y-axis ranges of [-5, 5]. Customize axis appearance and plot a curve using a lambda function. Add the Axes object, axis labels, and curve to the scene.


### Moving Camera:
In the following I will explain the moving camera example by Manim. 


### Define the Following GraphCamera class
Now define the FollowingGraphCamera class. This inherits from MovingCameraScene, which provides the basic functionality for moving the camera around the scene.


Picture 19

### Save the initial camera state
Before we start animating the camera, save its initial state so we can restore it later. Do this using the save_state() method of the camera's frame object.

Picture 20

### Axes and the curve
To create axes and a curve, we use the Axes class to create the axes and the plot() method to plot the curve. In this example, the sin() function is plotted over the range [0, 3*PI]


Picture 21

### Dots based on the graph
We can now create dots based on the graph that we will use to animate the camera. In this example, we will create three dots: one that will move along the curve, and two that will mark the endpoints of the curve.

Picture 22

### Add the objects to the scene.
We can now add the axes, curve, and dots to the scene using add().

Picture 23


### Move the camera to the starting point.
Before we start animating the camera, we need to move it to the starting point of the animation. In this example, we will move the camera to the position of the first dot.

Picture 24


### Define the updater function.
To animate the camera along the curve, an updater function needs to be defined that updates the camera's position based on the moving dot's position. The add_updater() method of the camera's frame object can be used to accomplish this. 


Picture 25


### Move the dot along the curve
Use the MoveAlongPath animation to move the dot along the curve. We can pass in the moving_dot object, the graph object, and a rate_func (in this case, linear) to control the speed of the animation.


Picture 26



### Remove the updater
Once the animation is complete, we need to remove the updater function using the remove_updater() method of the camera's frame object.


Picture 27


### Restore the camera state
We can restore the camera's state to its initial state using the Restore() animation, passing in the camera.frame object.

Picture 28




## Tips:
### Creating animations with custom frame rates and resolutions
Default: Manim uses a frame rate of 60 frames per second and a resolution of 1080p. You can customize these settings to suit your needs.
To set a custom frame rate add the -r or --frame_rate flag to the command line when running Manim. For example, to set a frame rate of 30 fps, you can run:

Picture 29

To set a custom resolution, you can add the -p or --pixel_height flag to the command line when running Manim. For example, to set a resolution of 720p (1280x720 pixels), you can run:

Picture 30

### Using Positional  constants to position objects	
Manim's constants UP, DOWN, LEFT, and RIGHT are useful for layout and object alignment. Example: Use LEFT and RIGHT constants to position two text objects side-by-side with space between them

Picture 31

Use move_to to position text objects relative to the screen by multiplying LEFT and RIGHT constants by 4 to move them left and right of the screens centre.


### Creating custom shapes and paths using Bézier curves and other curve types
Manim provides several built-in curve types, such as Line, Arc, and Circle. However, you may sometimes need to create custom shapes and paths using Bézier curves or other curve types.

To create a Bézier curve use the CubicBezier, taking four control points as arguments:

Picture 32

Create Bézier curve using four control points - UP, 2 * RIGHT, 2 * LEFT, and DOWN. CubicBezier returns a Path object for animation using Create method. Manim has other curve types, including QuadraticBezier and ArcBetweenPoints.


## Using the VGroup & Mobject.add() 

VGroup class for grouping multiple Mobjects (Mathematical objects) together. 
To create a VGroup, pass the Mobjects to be grouped as arguments:

Picture 33

The example creates a horizontal group of a Circle and a Square using VGroup. Then, the group is rotated 90 degrees.

Using the Mobject.add() to add new objects to an existing group:

Picture 34

In this example, a Triangle is added to the existing group using the add method and positioned next to the square using the next to method.






