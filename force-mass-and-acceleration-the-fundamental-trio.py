from manim import *

class NewtonsSecondLaw(Scene):
    def construct(self):
        # --- 1. Setup Objects ---
        # Small mass group
        small_block = Square(side_length=1.0, fill_opacity=1, color=BLUE)
        small_text = Text("Mass: 1kg", font_size=24).next_to(small_block, UP, buff=0.4) # Increased buff
        small_group = VGroup(small_block, small_text).move_to(LEFT * 3 + UP * 1.8)
        
        # Large mass group
        large_block = Square(side_length=1.8, fill_opacity=1, color=RED)
        large_text = Text("Mass: 3kg", font_size=24).next_to(large_block, UP, buff=0.4) # Increased buff
        large_group = VGroup(large_block, large_text).move_to(LEFT * 3 + DOWN * 1.5)
        
        ground1 = Line(LEFT * 5, RIGHT * 5, color=GRAY).next_to(small_block, DOWN, buff=0)
        ground2 = Line(LEFT * 5, RIGHT * 5, color=GRAY).next_to(large_block, DOWN, buff=0)

        self.add(ground1, ground2, small_group, large_group)

        # --- 2. Force Arrows ---
        # We define a longer arrow and position it with a healthy buff from the block
        force_a = Arrow(start=LEFT*2, end=ORIGIN, color=YELLOW, stroke_width=8, max_tip_length_to_length_ratio=0.25)
        force_a.next_to(small_block, LEFT, buff=0.6) # buff prevents overlap
        
        force_b = Arrow(start=LEFT*2, end=ORIGIN, color=YELLOW, stroke_width=8, max_tip_length_to_length_ratio=0.25)
        force_b.next_to(large_block, LEFT, buff=0.6) # buff prevents overlap
        
        f_text_a = Text("Force (F)", font_size=28, color=YELLOW).next_to(force_a, UP, buff=0.2)
        f_text_b = Text("Force (F)", font_size=28, color=YELLOW).next_to(force_b, UP, buff=0.2)

        self.play(GrowArrow(force_a), GrowArrow(force_b), FadeIn(f_text_a, f_text_b))
        self.wait(1)

        # --- 3. Animation ---
        self.play(
            FadeOut(f_text_a, f_text_b, force_a, force_b),
            small_group.animate.shift(RIGHT * 6.5),
            large_group.animate.shift(RIGHT * 2.2),
            run_time=3,
            rate_func=rate_functions.ease_in_quad
        )
        self.wait(1)

        # --- 4. Final Summary ---
        self.clear()
        formula = Text("F = m * a", font_size=72, color=YELLOW).center()
        explanation = Text("Greater Mass = Less Acceleration", font_size=32).next_to(formula, DOWN, buff=1)
        
        self.play(Write(formula))
        self.play(FadeIn(explanation))
        self.wait(2)