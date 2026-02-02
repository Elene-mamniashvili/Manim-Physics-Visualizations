from manim import *
import numpy as np

class WaveInterference(Scene):
    def construct(self):
        # 1. Setup Coordinate System
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": False}
        ).to_edge(DOWN, buff=0.5)

        # Labels - 'y' stays clear
        x_label = Text("Theta", font_size=20).next_to(axes.x_axis, RIGHT)
        y_label = Text("y", font_size=20).next_to(axes.y_axis, LEFT, buff=0.2).align_to(axes.y_axis, UP)

        # 2. Text and Equations
        title = Text("Lab: Wave Superposition & Interference", font_size=32).to_edge(UP, buff=0.2)
        
        # Source labels in the top-left
        label_a = Text("Wave A: sin(x)", color=BLUE, font_size=20)
        label_b = Text("Wave B: sin(3x)", color=GREEN, font_size=20)
        
        # RESULTANT LABEL: Aligned to x=0 (the y-axis)
        label_res = Text("Resultant: A + B", color=YELLOW, font_size=24, weight=BOLD)

        # Manual Positioning: 
        # Put A and B in the corner
        source_labels = VGroup(label_a, label_b).arrange(DOWN, aligned_edge=LEFT).to_corner(UL, buff=1)
        
        # Put Resultant slightly below them, also aligned to the LEFT edge
        label_res.next_to(source_labels, DOWN, buff=0.2, aligned_edge=LEFT)

        # 3. Defining the Wave Plots
        wave_a = axes.plot(lambda x: np.sin(x), color=BLUE)
        wave_b = axes.plot(lambda x: np.sin(3*x), color=GREEN)
        result_wave = axes.plot(lambda x: np.sin(x) + np.sin(3*x), color=YELLOW)

        # 4. Animation Sequence
        self.play(Write(title), Create(axes), Write(x_label), Write(y_label))
        
        self.play(Write(label_a))
        self.play(Create(wave_a), run_time=1.5)

        self.play(Write(label_b))
        self.play(Create(wave_b), run_time=1.5)
        self.wait(0.5)

        # Show result - now appearing on the left side under the other labels
        self.play(Write(label_res))
        self.play(
            wave_a.animate.set_stroke(opacity=0.3),
            wave_b.animate.set_stroke(opacity=0.3),
            Create(result_wave),
            run_time=3
        )
        self.wait(3)