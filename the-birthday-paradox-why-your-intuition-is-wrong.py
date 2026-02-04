from manim import *

class BirthdayParadox(Scene):
    def construct(self):
        # 1. Setup Axes - Explicitly forcing standard Text for numbers
        axes = Axes(
            x_range=[0, 50, 10],
            y_range=[0, 1, 0.2],
            axis_config={"include_tip": True},
            x_length=9,
            y_length=5,
            tips=False
        )
        
        # This is the specific fix: label_constructor=Text
        axes.add_coordinates(
            font_size=20, 
            label_constructor=Text
        )

        # 2. Probability Logic
        def get_prob(n):
            if n < 2: return 0
            p_no_match = 1.0
            for i in range(int(n)):
                p_no_match *= (365 - i) / 365
            return 1 - p_no_match

        # 3. Create the S-Curve Graph
        graph = axes.plot(lambda x: get_prob(x), x_range=[0, 50], color=BLUE)

        # 4. Marking the 23-person Tipping Point
        p_val = get_prob(23)
        dot_coords = axes.c2p(23, p_val)
        
        dot = Dot(dot_coords, color=YELLOW)
        v_line = axes.get_vertical_line(dot_coords, color=YELLOW, line_func=DashedLine)
        
        # Use Text here as well to be safe
        label = Text(
            "23 People: 50.7%", 
            font_size=24,
            color=YELLOW
        ).next_to(dot_coords, UR)

        # 5. Animation Sequence
        self.play(Create(axes))
        self.play(Create(graph), run_time=3)
        self.play(FadeIn(dot), Create(v_line))
        self.play(Write(label))
        self.wait(2)