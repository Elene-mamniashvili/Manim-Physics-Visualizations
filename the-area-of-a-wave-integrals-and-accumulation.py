from manim import *
import numpy as np

class IntegralAccumulation(Scene):
    def construct(self):
        # 1. Setup
        title = Text("The Integral: Area as Accumulation", font_size=32).to_edge(UP)
        axes = Axes(
            x_range=[0, 7, 1], y_range=[-1.5, 1.5, 1],
            axis_config={"color": BLUE_D, "include_tip": False},
            x_length=10, y_length=4
        ).shift(DOWN * 0.5).set_z_index(5)

        cos_curve = axes.plot(lambda x: np.cos(x), color=PURPLE).set_z_index(4)
        
        # 2. Label
        # 'UR' keeps it above the curve, 'shift(0.8 * LEFT)' pulls it back
        cos_label = Text("v(t) = cos(t)", color=PURPLE, font_size=22)
        cos_label.next_to(cos_curve, UR, buff=0.1).shift(0.8 * LEFT) 

        # 3. Inscribed Logic (Split sampling for perfect fit)
        n_tracker = ValueTracker(10)
        
        def get_inscribed_rects():
            n = n_tracker.get_value()
            dx = PI / n
            pos = axes.get_riemann_rectangles(
                cos_curve, x_range=[0, PI/2], dx=dx, 
                input_sample_type="right", fill_opacity=0.5, stroke_width=0
            ).set_color("#00FFFF")
            
            neg = axes.get_riemann_rectangles(
                cos_curve, x_range=[PI/2, PI], dx=dx, 
                input_sample_type="left", fill_opacity=0.5, stroke_width=0
            ).set_color("#FF5252")
            return VGroup(pos, neg)

        rects = always_redraw(get_inscribed_rects)

        # 4. Animation Sequence
        self.play(Write(title))
        self.play(Create(axes), Create(cos_curve), Write(cos_label))
        self.play(Create(rects))
        self.wait(1)
        
        # Limit Process
        self.play(n_tracker.animate.set_value(120), run_time=5, rate_func=smooth)
        self.wait(0.5)

        # 5. Instant Swap 
        pos_area = axes.get_area(cos_curve, x_range=[0, PI/2], color="#00FFFF", opacity=0.4)
        neg_area = axes.get_area(cos_curve, x_range=[PI/2, PI], color="#FF5252", opacity=0.4)
        final_fill = VGroup(pos_area, neg_area)
        
        result_text = Text("Total Area = 0.0", font_size=24, color="#00FFFF").next_to(axes, DOWN)
        
        # Immediate removal and addition
        self.remove(rects)
        self.add(final_fill)
        self.play(Write(result_text))
        
        self.wait(3)