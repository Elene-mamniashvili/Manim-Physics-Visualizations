from manim import *
import numpy as np

class DampedOscillation(Scene):
    def construct(self):
        # 1. Setup Coordinate System
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": False}
        ).to_edge(DOWN, buff=0.5)

        # Labels for the axes
        x_label = Text("Time (t)", font_size=20).next_to(axes.x_axis, RIGHT)
        y_label = Text("y", font_size=20).next_to(axes.y_axis, LEFT, buff=0.2).align_to(axes.y_axis, UP)

        # 2. Titles and Text
        title = Text("Lab: Damping & Exponential Decay", font_size=32).to_edge(UP, buff=0.2)
        
        # Formula Labels for the Sidebar
        label_decay = Text("Envelope: A(t) = e^-0.5t", color=RED, font_size=20)
        label_wave = Text("Wave: e^-0.5t * sin(5t + pi/2)", color=BLUE, font_size=20)
        
        # Position labels in the top-left corner
        labels_group = VGroup(label_decay, label_wave).arrange(DOWN, aligned_edge=LEFT)
        labels_group.to_corner(UL, buff=0.8)

        # 3. Defining the Mathematical Plots
        # Upper and Lower Exponential Envelopes (Using DashedVMobject for compatibility)
        upper_plot = axes.plot(lambda x: np.exp(-0.5*x), color=RED)
        lower_plot = axes.plot(lambda x: -np.exp(-0.5*x), color=RED)
        
        # Wrap the plots to make them dashed
        upper_env = DashedVMobject(upper_plot, dashed_ratio=0.5)
        lower_env = DashedVMobject(lower_plot, dashed_ratio=0.5)
        
        # The Damped Sine Wave with Phase Shift pi/2
        damped_wave = axes.plot(
            lambda x: np.exp(-0.5*x) * np.sin(5*x + np.pi/2), 
            color=BLUE
        )

        # 4. Animation Sequence
        self.play(Write(title), Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)
        
        # Step 1: Draw the boundaries (The Envelope)
        self.play(Write(label_decay))
        self.play(Create(upper_env), Create(lower_env), run_time=2)
        self.wait(0.5)
        
        # Step 2: Draw the wave constrained within those boundaries
        self.play(Write(label_wave))
        self.play(Create(damped_wave), run_time=4)
        
        # Hold the final result
        self.wait(3)