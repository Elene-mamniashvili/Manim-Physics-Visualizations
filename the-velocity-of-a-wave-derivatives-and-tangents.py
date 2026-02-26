from manim import *
import numpy as np

class SineTangentExtended(Scene):
    def construct(self):
        # 1. Setup Extended Axes
        axes = Axes(
            x_range=[0, 10, 1], # X goes to 10
            y_range=[-2, 2, 1],
            axis_config={"include_tip": True},
            x_length=11,
            y_length=5
        ).to_edge(DOWN)
        
        x_label = Text("x", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("y", font_size=24).next_to(axes.y_axis, UP)

        # 2. The Wave (plotted to 9.5)
        sine_curve = axes.plot(lambda x: np.sin(x), x_range=[0, 9.5], color=BLUE)
        
        # 3. Tracker
        t = ValueTracker(0)

        # 4. Moving Tangent Line & Label
        # We group them so the text stays attached to the line
        def get_tangent_group():
            val = t.get_value()
            y = np.sin(val)
            slope = np.cos(val)
            p1 = axes.c2p(val - 1, y - slope)
            p2 = axes.c2p(val + 1, y + slope)
            
            line = Line(p1, p2, color=YELLOW)
            label = Text("Tangent", color=YELLOW, font_size=20).next_to(line, UP, buff=0.1)
            
            return VGroup(line, label)

        tangent_group = always_redraw(get_tangent_group)

        # 5. Moving Slope Triangle (Derivative Visual)
        def get_slope_triangle():
            val = t.get_value()
            y = np.sin(val)
            slope = np.cos(val)
            
            p_start = axes.c2p(val, y)
            p_corner = axes.c2p(val + 0.5, y)
            # 0.001 buffer prevents crash at peaks
            p_end = axes.c2p(val + 0.5, y + (0.5 * slope) + 0.001) 
            
            run_line = Line(p_start, p_corner, color=GREEN, stroke_width=4)
            rise_line = Line(p_corner, p_end, color=RED, stroke_width=4)
            
            return VGroup(run_line, rise_line)

        slope_triangle = always_redraw(get_slope_triangle)

        # 6. Derivative Counter
        slope_title = Text("Derivative:", font_size=24).to_corner(UL)
        slope_val_text = always_redraw(lambda: 
            Text(f"{np.cos(t.get_value()):.2f}", color=RED, font_size=24)
            .next_to(slope_title, RIGHT)
        )

        dot = always_redraw(lambda: 
            Dot(color=WHITE).move_to(axes.c2p(t.get_value(), np.sin(t.get_value())))
        )

        # 7. Animation
        self.add(axes, x_label, y_label, sine_curve)
        self.play(
            FadeIn(tangent_group), 
            FadeIn(dot), 
            FadeIn(slope_triangle),
            Write(slope_title)
        )
        self.add(slope_val_text)

        # Animate to 8.5 (well past 6.28)
        self.play(
            t.animate.set_value(8.5), 
            run_time=12,
            rate_func=linear
        )
        self.wait(2)