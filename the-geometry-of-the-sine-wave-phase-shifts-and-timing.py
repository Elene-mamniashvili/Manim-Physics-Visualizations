from manim import *
import numpy as np

class SinePhaseShift(Scene):
    def construct(self):
        # 1. Setup Coordinate System
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            y_length=4,
            axis_config={"include_tip": False}
        ).to_edge(DOWN, buff=1)

        # Labels using standard Text instead of MathTex
        x_label = Text("Time (Theta)", font_size=20).next_to(axes.x_axis, RIGHT)
        y_label = Text("y", font_size=20).next_to(axes.y_axis, UP)
        labels = VGroup(x_label, y_label)

        # 2. Text and Equations (Using Text pattern)
        title = Text("Lab: Phase Displacement Analysis", font_size=32).to_edge(UP)
        
        # Base Equation: y = sin(theta)
        base_eq = Text("y = sin(x)", color=WHITE, font_size=24)
        base_eq.to_corner(UL, buff=1.2)

        # Shifted Equation: y = sin(x + PI/2)
        # Using a simple string since we are avoiding LaTeX
        shifted_eq = Text("y = sin(x + 1.57)", color=YELLOW, font_size=24)
        shifted_eq.next_to(base_eq, DOWN, buff=0.4, aligned_edge=LEFT)

        # 3. Wave Plots
        base_wave = axes.plot(lambda x: np.sin(x), color=WHITE)
        # Shifted by PI/2 (approx 1.57)
        shifted_wave = axes.plot(lambda x: np.sin(x + PI/2), color=YELLOW)

        # 4. Animation Sequence (Following your Fibonacci pattern)
        self.play(Write(title), Create(axes), Write(labels))
        self.wait(0.5)

        # Draw Base Wave and its label
        self.play(Write(base_eq))
        self.play(Create(base_wave), run_time=2)
        self.wait(1)

        # Draw Shifted Wave and its label
        self.play(Write(shifted_eq))
        self.play(Create(shifted_wave), run_time=2)
        
        # 5. Visualizing the Phase Gap (Using Braces/Lines without LaTeX)
        point_shifted_peak = axes.c2p(0, 1) 
        point_base_peak = axes.c2p(PI/2, 1) 
        
        gap_line = DashedLine(point_shifted_peak, point_base_peak, color=BLUE)
        
        # We use a standard Text label for the gap
        gap_label = Text("Phase Shift", font_size=18, color=BLUE).next_to(gap_line, UP)

        self.play(Create(gap_line), Write(gap_label))
        self.wait(3)