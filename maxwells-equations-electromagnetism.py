from manim import *
import numpy as np

class GaussLawMagnetism(Scene):
    def construct(self):
        # 1. Title and Equation
        title = Text("Gauss's Law for Magnetism", font_size=36).to_edge(UP)
        equation = Text("∇ · B = 0", font_size=40, color=BLUE).next_to(title, DOWN)
        self.add(title, equation)

        # 2. Define the Magnetic Dipole Field
        def dipole_field(p):
            x, y, z = p
            m = np.array([0, 1, 0]) # Magnetic moment pointing UP
            r = np.array([x, y, 0])
            r_mag = np.linalg.norm(r)
            if r_mag < 0.5: 
                return np.zeros(3)
            
            term1 = 3 * r * np.dot(m, r) / (r_mag**5)
            term2 = m / (r_mag**3)
            return (term1 - term2) * 0.5

        # Create the Vector Field
        field = ArrowVectorField(
            dipole_field, 
            x_range=[-7, 7], 
            y_range=[-4, 4],
            colors=[BLUE_E, BLUE_A]
        )
        
        # Create moving stream lines
        stream_lines = StreamLines(
            dipole_field, 
            x_range=[-7, 7], 
            y_range=[-4, 4],
            stroke_width=2,
            max_anchors_per_line=30
        )

        # 3. Create the Gaussian Surface 
        gauss_circle = Circle(radius=1.5, color=WHITE, stroke_width=4)
        gauss_circle.set_fill(WHITE, opacity=0.1)
        
        flux_label = always_redraw(lambda: VGroup(
            Text("Net Flux:", font_size=24),
            Text("0.00", font_size=24, color=GREEN)
        ).arrange(RIGHT).next_to(gauss_circle, UP))

        # 4. Animation Sequence
        self.add(field)
        self.play(stream_lines.create(), run_time=2)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=True, flow_speed=1.5)

        self.play(Create(gauss_circle), FadeIn(flux_label))
        self.wait()

        # 5. Move the surface around the field
        # Move to North Pole
        self.play(gauss_circle.animate.shift(UP * 2), run_time=3)
        self.wait(1)
        
        # Move to South Pole
        self.play(gauss_circle.animate.shift(DOWN * 4), run_time=3)
        self.wait(1)
        
        # Move to the Side
        self.play(gauss_circle.animate.shift(RIGHT * 4 + UP * 2), run_time=3)
        self.wait(2)

        # 6. Final Highlight
        explanation = Text(
            "Lines entering = Lines leaving", 
            font_size=24, 
            color=YELLOW
        ).to_edge(DOWN, buff=1)
        
        self.play(Write(explanation))
        self.play(Indicate(equation))
        self.wait(2)