from manim import *

class SineProjection(Scene):
    def construct(self):
        # 1. Setup with hex colors for reliability
        neon_color = "#00FFFF" 
        
        axes = Axes(
            x_range=[0, 7, 1], 
            y_range=[-1.5, 1.5, 1], 
            x_length=7,
            axis_config={"include_tip": True}
        ).to_edge(RIGHT, buff=0.5)
        
        circle = Circle(radius=1, color=WHITE).to_edge(LEFT, buff=1.0)
        
        dot_on_circle = Dot(color=neon_color).move_to(circle.get_right())
        rolling_dot = Dot(color=neon_color).move_to(axes.c2p(0, 0))
        
        projection_line = always_redraw(lambda: Line(
            dot_on_circle.get_center(), 
            rolling_dot.get_center(), 
            stroke_width=2, 
            stroke_opacity=0.5,
            color=WHITE
        ))
        
        wave_trace = TracedPath(
            rolling_dot.get_center, 
            stroke_color=neon_color, 
            stroke_width=5
        )
        
        self.add(axes, circle, projection_line, wave_trace)
        
        # 4. The Animation
        self.play(
            Rotate(dot_on_circle, angle=2*PI, about_point=circle.get_center()),
            rolling_dot.animate.move_to(axes.c2p(2*PI, 0)),
            UpdateFromFunc(rolling_dot, lambda d: d.set_y(dot_on_circle.get_y())),
            run_time=6,
            rate_func=linear
        )
        self.wait(2)