# Learning Log
## What is Manim?

## Manims Versions

### Manim Community Edition (CE)
This is the version of Manim that is actively maintained and developed by the Manim community. It is the most up-to-date and feature-rich version of Manim and includes many improvements and additions to the original version created by Grant. Manim Community Edition is open-source and available on GitHub.

### Manim GL
Manim GL is a new version of Manim that is currently in development. It is a complete rewrite of the original Manim codebase and aims to improve performance, flexibility, and ease of use. Manim GL uses the OpenGL graphics library, which allows for hardware acceleration and faster rendering. It also includes a more user-friendly interface and better documentation. Manim GL is still in development, but it promises to be a significant improvement over the original Manim.

Due to the community-based nature of Manim (CE) and its more stable nature I have chosen to learn this version. 

## Why Manim
Manim's animations have not only made it easier for me to comprehend difficult mathematical ideas, but they've also made studying more engaging and enjoyable. 

## Goal  
Produce an animation which displays the proof of the Gaussian integral in a visual an intuitive manner with Manim.

## Week 1

### (20/03/23)

 I decided to dive into the world of Manim and began by researching the various versions available. I spent some time exploring the Manim community website and familiarized myself with the basic file structure of a Manim project as well as some example projects. I also watched a few introductory videos on Manim. 
 
 ### (25/03/23)
 
 I installed Manim, something which turned out to be surprisingly difficult requiring various dependencies and installations to get right. I then created my first Manim script by following the example provided in the documentation. It was a simple animation that moved a circle across the screen. I was pleasantly surprised to see how easy it was to create such animations with Manim. 
 
 ## Week 2
 
 ### (28/03/23)
 
 I learned how to animate text using the MathTex and Tex classes in Manim. I discovered that these classes could be used to render mathematical expressions and equations in various fonts and sizes. Luckily, I’ve already had experience with LaTex so learning using it wasn’t too bad. I explored the various text alignment options available in Manim, such as left, centre, and right alignment. I also learned how to use the TextAlign class to align multiple lines of text.
 
 ### (30/03/23)
 
 I spent some time creating a few text animations, such as typing out a sentence character by character and having it disappear after a few seconds. I also learned how to use the FadeIn and FadeOut classes to create smooth transitions between different animations. I explored the various text alignment options available in Manim, such as left, centre, and right alignment. I also learned how to use the TextAlign class to align multiple lines of text.
 
 ### (01/04/23)
 
 I experimented with adding various effects to my text animations, such as scaling, rotating, and pulsing. I also learned how to use the Play command to execute multiple animations in sequence.
 
 
 ## Week 3
 
 ### (04/04/23)
 I learned how to create shapes in Manim using the Circle, Square, and Polygon classes. I also discovered the various options available for changing the colour, stroke width, and opacity of these shapes. I also learnt how to use the Transform class to smoothly transform one shape into another.
 
 ### (08/04/23)
 I explored the various transformation methods available in Manim, such as applying shear, stretch, and reflection transformations to shapes. I also learned how to use the Succession class to apply multiple transformations in sequence. I’m not sure why but when doing this I kept running into crashes and it took me far longer than I had expected to get the basics of this down. A lot of issues stemmed from the tutorials I used using older versions of Manim, using names which have since been changed.
 
 ### (09/04/23)
 
 I experimented with creating more complex animations by combining shape and text animations. For example, I created an animation where a polygon was drawn and then filled with text. This took forever to get right, had trouble positioning the text in the right place. Also keeping track of objects was difficult once I had Transformed the objects. The last thing I did was try animating some Bezier curves.
 
 ## Week 4
 ### (12/04/23) 
 
 I learned how to use the CoordinateSystem class in Manim to create coordinate axes and grids. I also discovered the various options available for customizing the appearance of these coordinate systems. I also tired creating coordinate system animations, such as animating a point moving along a curve or plotting a function on a graph. I also learned how to use the Arc class to create arcs and angles in a coordinate system.
 
 ### (16/04/23)
 I explored the various mathematical functions available in Manim, such as the sine and cosine. I also learned how to use the Parametric Function class to plot parametric equations. I experimented with combining coordinate system animations with shape and text animations. Example: I created an animation where a graph was drawn, and a point moved along the graph while a label indicating the value of the function was displayed.
 
 ## Week 5 
 ### Retrosective Note
 I Spent most of the next 2 weeks animating the Gaussian Integral proof via polar coordinates. The aim was to combine a lot of what I learnt into a meaningful animation, not just an example of what Manim can do.
 
 ### (18/04/23)
 I learned how to use the Camera class in Manim to control the camera movement and perspective of an animation. I discovered the various methods available for panning, zooming, and rotating the camera. 
 
 #### Retrsoepcitve Note:
 This would turn out quite useful as I used it to move about the 3d graph I would create.
 
 ### (20/04/23)
 I spent most of today animating the proof for the gaussian integral. I did this by writing out each stage of the integral, breaking it down into 7 equations and then using transforms to convert them into one another. 
 
### (21/04/23)
I learnt how to create 3D Graphs and surfaces on them, this was surprisingly not too bad as the documentation for this on Manim was very comprehensive, with a very handy example. This was pretty handy I spent some time trying to animate f(x,y) = e^-(x^2+y^2) , a 3 dimensional graph.

### (22/04/23)
I’d rather counter intuitively animated the 3d graph first so I spent today animating what was supposed to be the easier graph of just f(x) = e^(-x^2), but I kept running into different errors ranging from objects having been renamed since older versions, to objects no aligning properly on the screen.

### (23/04/23)
Spent today doing the intro for the tutorial, this including the opening slide, a quote on maths from Gauss then the actual integral itself. This was straightforward, with the only problem being keeping track of all the objects as the where transformed, which became very fustrating when all the animations kept playing at once and wouldnt fade out.

## Week 6

### (24/04/23)
Spent today putting the animation all together and amending the timings, took a surprisingly long time since I had to contend with all the overlaps on my first try. 

### (25/04/23)
Spent today reviewing everything I had done over the past 6 weeks, mainly going over my animation for the Gaussian Integral and seeing if there was anything else I could tweak to improve upon it. I also spent a while having to remove as many words from my Learning Log as possible to get it below the word limit.

##Conclusion 

Overall, my experience with Manim was extremely positive, and I found the library to be very flexible and powerful. While there was a learning curve, I found that the official documentation was very helpful, with my biggest issue is that a lot of solutions to problems I had on Stack Overflow or tutorials on the internet using outdated versions of the code.  I wish I spent more time doing my own examples and incorporating I wish I had added more complexity to, I kept wanting to add more features from Manim, even if it made the substance/visualization too busy.

### Things To Explore: 
* Adding Audio with Manim \
* Trying ManimGL \ 
* Project around trigonometric functions 


 
