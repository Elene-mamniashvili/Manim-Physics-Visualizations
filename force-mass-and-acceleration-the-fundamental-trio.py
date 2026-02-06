from manim import *

class NewtonsSecondLaw(Scene):
    def construct(self):
        # --- 1. Setup Objects ---
        # Large mass group (Our anchor)
        large_block = Square(side_length=1.8, fill_opacity=1, color=RED)
        large_text = Text("Mass: 3kg", font_size=24).next_to(large_block, UP, buff=0.4)
        large_group = VGroup(large_block, large_text).move_to(LEFT * 3 + DOWN * 1.5)
        
        # Small mass group (Aligned to large block's left)
        small_block = Square(side_length=1.0, fill_opacity=1, color=BLUE)
        small_text = Text("Mass: 1kg", font_size=24).next_to(small_block, UP, buff=0.4)
        small_group = VGroup(small_block, small_text).move_to(LEFT * 3 + UP * 1.8)
        small_group.align_to(large_group, LEFT)
        
        # --- 2. Synchronized Ground Coordinates ---
        # Small block: Start = block.get_left(), End = start + shift (6.5) + width (1.0)
        start_x_small = small_block.get_left()[0] 
        ground1 = Line(
            start=[start_x_small, small_block.get_bottom()[1], 0],
            end=[start_x_small + 7.5, small_block.get_bottom()[1], 0],
            color=GRAY, stroke_width=4
        )
        
        # Large block: Start = block.get_left(), End = start + shift (2.2) + width (1.8)
        start_x_large = large_block.get_left()[0]
        ground2 = Line(
            start=[start_x_large, large_block.get_bottom()[1], 0],
            end=[start_x_large + 4.0, large_block.get_bottom()[1], 0],
            color=GRAY, stroke_width=4
        )

        self.add(ground1, ground2, small_group, large_group)

        # --- 3. Force Arrows ---
        force_a = Arrow(start=LEFT*2, end=ORIGIN, color=YELLOW, stroke_width=8)
        force_a.next_to(small_block, LEFT, buff=0.6)
        
        force_b = Arrow(start=LEFT*2, end=ORIGIN, color=YELLOW, stroke_width=8)
        force_b.next_to(large_block, LEFT, buff=0.6)
        
        f_text_a = Text("Force (F)", font_size=28, color=YELLOW).next_to(force_a, UP, buff=0.2)
        f_text_b = Text("Force (F)", font_size=28, color=YELLOW).next_to(force_b, UP, buff=0.2)

        self.play(GrowArrow(force_a), GrowArrow(force_b), FadeIn(f_text_a, f_text_b))
        self.wait(1)

        # --- 4. Animation ---
        self.play(
            FadeOut(f_text_a, f_text_b, force_a, force_b),
            small_group.animate.shift(RIGHT * 6.5),
            large_group.animate.shift(RIGHT * 2.2),
            run_time=3,
            rate_func=rate_functions.ease_in_quad
        )
        self.wait(1)

        # --- 5. Final Summary ---
        self.clear()
        formula = Text("F = m * a", font_size=72, color=YELLOW).center()
        explanation = Text("Greater Mass = Less Acceleration", font_size=32).next_to(formula, DOWN, buff=1)
        
        self.play(Write(formula))
        self.play(FadeIn(explanation))
        self.wait(2)