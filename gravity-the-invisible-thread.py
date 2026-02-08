from manim import *
import numpy as np

class GravitationalField(Scene):
    def construct(self):
        # --- 1. Setup the Environment ---
        # The stationary Sun (Massive Body)
        # Created with a core and a subtle outer 'glow' circle
        sun_core = Dot(radius=0.5, color=YELLOW)
        sun_glow = Circle(radius=0.7, color=YELLOW, fill_opacity=0.3, stroke_width=0)
        sun = VGroup(sun_glow, sun_core)
        
        sun_label = Text("Mass M", font_size=24).next_to(sun, UP)
        
        # The moving Planet
        planet = Dot(radius=0.2, color=BLUE)
        planet.move_to(RIGHT * 6 + UP * 3) # Starting position
        
        # --- 2. The Dynamic Influence Field ---
        # A circular ripple that gets thicker/brighter as the planet nears the center
        field_circle = always_redraw(lambda: Circle(
            radius=np.linalg.norm(planet.get_center()),
            stroke_width=interpolate(1, 8, 1/(np.linalg.norm(planet.get_center()) + 0.1)),
            stroke_opacity=interpolate(0.1, 0.6, 1/(np.linalg.norm(planet.get_center()) + 0.1)),
            color=YELLOW
        ).move_to(sun.get_center()))

        # The connecting force vector pointing to the sun
        force_arrow = always_redraw(lambda: DoubleArrow(
            start=planet.get_center(),
            end=sun.get_center(),
            buff=0.1,
            color=YELLOW,
            stroke_width=interpolate(1, 10, 2/(np.linalg.norm(planet.get_center()) + 0.1)),
            tip_length=0.15
        ))

        self.add(sun, sun_label, field_circle, force_arrow, planet)
        self.play(FadeIn(sun, sun_label))
        self.wait(1)

        # --- 3. The Interaction Animation ---
        # Path: Approach, swoop close, then head back out
        points = [
            LEFT * 3 + UP * 1, 
            LEFT * 1 + DOWN * 2, 
            RIGHT * 4 + DOWN * 1, 
            RIGHT * 6 + UP * 2
        ]
        
        for point in points:
            self.play(
                planet.animate.move_to(point),
                run_time=2,
                rate_func=smooth
            )

        self.wait(2)