from manim import *
import numpy as np

class FrequencyModulation(Scene):
    def construct(self):
        # 1. Coordinate System Setup
        axes = Axes(
            x_range=[0, 4 * PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": False}
        ).to_edge(DOWN, buff=0.5)

        title = Text("Lab:Frequency Modulation (FM)", font_size=32).to_edge(UP, buff=0.3)

        # 2. Math Constants
        B = 5    # Carrier Frequency
        M = 3    # Modulation Intensity (The "Swing")
        C = 2    # Modulator Frequency (The Speed of Change)

        # 3. The FM Plot
        # This creates the characteristic "Accordion Effect"
        fm_wave = axes.plot(
            lambda x: np.sin(B * x + M * np.sin(C * x)),
            color=BLUE,
            stroke_width=3
        )

        # 4. Reference Wave (Faintly shows the original speed)
        reference_wave = axes.plot(
            lambda x: np.sin(B * x),
            color=GRAY,
            stroke_opacity=0.2
        )

        # 5. Drawing Logic
        self.play(Write(title), Create(axes))
        self.wait(0.5)
        
        # Show the reference first to establish the "Normal" state
        self.play(Create(reference_wave), run_time=1.5)
        
        # Create the FM wave. Watch it bunch up and stretch out!
        self.play(
            Create(fm_wave), 
            run_time=5, 
            rate_func=linear
        )
        
        self.wait(2)