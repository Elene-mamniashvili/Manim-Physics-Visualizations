from manim import *

class SimpsonsParadoxWiki(Scene):
    def construct(self):
        # 1. THE GRID
        grid = NumberPlane(
            x_range=[0, 15, 1], 
            y_range=[0, 12, 1],
            x_length=10, 
            y_length=6,
            background_line_style={"stroke_opacity": 0.1}
        ).to_edge(DOWN)
        self.add(grid)

        # 2. REFINED HUD (Pulled back from Y-axis)
        HUD_X, HUD_Y = -6.2, 3.4  # Moved further left
        VAL_OFFSET = 2.8           # Reduced distance between label and value
        
        stats = {"a": "Upward", "b": "Upward", "t": "Downward"}

        # HUD Labels
        a_txt = Text("Group A Trend:", font_size=19, font="Consolas").move_to([HUD_X, HUD_Y, 0], LEFT)
        b_txt = Text("Group B Trend:", font_size=19, font="Consolas").move_to([HUD_X, HUD_Y-0.4, 0], LEFT)
        t_txt = Text("GLOBAL TREND :", font_size=19, font="Consolas", color=WHITE).move_to([HUD_X, HUD_Y-0.8, 0], LEFT)
        
        # Values
        val_a = Text(stats["a"], font_size=19, font="Consolas", color=BLUE).move_to([HUD_X + VAL_OFFSET, HUD_Y, 0], LEFT)
        val_b = Text(stats["b"], font_size=19, font="Consolas", color=RED).move_to([HUD_X + VAL_OFFSET, HUD_Y-0.4, 0], LEFT)
        val_t = Text("", font_size=19, font="Consolas", color=WHITE).move_to([HUD_X + VAL_OFFSET, HUD_Y-0.8, 0], LEFT)

        self.add(a_txt, b_txt, t_txt, val_a, val_b)

        # 3. THE DATA TRENDS (Wikipedia Style)
        # Blue Group: Higher starting intercept
        line_a = Line(grid.c2p(1, 6), grid.c2p(4, 9), color=BLUE, stroke_width=6).add_tip()
        dots_a = VGroup(*[Dot(grid.c2p(x, x+5), color=BLUE, fill_opacity=0.6) for x in [1, 2, 3, 4]])

        # Red Group: Lower starting intercept
        line_b = Line(grid.c2p(8, 1), grid.c2p(11, 4), color=RED, stroke_width=6).add_tip()
        dots_b = VGroup(*[Dot(grid.c2p(x, x-7), color=RED, fill_opacity=0.6) for x in [8, 9, 10, 11]])

        # Global Paradox Line (Connecting centers)
        v_tot = DashedLine(grid.c2p(2.5, 7.5), grid.c2p(9.5, 2.5), color=WHITE, stroke_width=4).add_tip()

        # 4. ANIMATION SEQUENCE
        self.play(FadeIn(dots_a), Create(line_a), run_time=1.5)
        self.wait(0.5)
        
        self.play(FadeIn(dots_b), Create(line_b), run_time=1.5)
        self.wait(1)

        # The Reveal: Text and Line update together
        self.play(
            Create(v_tot),
            val_t.animate.become(
                Text("Downward", font_size=19, font="Consolas", color=WHITE).move_to([HUD_X + VAL_OFFSET, HUD_Y-0.8, 0], LEFT)
            ),
            run_time=2
        )
        self.play(Indicate(v_tot, color=WHITE, scale_factor=1.2))
        
        self.wait(3)