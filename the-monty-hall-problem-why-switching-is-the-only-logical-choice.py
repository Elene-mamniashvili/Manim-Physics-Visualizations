from manim import *

class MontyHallAnalysis(Scene):
    def construct(self):
        # 1. Create Doors with adjusted Title positions (UP * 2.2 to avoid overlap)
        doors = VGroup(*[
            VGroup(
                Rectangle(width=2, height=3.5, fill_opacity=1, fill_color=BLUE_E),
                Text(f"Door {i+1}", font_size=24).shift(UP * 2.2)
            ) for i in range(3)
        ]).arrange(RIGHT, buff=1).shift(UP * 0.5)

        # 2. Probability Labels with extra room (buff=0.8)
        prob_labels = VGroup(*[
            Text("1/3", color=YELLOW, font_size=28).next_to(doors[i], DOWN, buff=0.8)
            for i in range(3)
        ])

        self.play(DrawBorderThenFill(doors))
        self.play(Write(prob_labels))
        self.wait()

        # 3. Highlight Initial Choice
        choice_rect = SurroundingRectangle(doors[0], color=GREEN, buff=0.1)
        choice_text = Text("Your Choice", color=GREEN, font_size=20).next_to(choice_rect, UP, buff=0.5)
        
        self.play(Create(choice_rect), Write(choice_text))
        self.wait()

        # 4. Group the "Other" Doors
        others_rect = SurroundingRectangle(VGroup(doors[1], doors[2]), color=PURPLE, buff=0.2)
        others_text = Text("Host's Group (2/3)", color=PURPLE, font_size=24).next_to(others_rect, UP, buff=0.5)
        
        self.play(
            Create(others_rect),
            Write(others_text),
            doors[1].animate.set_opacity(0.5),
            doors[2].animate.set_opacity(0.5)
        )
        self.wait()

        # 5. Monty opens Door 3 to reveal a Goat
        x_mark = Text("X", color=RED, font_size=80).move_to(doors[2])
        goat_text = Text("GOAT", color=RED, font_size=24).next_to(x_mark, DOWN, buff=0.2)
        
        self.play(Write(x_mark), Write(goat_text))
        self.play(prob_labels[2].animate.set_opacity(0.2))
        self.wait()

       # 6. ARROW LOGIC
        new_prob = Text("2/3 Chance", color=PURPLE, font_size=32).move_to(prob_labels[1])
        
        # 'start' is now set to the center of the old label 3 position 
        # 'end' remains the same with a safe 'buff' to avoid the label
        arrow = Arrow(
            start=prob_labels[2].get_center(), # Started from the center to gain length
            end=new_prob.get_right() + RIGHT * 0.2, 
            buff=0.4, # Buffer keeps the tip from touching the text
            color=PURPLE,
            stroke_width=10, 
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=5
        )

        self.play(
            FadeOut(prob_labels[1]),
            ReplacementTransform(prob_labels[2].copy(), new_prob),
            Create(arrow)
        )
        
        # 7. Final Conclusion Note at the edge
        final_note = Text(
            "Switching captures the full 2/3 probability!", 
            color=YELLOW, 
            font_size=30
        ).to_edge(DOWN, buff=0.6)
        
        self.play(Write(final_note))
        self.play(Indicate(new_prob, scale_factor=1.1))
        self.wait(3)