from manim import *
import numpy as np

class SimpsonsParadox(Scene):
    def construct(self):
        # 1. SCALE DOWN THE GRID 
        # Making the units smaller ensures the full vector addition [12, 3] stays on screen.
        grid = NumberPlane(
            x_range=[0, 15, 1], 
            y_range=[0, 10, 1],
            x_length=10, 
            y_length=6,
            background_line_style={"stroke_opacity": 0.2}
        ).shift(DOWN * 0.5 + RIGHT * 1.5) 
        
        self.add(grid)

        # 2. STATIONARY HUD (Fixed Absolute Coordinates)
        HUD_X, HUD_Y = -6.0, 3.3
        stats = {"group_a": "0/0", "group_b": "0/0", "total": "0/0"}

        # Labels
        a_label = Text("Group A:", font_size=20, font="Consolas").move_to([HUD_X, HUD_Y, 0], aligned_edge=LEFT)
        b_label = Text("Group B:", font_size=20, font="Consolas").move_to([HUD_X, HUD_Y-0.4, 0], aligned_edge=LEFT)
        t_label = Text("TOTAL  :", font_size=20, font="Consolas", color=YELLOW).move_to([HUD_X, HUD_Y-0.8, 0], aligned_edge=LEFT)
        self.add(a_label, b_label, t_label)

        # Value Redrawers (Fixed Parentheses)
        a_val = always_redraw(lambda: Text(stats["group_a"], font_size=20, font="Consolas")
            .move_to([HUD_X + 1.8, HUD_Y, 0], aligned_edge=LEFT))
            
        b_val = always_redraw(lambda: Text(stats["group_b"], font_size=20, font="Consolas")
            .move_to([HUD_X + 1.8, HUD_Y-0.4, 0], aligned_edge=LEFT))
            
        t_val = always_redraw(lambda: Text(stats["total"], font_size=20, font="Consolas", color=YELLOW)
            .move_to([HUD_X + 1.8, HUD_Y-0.8, 0], aligned_edge=LEFT))
        
        self.add(a_val, b_val, t_val)

        # 3. VECTORS
        v1 = Line(grid.c2p(0,0), grid.c2p(2,2), color=BLUE, buff=0).add_tip(tip_length=0.2)
        v2 = Line(grid.c2p(0,0), grid.c2p(10,1), color=RED, buff=0).add_tip(tip_length=0.2)
        v_total = DashedLine(grid.c2p(0,0), grid.c2p(12,3), color=YELLOW, dash_length=0.1).add_tip()

        # 4. ANIMATION SEQUENCE
        # Draw Group A
        self.play(Create(v1), run_time=2)
        stats["group_a"] = "2/2 (100%)"
        self.wait(1)
        
        # Draw Group B
        self.play(Create(v2), run_time=2)
        stats["group_b"] = "1/10 (10%)"
        self.wait(1)

        # Draw Total (Update stats BEFORE animation so 0/0 updates instantly)
        stats["total"] = "3/12 (25%)"
        self.play(Create(v_total), run_time=2.5)
        
        self.wait(3)