from manim import * 

class Gauss(ThreeDScene):
    def construct(self):
        # Create title and subtitle
        title = Tex("Introduction to the Gaussian Integral via Polar Coordinates")
        subtitle = Tex("Produced with Manim")
        title.set_color_by_gradient(BLUE, ORANGE)
        subtitle.set_color_by_gradient(ORANGE,BLUE)
        title.next_to(subtitle, direction=UP)
       
       #Define the quote, specify the colour of "sublime science"
        quote = Tex("``The enchanting charms of this ", "sublime science", " reveal only to those who have the courage to go deeply into it.`` - Carl Friedrich Gauss ", font_size=30)
        quote.set_color_by_tex("sublime science", WHITE)

        # Show title and subtitle
        self.play(Write(title))
        self.wait(1)
        self.play(Write(subtitle))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        self.wait(1)
       
        # Play the initial quote animation
        self.play(Write(quote), run_time=7)

        # Fade the words "sublime science" from white to blue
        self.play(
            quote[1].animate.set_color(BLUE),
            run_time=2
        )

        # Wait a moment before finishing
        self.wait()

        # Create new title and formula
        title = Tex("A Brief Introduction")
        formula = MathTex(r"f(x)=",
                          r"\int_{-\infty}^{\infty} e^{-x^2} dx"
                          )
        equation = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2} dx")
       
       # Create a box around the formula
        box = SurroundingRectangle(formula[1], buff=0.1)
       
       # Transform quote to title
        self.play(Transform(quote,title))
        self.wait()

        # Move title to top
        title_target = title.copy().to_edge(UP)
        self.play(Succession(
            FadeOut(quote),
            title.animate.move_to(title_target)
        ))
       
       # Show formula and box
        self.play(Write(formula))
        self.play(Create(box))
        self.play(FadeOut(box))
        self.wait(1)

        # Fade out title
        self.play(FadeOut(title))
        self.wait()

        # Transform formula to equation
        equation.to_corner(UP + LEFT)
        self.play(Transform(formula, equation))
       
             
        self.wait()
       
        # Add grid and equation to scene
        grid = NumberPlane()
        self.add(grid, equation)
        self.play(
            Create(grid, run_time=3, lag_ratio=0.1),
        )
       
       # Create a graph of the Gaussian function
        equation2 = MathTex("f(x,y) = e^{-(x^2+y^2)}")
        equation2.to_corner(UP + LEFT)
       

       
        def gaussian(x):
            return np.exp(-x**2)
        graph = FunctionGraph(gaussian, x_range=[-7, 7], color=BLUE) # adjust the x_range argument
       
       # Show the graph
        self.play(Create(graph))
        self.wait()
       #Fade out the formula
        self.play(FadeOut(formula))

        # Show equation2
        self.play(FadeOut(equation))
        self.play(Write(equation2))
       

        # Fade out the graph
        self.play(FadeOut(graph))
       
       # Create 3D axes and surface
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-1, 1, 0.5],
        )

        surface = Surface(
            lambda u, v: np.array([
                u,
                v,
                np.exp(-u**2 - v**2)
            ]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.8,
            checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(20, 20)
        )
        self.wait(2)
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        self.add_fixed_in_frame_mobjects(equation2)
        self.play(Transform(grid, axes))
        self.wait(1)
       
       #Rotate Camera around graph
        self.play(Create(surface), runtime=3)
        self.begin_ambient_camera_rotation(
            rate=PI /10, about="theta"
        )
        self.wait(4)
        self.stop_ambient_camera_rotation()

        #Fade out grid,axes and equation 2
        self.play(FadeOut(grid), FadeOut(axes), FadeOut(equation2))
       
       
        # Fade Out Surface
        self.play(FadeOut(surface))
       
        #Return camera to default
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
       
        #Define all steps of the proof
        eq1 = MathTex(r"I = \int_{-\infty}^{\infty} e^{-x^2} dx")
        eq2 = MathTex(r"I^2 = \int_{-\infty}^{\infty} e^{-x^2} dx \int_{-\infty}^{\infty} e^{-y^2} dy")
        eq3 = MathTex(r"I^2 = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} e^{-(x^2+y^2)} dx dy")
        eq4 = MathTex(r"I^2 = \int_{0}^{2\pi} \int_{0}^{\infty} e^{-r^2} r dr d\theta")
        eq5 = MathTex(r"I^2 = \pi \int_{0}^{\infty} e^{-r^2} r d(r^2)")
        eq6 = MathTex(r"I^2 = \pi \int_{0}^{\infty} e^{-u} du")
        eq7 = MathTex(r"I = \sqrt{\pi}")

        # Step 1: Square I
        self.play(Write(eq1))
        self.wait(2)
        self.play(Transform(eq1, eq2))
        self.wait(2)
        self.play(Transform(eq1, eq3))
        self.wait(2)

        # Step 2: Change to polar coordinates
        self.play(Transform(eq1, eq4))
        self.wait(2)

        # Step 3: Evaluate theta integral
        self.play(Transform(eq1, eq5))
        self.wait(2)

        # Step 4: Evaluate r integral
        self.play(Transform(eq1, eq6))
        self.wait(2)

        # Step 5: Evaluate the result
        self.play(Transform(eq1, eq7))
        self.wait(2)
