from manim import *

class MomentumConservation(Scene):
    def construct(self):
        # 1. Setup Title and System Boundary
        title = Text("Conservation of Momentum", font_size=40).to_edge(UP)
        
        # DashedVMobject
        rect = Rectangle(width=10, height=4, color=GRAY)
        system_box = DashedVMobject(rect)
        
        system_label = Text("Isolated System", font_size=20, color=GRAY).next_to(system_box, UP, buff=0.1)
        self.add(title, system_box, system_label)

        # 2. Define Objects (Mass represented by size)
        m1, m2 = 2, 1  
        ball1 = Circle(radius=0.5, color=RED, fill_opacity=0.8).shift(LEFT * 4)
        ball2 = Circle(radius=0.25, color=BLUE, fill_opacity=0.8).shift(RIGHT * 1)
        
        label1 = Text(f"m={m1}", font_size=20).next_to(ball1, DOWN)
        label2 = Text(f"m={m2}", font_size=20).next_to(ball2, DOWN)

        # 3. Velocity Vectors
        v1_val = 2
        v2_val = -1
        arrow1 = Arrow(ball1.get_center(), ball1.get_center() + RIGHT * v1_val, buff=0, color=RED)
        arrow2 = Arrow(ball2.get_center(), ball2.get_center() + LEFT * abs(v2_val), buff=0, color=BLUE)

        # 4. Momentum Display
        total_p_val = (m1 * v1_val) + (m2 * v2_val)
        total_p_text = Text(f"Total Momentum: {total_p_val}", font_size=30, color=YELLOW).shift(UP * 2.5)

        self.play(FadeIn(ball1, ball2, label1, label2, arrow1, arrow2, total_p_text))
        self.wait(1)

        # 5. Collision Physics (Elastic calculation)
        v1_final = ((m1 - m2) / (m1 + m2)) * v1_val + ((2 * m2) / (m1 + m2)) * v2_val
        v2_final = ((2 * m1) / (m1 + m2)) * v1_val + ((m2 - m1) / (m1 + m2)) * v2_val

        # Animation of approach
        impact_point = ORIGIN
        self.play(
            ball1.animate.move_to(impact_point + LEFT*0.5),
            ball2.animate.move_to(impact_point + RIGHT*0.25),
            arrow1.animate.move_to(impact_point + LEFT*0.5 + RIGHT*(v1_val/2)),
            arrow2.animate.move_to(impact_point + RIGHT*0.25 + LEFT*(abs(v2_val)/2)),
            label1.animate.next_to(impact_point + LEFT*0.5, DOWN),
            label2.animate.next_to(impact_point + RIGHT*0.25, DOWN),
            rate_func=linear, run_time=2
        )

        # Collision Moment
        collision_flash = Flash(impact_point, color=YELLOW, flash_radius=0.5)
        
        # New Vectors after impact
        new_arrow1 = Arrow(impact_point + LEFT*0.5, impact_point + LEFT*0.5 + RIGHT * v1_final, buff=0, color=RED)
        new_arrow2 = Arrow(impact_point + RIGHT*0.25, impact_point + RIGHT*0.25 + RIGHT * v2_final, buff=0, color=BLUE)

        self.play(
            collision_flash,
            ReplacementTransform(arrow1, new_arrow1),
            ReplacementTransform(arrow2, new_arrow2)
        )

       # Bounce away
        self.play(
            ball1.animate.move_to(LEFT * 4), 
            ball2.animate.move_to(RIGHT * 4), 
            new_arrow1.animate.move_to(LEFT * 4 + RIGHT*(v1_final/2)),
            new_arrow2.animate.move_to(RIGHT * 4 + RIGHT*(v2_final/2)),
            label1.animate.next_to(LEFT * 4, DOWN),
            label2.animate.next_to(RIGHT * 4, DOWN),
            run_time=2
        )

        # THE FINAL FRAME: The blue arrow disappears
        # We use FadeOut to make the transition smooth
        self.play(
            FadeOut(new_arrow2),
           # ball2.animate.set_color(Grey), 
            run_time=1
        )
        
        self.wait(2)