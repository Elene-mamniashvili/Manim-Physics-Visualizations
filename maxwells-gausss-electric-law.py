from manim import *
import numpy as np

class GaussLawElectricity(Scene):
    def construct(self):
        # 1. Title and Equation
        title = Text("Gauss's Law for Electricity", font_size=36).to_edge(UP)
        equation = Text("∇ · E = ρ / ε₀", font_size=40, color=ORANGE).next_to(title, DOWN)
        self.add(title, equation)

        # 2. Define the Electric Field (Point Charge)
        charge_pos = RIGHT * 2 
        
        def electric_field(p):
            r = p - charge_pos
            mag = np.linalg.norm(r)
            if mag < 0.1: return np.zeros(3) # Prevent infinite values at center
            # 1/r^2 falloff for physical accuracy
            return (r / (mag**3)) * 3

        # 3. Create Moving Streamlines (Replacing static arrows)
        # These will continuously move to show the "faucet" effect
        stream_lines = StreamLines(
            electric_field, 
            x_range=[-7, 7], y_range=[-4, 4],
            stroke_width=3,
            color=RED_A,
            max_anchors_per_line=30
        )

        # 4. Charge and Gaussian Surface
        charge = Dot(point=charge_pos, color=RED, radius=0.2)
        charge_label = Text("+", color=WHITE).scale(0.8).move_to(charge)
        
        gauss_circle = Circle(radius=1.5, color=WHITE, stroke_width=4)
        gauss_circle.set_fill(WHITE, opacity=0.1).move_to(LEFT * 3)

        # 5. Flux Logic
        def get_flux_value():
            dist = np.linalg.norm(gauss_circle.get_center() - charge_pos)
            return "1.00" if dist < 1.5 else "0.00"

        flux_label = always_redraw(lambda: VGroup(
            Text("Net Flux:", font_size=24),
            Text(get_flux_value(), font_size=24, color=YELLOW)
        ).arrange(RIGHT).next_to(gauss_circle, UP))

        # 6. Animation Sequence
        self.add(charge, charge_label)
        self.play(stream_lines.create(), run_time=2)
        
        # Start the "Flowing" animation
        stream_lines.start_animation(warm_up=True, flow_speed=1.5)
        self.add(stream_lines)

        self.play(Create(gauss_circle), FadeIn(flux_label))
        self.wait(1)

        # Move circle to surround the charge
        # You will see the streamlines "flowing" through the circle
        self.play(gauss_circle.animate.move_to(charge_pos), run_time=4)
        self.wait(2)

        # Move circle away
        self.play(gauss_circle.animate.move_to(LEFT * 3 + DOWN * 1), run_time=3)
        self.wait(2)