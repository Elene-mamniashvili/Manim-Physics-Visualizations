from manim import *
import numpy as np

class ResonanceExplosion(Scene):
    def construct(self):
        # 1. Setup Coordinate System
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-4, 4, 1],
            x_length=10,
            y_length=6,
            axis_config={"include_tip": False}
        ).to_edge(DOWN, buff=0.5)

        title = Text("The Growing Vibration (Resonance)", font_size=32).to_edge(UP, buff=0.2)
        
        # 2. Math Parameters
        G = 0.35  
        B = 5     

        # 3. Defining the Expanding Envelope
        upper_line = axes.plot(lambda x: G * x, color=RED)
        lower_line = axes.plot(lambda x: -G * x, color=RED)
        
        upper_env = DashedVMobject(upper_line, dashed_ratio=0.5)
        lower_env = DashedVMobject(lower_line, dashed_ratio=0.5)

        # 4. The Resonant Wave
        resonant_wave = axes.plot(
            lambda x: (G * x) * np.sin(B * x),
            color=BLUE,
            stroke_width=3
        )

        # 5. Non-LaTeX Label (Fixes FileNotFoundError)
        formula = Text("y = (G * t) sin(Bt)", font_size=22, color=BLUE).to_corner(UL, buff=0.8)

        # 6. Animation Sequence
        self.play(Write(title), Create(axes))
        self.play(Write(formula))
        self.play(Create(upper_env), Create(lower_env), run_time=2)
        self.play(Create(resonant_wave), run_time=6, rate_func=linear)
        self.wait(3)