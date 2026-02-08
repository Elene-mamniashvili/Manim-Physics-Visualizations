from manim import *

class NewtonsThirdLaw(Scene):
    def construct(self):
        # --- 1. Setup Objects ---
        # Each block will shift 3.5 units. Width is 1.0.
        blue_block = Square(side_length=1.0, fill_opacity=1, color=BLUE).move_to(LEFT * 0.5)
        red_block = Square(side_length=1.0, fill_opacity=1, color=RED).next_to(blue_block, RIGHT, buff=0)
        
        system = VGroup(blue_block, red_block).center()
        
        # GROUND LOGIC: (Displacement 3.5 + Width 1.0) * 2 = 9.0 units
        # This keeps the blocks in the middle and ends flush at the corners
        ground = Line(start=ORIGIN, end=RIGHT * 9.0, color=GRAY, stroke_width=4)
        ground.next_to(system, DOWN, buff=0).move_to([system.get_center()[0], -0.5, 0])

        self.add(ground, blue_block, red_block)
        
        # --- 2. Action/Reaction Arrows ---
        arrow_red = Arrow(ORIGIN, RIGHT * 1.5, color=YELLOW, buff=0).move_to(red_block.get_left(), aligned_edge=LEFT)
        arrow_blue = Arrow(ORIGIN, LEFT * 1.5, color=YELLOW, buff=0).move_to(blue_block.get_right(), aligned_edge=RIGHT)
        
        label_red = Text("Action", font_size=24, color=YELLOW).next_to(arrow_red, UP, buff=0.2)
        label_blue = Text("Reaction", font_size=24, color=YELLOW).next_to(arrow_blue, UP, buff=0.2)

        self.play(GrowArrow(arrow_red), GrowArrow(arrow_blue), FadeIn(label_red, label_blue))
        self.wait(1)

        # --- 3. Animation ---
        self.play(
            FadeOut(label_red, label_blue, arrow_red, arrow_blue),
            blue_block.animate.shift(LEFT * 4), # Moves to exactly the left end of the line
            red_block.animate.shift(RIGHT * 4), # Moves to exactly the right end of the line
            run_time=3,
            rate_func=rate_functions.ease_in_out_quad
        )
        self.wait(1)

        # --- 4. Final Summary ---
        self.clear()
        formula = Text("Action = -Reaction", font_size=60, color=YELLOW).center()
        explanation = Text("Total System Force = 0", font_size=32).next_to(formula, DOWN, buff=1)
        
        self.play(Write(formula))
        self.play(FadeIn(explanation))
        self.wait(2)