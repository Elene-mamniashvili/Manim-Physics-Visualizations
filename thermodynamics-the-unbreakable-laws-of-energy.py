from manim import *
import numpy as np

class ThermodynamicsFinal(Scene):
    def construct(self):
        # --- 0. THE ZEROTH LAW (THE BASELINE) ---
        title0 = Text("0th Law: Thermal Equilibrium", font_size=36).to_edge(UP)
        box_a = Square(side_length=1.2, fill_opacity=0.6, color=RED).shift(LEFT*3.5)
        box_c = Square(side_length=1.2, fill_opacity=0.6, color=WHITE).shift(ORIGIN)
        box_b = Square(side_length=1.2, fill_opacity=0.6, color=BLUE).shift(RIGHT*3.5)
        
        l_a = Text("A", font_size=20).next_to(box_a, UP)
        l_c = Text("C (Thermometer)", font_size=18, color=YELLOW).next_to(box_c, UP)
        l_b = Text("B", font_size=20).next_to(box_b, UP)

        self.play(Write(title0))
        self.play(FadeIn(box_a, box_b, box_c), Write(l_a), Write(l_b), Write(l_c))
        
        # C touches A then B to sync them
        self.play(box_c.animate.next_to(box_a, RIGHT, buff=0))
        self.play(box_c.animate.set_color(RED_A))
        self.play(box_c.animate.next_to(box_b, LEFT, buff=0))
        self.play(box_c.animate.set_color(BLUE_A))
        self.play(box_a.animate.set_color(PURPLE), box_b.animate.set_color(PURPLE), box_c.animate.set_color(PURPLE))
        self.wait(1)
        self.play(FadeOut(box_a, box_b, box_c, l_a, l_b, l_c, title0))

        # --- GLASS HELPER ---
        def create_glass():
            bottom = ArcBetweenPoints(LEFT*0.8 + DOWN*1.5, RIGHT*0.8 + DOWN*1.5, angle=-TAU/4)
            left_w = Line(LEFT*0.8 + DOWN*1.5, LEFT*1.1 + UP*1.5)
            right_w = Line(RIGHT*0.8 + DOWN*1.5, RIGHT*1.1 + UP*1.5)
            rim = Ellipse(width=2.2, height=0.3).move_to(UP*1.5)
            return VGroup(left_w, right_w, bottom, rim).set_color(WHITE)

        # --- 1. FIRST LAW (ENERGY BALANCE) ---
        title1 = Text("1st Law: Conservation of Energy", font_size=36).to_edge(UP)
        glass1 = create_glass().shift(LEFT*4.5)
        label1 = Text("1st Law: Energy", font_size=24).next_to(glass1, DOWN)
        
        liquid1 = Polygon(
            [-0.78, -1.4, 0], [0.78, -1.4, 0], [0.9, 0, 0], [-0.9, 0, 0],
            fill_opacity=0.4, color=GREEN, stroke_width=0
        ).move_to(glass1.get_bottom(), aligned_edge=DOWN).shift(UP*0.15)

        heat_in = Arrow(UP*3.2 + LEFT*5.5, UP*1.4 + LEFT*4.8, color=RED)
        work_out = Arrow(DOWN*0.2 + LEFT*4.2, DOWN*1.8 + LEFT*3.5, color=YELLOW)
        
        self.play(Write(title1), Create(glass1), FadeIn(liquid1), Write(label1))
        self.play(GrowArrow(heat_in)) # Heat arrow points DOWN into glass
        self.play(liquid1.animate.stretch_to_fit_height(2.6).move_to(glass1.get_bottom(), aligned_edge=DOWN).shift(UP*0.15))
        self.play(GrowArrow(work_out)) # Work arrow points DOWN away from glass
        self.play(liquid1.animate.stretch_to_fit_height(1.4).move_to(glass1.get_bottom(), aligned_edge=DOWN).shift(UP*0.15))
        self.wait(1)
        self.play(FadeOut(title1, heat_in, work_out))

        # --- 2. SECOND LAW (ENTROPY FIZZ) ---
        title2 = Text("2nd Law: Entropy (Disorder)", font_size=36).to_edge(UP)
        glass2 = create_glass().shift(ORIGIN)
        label2 = Text("2nd Law: Entropy", font_size=24).next_to(glass2, DOWN)
        liquid2 = Polygon(
            [-0.78, -1.4, 0], [0.78, -1.4, 0], [0.9, 0, 0], [-0.9, 0, 0],
            fill_opacity=0.4, color=ORANGE, stroke_width=0
        ).move_to(glass2.get_bottom(), aligned_edge=DOWN).shift(UP*0.15)

        bubbles = VGroup(*[Dot(radius=0.04, color=WHITE, fill_opacity=0.6) for _ in range(20)])
        for b in bubbles:
            b.move_to([np.random.uniform(-0.6, 0.6), np.random.uniform(-1.2, 0), 0])

        self.play(Write(title2), Create(glass2), FadeIn(liquid2), Write(label2))
        self.play(FadeIn(bubbles))
        # Bubbles rise to represent entropy
        bubbles.add_updater(lambda m, dt: [b.shift(UP*0.5*dt).set_y(-1.3) if b.get_center()[1] > 0.1 else b.shift(UP*0.5*dt) for b in m])
        self.wait(3)
        bubbles.clear_updaters()
        self.play(FadeOut(title2))

        # --- 3. THIRD LAW (STILLNESS) ---
        title3 = Text("3rd Law: Absolute Zero", font_size=36).to_edge(UP)
        glass3 = create_glass().shift(RIGHT*4.5)
        label3 = Text("3rd Law: Stillness", font_size=24).next_to(glass3, DOWN)
        liquid3 = Polygon(
            [-0.78, -1.4, 0], [0.78, -1.4, 0], [0.9, 0, 0], [-0.9, 0, 0],
            fill_opacity=0.9, color=BLUE_E, stroke_width=0
        ).move_to(glass3.get_bottom(), aligned_edge=DOWN).shift(UP*0.15)
        
        freeze_x = Cross(scale_factor=0.3).move_to(glass3.get_center()).set_color(RED)

        self.play(Write(title3), Create(glass3), FadeIn(liquid3), Write(label3))
        self.wait(0.5)
        # Freeze liquid to show limit
        self.play(liquid3.animate.set_color(WHITE), Create(freeze_x))
        self.play(FadeOut(freeze_x))
        self.wait(1)
        self.play(FadeOut(title3))

        # --- FINAL VISUAL (THREE GLASSES SIDE BY SIDE) ---
        final_msg = Text("The Unbreakable Laws", font_size=40, color=YELLOW).to_edge(UP)
        self.play(Write(final_msg))
        self.wait(5)