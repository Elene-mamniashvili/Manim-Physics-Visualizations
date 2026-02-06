from manim import *

class NewtonsFirstLaw(Scene):
    def construct(self):
        # --- 1. Object at Rest ---
        status_label = Text("At Rest: Velocity (v) = 0", font_size=36).to_edge(UP, buff=0.8)
        
        square = Square(side_length=1.5, fill_opacity=1, color=RED)
        ground = Line(LEFT * 4, RIGHT * 4, color=GRAY).next_to(square, DOWN, buff=0)
        
        self.add(ground)
        self.play(DrawBorderThenFill(square), Write(status_label))
        self.wait(1)
        
        # --- 2. Applying an Unbalanced Force ---
        # Tip ends at -0.9, square starts at -0.75 (No intersection)
        force_arrow = Arrow(LEFT * 3.5, LEFT * 0.9, color=YELLOW, buff=0)
        # Increased buff=0.6 so text is well above the square
        force_text = Text("Unbalanced Force", font_size=28, color=YELLOW).next_to(force_arrow, UP, buff=0.6)
        
        self.play(GrowArrow(force_arrow), FadeIn(force_text))
        self.wait(1)
        
        # --- 3. Transition to Motion ---
        moving_label = Text("In Motion: v is Constant", font_size=36).to_edge(UP, buff=0.8)
        
        self.play(
            FadeOut(status_label, force_arrow, force_text),
            FadeIn(moving_label),
            square.animate.shift(RIGHT * 4),
            run_time=2,
            rate_func=linear
        )
        self.wait(1)
        
        # --- 4. Deep Space (No Friction) ---
        self.play(FadeOut(square, ground, moving_label))
        
        space_label = Text("In Vacuum: No Friction", font_size=32, color=PURPLE).to_edge(UP, buff=0.8)
        puck = Circle(radius=0.5, fill_opacity=1, color=WHITE)
        
        # Velocity vector and text with high buff to avoid overlap
        velocity_vector = Arrow(ORIGIN, RIGHT * 1.5, color=GREEN, buff=0).next_to(puck, RIGHT, buff=0.2)
        v_text = Text("Constant Velocity", font_size=24, color=GREEN).next_to(velocity_vector, UP, buff=0.5)
        
        # Group puck and its velocity indicator
        moving_obj = VGroup(puck, velocity_vector, v_text).move_to(LEFT * 5)
        
        self.play(FadeIn(space_label), FadeIn(moving_obj))
        
        # Animation showing infinite constant motion
        self.play(
            moving_obj.animate.shift(RIGHT * 10),
            run_time=5,
            rate_func=linear
        )
        self.wait(1)
        
        # --- 5. Conclusion Formula ---
        # Using standard text instead of LaTeX for maximum compatibility
        formula = Text("Sum of Forces = 0  →  Acceleration = 0", font_size=32, color=YELLOW).center()
        bg_rect = SurroundingRectangle(formula, color=BLUE, buff=0.5)
        
        self.play(FadeOut(space_label, moving_obj))
        self.play(Write(formula), Create(bg_rect))
        self.wait(3)