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
* [Manim Community Homepage](https://www.manim.community/)



## Basic Animations

### Creating a Scene, Adding Objects to It:
To create a scene, you need to create a new class that inherits from the Scene class. Example:

![Picture1](https://user-images.githubusercontent.com/115800139/235097053-81ab9e12-0038-44cd-a4a0-1c36ad267469.png)

Created a MyScene class that adds a Circle object to the scene using the self.add() method. You can add any type of object to the scene this way, including shapes, text, and images.

### Animating Over Time
To animate an object over time you use play()Example:

![Picture2](https://user-images.githubusercontent.com/115800139/235097411-4fed492f-d411-40d3-ac16-c19ec1355c95.png)

We scale the Circle object to double its size using circle.animate.scale(2) with linear rate function and 2 seconds duration.

### Changing Object Properties
You can change the properties of an object in Manim to create different effects. Example:

![Picture3](https://user-images.githubusercontent.com/115800139/235097623-d29a16d7-bc9d-446c-be1f-939f8e08c954.png)

A blue Circle object is created with 50% opacity, then shift(), set_color(), and set_fill() methods are used to animate the Circle's position, color, and opacity properties with the there_and_back rate function over a 2-second duration.

## Animating Text and LaTeX Equations
### Latex:
To animate equations Manim uses LaTex, a language unto itself. I won’t be providing a tutorial on how it works however below are some examples of LaTex:

### Equation:

![Picture4](https://user-images.githubusercontent.com/115800139/235097672-c30e2b84-c42d-4056-bcaf-eeefa23f3c77.png)

### Matrix:

![Picture5](https://user-images.githubusercontent.com/115800139/235097725-bcd675bf-74de-4f98-8f26-0ce675f4d947.png)

### Intergral:

![Picture6](https://user-images.githubusercontent.com/115800139/235097790-42f97ca7-0616-47aa-9ca7-e91258addb0d.png)

### Greek symbols

![Picture7](https://user-images.githubusercontent.com/115800139/235097836-c58f72ad-519b-41ca-941f-c97e36f4f19a.png)

### Fraction

![Picture8](https://user-images.githubusercontent.com/115800139/235097889-c200bdd1-cd28-4c2e-b12e-bd6e6d74fed3.png)

## Animating text and LaTeX equations in Manim.

### Text:
The Text object is used to add text to a scene. Example:

![Picture9](https://user-images.githubusercontent.com/115800139/235097962-ee20ade5-ad7f-4c7e-95cd-bdc5d2167cdc.png)

We created a Text object with the example of "Hello World!" and then used the Write to animate it.


### Text Properties: 
We can change various properties of a Text object like position, color, opacity, etc. 

![Picture10](https://user-images.githubusercontent.com/115800139/235097998-6dc0604a-3720-4d74-a6d4-c9f31a6be6c8.png)

A red Text object is created with "Hello World!" and moved to the top edge of the screen. The object is animated by shifting it down, scaling it up, and changing its color to blue.


### LaTeX Equations:
Manim has great support for LaTeX equations. Example:

![Picture11](https://user-images.githubusercontent.com/115800139/235098029-d2b54999-2bb8-42cd-97d3-6c08e88afbec.png)

We created a MathTex object with the LaTeX equation.

![Picture12](https://user-images.githubusercontent.com/115800139/235098077-25797d94-5e67-4841-ada3-517aea09ce5b.png)

Then used Write to animate it.

### Equation Properties: 
We can change various properties of a MathTex object like position, color, opacity, etc. Example:

![Picture13](https://user-images.githubusercontent.com/115800139/235098120-0712bc71-66a7-4c56-b48c-0cd6db99f441.png)

Above we created a MathTex object with the LaTeX equation. 

![Picture14](https://user-images.githubusercontent.com/115800139/235098151-44ae146e-b617-447e-8efd-4c64b539d20b.png)

The equation text object with yellow color is moved to the top edge of the screen using the to_edge method. The animation scales the object by a factor of 2 and changes its color to red.


## Advanced concepts


The AnimationGroup is used to animate multiple objects simultaneously. You create a list of the objects you want to animate, and then pass the list and the desired animation to an instance of AnimationGroup. Example:

![Picture15](https://user-images.githubusercontent.com/115800139/235098180-c9cd2114-8fe7-4428-85a8-ae72f6ce6a07.png)

We created a circle and a square, then AnimationGroup and pass the objects (circle and square) and the animation (Create) as arguments. Finally, play the animation using self.play(group).


Using the Transform class for smoothly transitioning between different object configurations:
Transform class enables smooth object transitions. Create initial and final objects, pass them to Transform instance. Example:

![Picture16](https://user-images.githubusercontent.com/115800139/235098230-4932f175-14dc-49ac-8a62-f71e08ae31b2.png)

Create a circle and square, create initial animation to create the circle, wait using self.wait(), then Transform animation to transform circle into square.

Using Easing Functions to Control the Motion of Objects
Transform class smoothly transitions between different object configurations. To use, create the initial and final objects, then pass them to an instance of Transform. Example:

![Picture17](https://user-images.githubusercontent.com/115800139/235098304-3b2f2c8f-5301-4a48-88d9-e440e999f50f.png)

Create a circle, animate it with several transformations using the there_and_back easing function for smooth back-and-forth motion.


##Data visualization

Manim is a powerful tool for creating animated visualizations from graph plotting, customization, and animated scatterplots to histograms.

### Plotting graphs and charts with Manim:
To plot graphs, create a scene and instantiate an Axes object, which represents Cartesian axes. Use x_range and y_range to specify axis ranges and customize their appearance with x_axis_config and y_axis_config.

![Picture18](https://user-images.githubusercontent.com/115800139/235098354-ee2d01de-da0a-4c24-a4a4-605e0f918052.png)

Create an Axes object with x and y-axis ranges of [-5, 5]. Customize axis appearance and plot a curve using a lambda function. Add the Axes object, axis labels, and curve to the scene.


### Moving Camera:
In the following I will explain the moving camera example by Manim. 


### Define the Following GraphCamera class
Now define the FollowingGraphCamera class. This inherits from MovingCameraScene, which provides the basic functionality for moving the camera around the scene.


![Picture19](https://user-images.githubusercontent.com/115800139/235098403-a6fa75bb-cb65-472b-be8c-854285b2ef12.png)

### Save the initial camera state
Before we start animating the camera, save its initial state so we can restore it later. Do this using the save_state() method of the camera's frame object.

![Picture20](https://user-images.githubusercontent.com/115800139/235098453-2c48afbb-f9fa-4d9c-aaae-a7aa0214e76f.png)

### Axes and the curve
To create axes and a curve, we use the Axes class to create the axes and the plot() method to plot the curve. In this example, the sin() function is plotted over the range [0, 3*PI]


![Picture21](https://user-images.githubusercontent.com/115800139/235098541-4ffd786d-e1a0-4700-b316-3cf4dca3a24f.png)

### Dots based on the graph
We can now create dots based on the graph that we will use to animate the camera. In this example, we will create three dots: one that will move along the curve, and two that will mark the endpoints of the curve.

![Picture22](https://user-images.githubusercontent.com/115800139/235098580-e7d771f8-4549-4df8-9a00-f1355bf54cbd.png)

### Add the objects to the scene.
We can now add the axes, curve, and dots to the scene using add().

![Picture23](https://user-images.githubusercontent.com/115800139/235098634-bc2b537c-e652-4211-ae71-ccc73e0e94d6.png)


### Move the camera to the starting point.
Before we start animating the camera, we need to move it to the starting point of the animation. In this example, we will move the camera to the position of the first dot.

![Picture24](https://user-images.githubusercontent.com/115800139/235098690-7fa26fc3-740b-4d60-8b24-7a2a52c837de.png)


### Define the updater function.
To animate the camera along the curve, an updater function needs to be defined that updates the camera's position based on the moving dot's position. The add_updater() method of the camera's frame object can be used to accomplish this. 


![Picture25](https://user-images.githubusercontent.com/115800139/235098744-732adaf0-e107-48d4-a53d-b5eed8b89d26.png)


### Move the dot along the curve
Use the MoveAlongPath animation to move the dot along the curve. We can pass in the moving_dot object, the graph object, and a rate_func (in this case, linear) to control the speed of the animation.


![Picture26](https://user-images.githubusercontent.com/115800139/235098780-839da45b-8f8d-4b2f-8973-6973a3c1221c.png)



### Remove the updater
Once the animation is complete, we need to remove the updater function using the remove_updater() method of the camera's frame object.


![Picture27](https://user-images.githubusercontent.com/115800139/235098826-f3d55e06-4b0d-4f32-b71d-6bdc3a01fa4f.png)


### Restore the camera state
We can restore the camera's state to its initial state using the Restore() animation, passing in the camera.frame object.

![Picture28](https://user-images.githubusercontent.com/115800139/235098920-e5fa5ccb-9000-4c15-b3a9-0fcc3acd4368.png)




## Tips:
### Creating animations with custom frame rates and resolutions
Default: Manim uses a frame rate of 60 frames per second and a resolution of 1080p. You can customize these settings to suit your needs.
To set a custom frame rate add the -r or --frame_rate flag to the command line when running Manim. For example, to set a frame rate of 30 fps, you can run:

![Picture29](https://user-images.githubusercontent.com/115800139/235099011-36537393-bb0d-48a0-919f-96ab1843783a.png)

To set a custom resolution, you can add the -p or --pixel_height flag to the command line when running Manim. For example, to set a resolution of 720p (1280x720 pixels), you can run:

![Picture30](https://user-images.githubusercontent.com/115800139/235099074-ac7d910d-0285-4ce1-ba57-657c213a1ae0.png)

### Using Positional  constants to position objects	
Manim's constants UP, DOWN, LEFT, and RIGHT are useful for layout and object alignment. Example: Use LEFT and RIGHT constants to position two text objects side-by-side with space between them

![Picture31](https://user-images.githubusercontent.com/115800139/235099146-c9cb1c1e-ad5a-4a91-a804-3ab51e843609.png)

Use move_to to position text objects relative to the screen by multiplying LEFT and RIGHT constants by 4 to move them left and right of the screens centre.


### Creating custom shapes and paths using Bézier curves and other curve types
Manim provides several built-in curve types, such as Line, Arc, and Circle. However, you may sometimes need to create custom shapes and paths using Bézier curves or other curve types.

To create a Bézier curve use the CubicBezier, taking four control points as arguments:

![Picture32](https://user-images.githubusercontent.com/115800139/235099195-8eb4d4e4-9acb-4d35-a928-3d182383d136.png)

Create Bézier curve using four control points - UP, 2 * RIGHT, 2 * LEFT, and DOWN. CubicBezier returns a Path object for animation using Create method. Manim has other curve types, including QuadraticBezier and ArcBetweenPoints.


## Using the VGroup & Mobject.add() 

VGroup class for grouping multiple Mobjects (Mathematical objects) together. 
To create a VGroup, pass the Mobjects to be grouped as arguments:

![Picture33](https://user-images.githubusercontent.com/115800139/235099230-0551f5fd-af42-40b1-97e0-6bcfcccf6381.png)

The example creates a horizontal group of a Circle and a Square using VGroup. Then, the group is rotated 90 degrees.

Using the Mobject.add() to add new objects to an existing group:

![Picture34](https://user-images.githubusercontent.com/115800139/235099279-7075cff7-42df-431c-a123-54629603c952.png)

In this example, a Triangle is added to the existing group using the add method and positioned next to the square using the next to method.






