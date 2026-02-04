from manim import *
import numpy as np

class FourierSynthesis(Scene):
    def construct(self):
        # 1. Setup Coordinate System
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=4,
            axis_config={"include_tip": False}
        ).to_edge(DOWN, buff=0.5)

        title = Text("Lab: The Geometry of Synthesis", font_size=36).to_edge(UP)
        
        # 2. Fourier Function Logic (Odd Harmonics)
        # We use phase PI/2 to match your blog's "Aligned Peaks" logic
        def get_fourier_wave(n_terms, stroke_width=2, color=BLUE, opacity=1.0):
            return axes.plot(
                lambda x: sum([
                    (1/n) * np.sin(n * x + PI/2) 
                    for n in range(1, n_terms * 2, 2)
                ]),
                color=color,
                stroke_width=stroke_width,
                stroke_opacity=opacity
            )

        # 3. Create Layers
        fundamental = get_fourier_wave(1, color=BLUE, opacity=0.4)
        harmonic_3 = get_fourier_wave(2, color=BLUE, opacity=0.6)
        harmonic_5 = get_fourier_wave(3, color=BLUE, opacity=0.8)
        
        # Final Square Approximation (10 terms)
        square_approx = get_fourier_wave(10, color=WHITE, stroke_width=4)

        # 4. Labels
        labels = VGroup(
            Text("n=1 (Fundamental)", font_size=20, color=BLUE),
            Text("n=1,3 (Adding Harmonics)", font_size=20, color=BLUE),
            Text("n=1,3,5... (Synthesis)", font_size=20, color=WHITE)
        ).to_corner(UL)

        # 5. Animation Sequence
        self.play(Write(title), Create(axes))
        self.wait(1)

        # Step 1: Fundamental
        self.play(Create(fundamental), Write(labels[0]))
        self.wait(1)

        # Step 2: Add 3rd Harmonic
        self.play(
            Transform(fundamental, harmonic_3),
            Transform(labels[0], labels[1]),
            run_time=2
        )
        self.wait(1)

        # Step 3: Final Synthesis
        self.play(
            Transform(fundamental, square_approx),
            Transform(labels[0], labels[2]),
            run_time=3
        )
        
        # Highlight the "Architecture"
        self.play(Indicate(fundamental, color=YELLOW))
        self.wait(2)