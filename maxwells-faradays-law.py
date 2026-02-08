from manim import *
import numpy as np

class FaradaysLaw(Scene):
    def construct(self):
        # 1. Title and Equation (LaTeX-free)
        title = Text("Faraday's Law of Induction", font_size=36).to_edge(UP)
        equation = Text("∇ × E = -∂B / ∂t", font_size=40, color=PURPLE).next_to(title, DOWN)
        self.add(title, equation)

        # 2. The Wire Loop (Stationary)
        wire_loop = Circle(radius=1.8, color=WHITE, stroke_width=6)
        wire_label = Text("Wire Loop", font_size=24).next_to(wire_loop, DOWN, buff=0.5)
        self.add(wire_loop, wire_label)

        # 3. The Bar Magnet
        magnet_body = Rectangle(width=2.5, height=1, color=GRAY).set_fill(GRAY, opacity=0.5)
        n_label = Text("N", color=RED).shift(RIGHT * 0.7)
        s_label = Text("S", color=BLUE).shift(LEFT * 0.7)
        magnet = VGroup(magnet_body, n_label, s_label)
        magnet.move_to(LEFT * 5)

        # 4. Induction Strength Logic
        def get_induction_factor():
            x = magnet.get_center()[0]
            # Strength peaks near the loop (x=0) and flips direction
            return -x * np.exp(-(x**2) / 1.5)

        # 5. The Induced Electric Field (Fixed VectorField call)
        # We define the field within a specific area using the 'VectorField' correctly
        induced_field = always_redraw(lambda: VectorField(
            lambda p: np.array([-p[1], p[0], 0]) * get_induction_factor(),
            # We don't use x_range here; VectorField fills the screen or we scale it
        ).scale(0.5).move_to(wire_loop)) 
        
        # Note: If you want to limit the area, we simply use the lambda logic 
        # to return zero vectors outside a certain radius.

        # 6. HUD: Flux Change Counter
        flux_info = always_redraw(lambda: VGroup(
            Text("dB/dt (Change):", font_size=20),
            Text(f"{get_induction_factor():.2f}", font_size=24, color=YELLOW)
        ).arrange(RIGHT).to_edge(DOWN, buff=0.5))

        # 7. Animation Sequence
        self.add(induced_field, flux_info)
        self.play(FadeIn(magnet))
        self.wait(1)

        # Move magnet through
        self.play(
            magnet.animate.move_to(RIGHT * 5),
            run_time=8,
            rate_func=linear
        )
        self.wait(1)

        # Move back
        self.play(
            magnet.animate.move_to(LEFT * 5),
            run_time=4
        )
        self.wait(2)