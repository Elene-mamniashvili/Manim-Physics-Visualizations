from manim import *
import numpy as np

class ParadoxOfChoice(Scene):
    def construct(self):
        # 1. Title
        title = Text("The Paradox of Choice", font_size=36).to_edge(UP, buff=0.5)
        self.play(Write(title))

        # 2. Axes Setup (using label_constructor=Text to avoid LaTeX errors)
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 6, 2],
            x_length=7,
            y_length=4,
            axis_config={"include_tip": True, "label_constructor": Text},
        ).shift(DOWN * 0.5) # Shift down to give Title more room

        # Axis Labels
        labels = axes.get_axis_labels(
            x_label=Text("Options", font_size=20),
            y_label=Text("Joy", font_size=20)
        )

        # 3. The Curve
        curve = axes.plot(
            lambda x: x * np.exp(-x / 2.5) * 3, 
            x_range=[0, 10], 
            color=TEAL
        )

        # 4. FIXED: Placing the "Diminishing Returns" label
        # We place it relative to the middle of the curve, not the start
        dim_label = Text("Law of Diminishing Returns", font_size=18, color=TEAL)
        # Position it specifically at the peak to avoid the Y-axis
        dim_label.next_to(axes.c2p(5, 4), UR, buff=0.2)

        # 5. Analysis Paralysis Zone
        paralysis_zone = axes.get_area(curve, x_range=[7, 10], color=RED, opacity=0.3)
        paralysis_text = Text("Analysis Paralysis", font_size=16, color=RED_A)
        paralysis_text.move_to(axes.c2p(8.5, 1.5))

        # Animation
        self.play(Create(axes), Write(labels))
        self.play(Create(curve), run_time=2)
        self.play(Write(dim_label))
        self.play(FadeIn(paralysis_zone), Write(paralysis_text))
        self.wait(2)