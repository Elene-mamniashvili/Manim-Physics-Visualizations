from manim import *
import numpy as np

class FaradaysLaw(Scene):
    def construct(self):
        # 1. Labels
        title = Text("Faraday's Law of Induction", font_size=36).to_edge(UP)
        equation = Text("∇ × E = -∂B / ∂t", font_size=40, color=PURPLE).next_to(title, DOWN)
        self.add(title, equation)

        # 2. The Coil (Stationary)
        wire_loop = Circle(radius=1.5, color=WHITE, stroke_width=6)
        self.add(wire_loop)

        # 3. The Bar Magnet
        magnet_body = Rectangle(width=2.0, height=0.8, color=GRAY).set_fill(GRAY, opacity=0.5)
        n_label = Text("N", color=RED, font_size=24).shift(RIGHT * 0.5)
        s_label = Text("S", color=BLUE, font_size=24).shift(LEFT * 0.5)
        magnet = VGroup(magnet_body, n_label, s_label)
        
        # Start at the LEFT but with a massive buffer (Halfway to the edge)
        magnet.to_edge(LEFT, buff=3.5) 

        # 4. Induction Logic
        def get_induction_factor():
            x = magnet.get_center()[0]
            # Adjusted for the shorter, centered movement
            return -x * np.exp(-(x**2) / 1.0)

        # 5. THE ARROWS (Induced Electric Field)
        induced_field = always_redraw(lambda: ArrowVectorField(
            lambda p: np.array([-p[1], p[0], 0]) * get_induction_factor(),
            x_range=[-2, 2, 0.5],
            y_range=[-2, 2, 0.5],
            colors=[YELLOW_A, YELLOW_E]
        ).set_opacity(min(abs(get_induction_factor()) * 5, 1)))

        # 6. HUD: Flux Change Counter
        flux_info = always_redraw(lambda: VGroup(
            Text("Flux Change (dB/dt):", font_size=20),
            Text(f"{get_induction_factor():.2f}", font_size=24, color=YELLOW)
        ).arrange(RIGHT).to_edge(DOWN, buff=0.5))

        # 7. Animation Sequence
        self.add(induced_field, flux_info)
        self.play(FadeIn(magnet))
        self.wait(1)

        # Move to the RIGHT edge but stop halfway (buff=3.5)
        self.play(
            magnet.animate.to_edge(RIGHT, buff=3.5),
            run_time=4,
            rate_func=linear
        )
        self.wait(1)

        # Move back to the LEFT halfway point
        self.play(
            magnet.animate.to_edge(LEFT, buff=3.5),
            run_time=3,
            rate_func=smooth
        )
        
        self.play(Indicate(equation, scale_factor=1.2))
        self.wait(2)