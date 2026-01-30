from manim import *
import numpy as np

class SineAmplitudeProjection(Scene):
    def construct(self):
        # 1. Configuration
        RADIUS = 1.8  
        t = ValueTracker(0)
        
        circle = Circle(radius=RADIUS, color=WHITE).shift(LEFT * 3)
        # Center of the circle for the radius line
        circle_center = circle.get_center()

        axes = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-2, 2, 1], 
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True}
        ).shift(RIGHT * 3.5)

        # 2. Objects
        dot_on_circle = always_redraw(lambda: Dot(color=YELLOW).move_to(
            circle.point_at_angle(t.get_value())
        ))

        # NEW: The Radius Line (The "DNA")
        radius_line = always_redraw(lambda: Line(
            start=circle_center,
            end=dot_on_circle.get_center(),
            color=YELLOW,
            stroke_width=4
        ))

        moving_dot_on_axes = always_redraw(lambda: Dot(color="#00FFFF").move_to(
            axes.c2p(t.get_value(), RADIUS * np.sin(t.get_value()))
        ))

        h_line = always_redraw(lambda: DashedLine(
            start=dot_on_circle.get_center(), 
            end=moving_dot_on_axes.get_center(), 
            color=GRAY, 
            stroke_opacity=0.5
        ))

        sine_graph = always_redraw(lambda: axes.plot(
            lambda x: RADIUS * np.sin(x), 
            color="#00FFFF", 
            x_range=[0, max(0.001, t.get_value())]
        ))

        # 3. Display
        self.add(circle, axes, dot_on_circle, moving_dot_on_axes, h_line, sine_graph, radius_line)
        self.play(t.animate.set_value(2 * PI), run_time=7, rate_func=linear)
        self.wait(2)