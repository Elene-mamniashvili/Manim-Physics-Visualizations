from manim import *
import numpy as np

class LawOfLargeNumbers(Scene):
    def construct(self):
        # --- 1. CONFIGURATION ---
        n_trials = 100
        results = np.random.randint(0, 2, n_trials)
        running_averages = np.cumsum(results) / np.arange(1, n_trials + 1)

        # --- 2. AXES SETUP  ---
        axes = Axes(
            x_range=[0, n_trials, 20],
            y_range=[0, 1, 0.2],
            x_length=10,
            y_length=5,
            axis_config={
                "include_tip": False,
                # THIS IS THE KEY: Force axes to use Text instead of MathTex
                "label_constructor": Text, 
                "font_size": 20
            },
            x_axis_config={"numbers_to_include": range(0, n_trials + 1, 20)},
            y_axis_config={"numbers_to_include": [0, 0.5, 1]}
        )
        
        # Manual labels using Text
        x_label = Text("Trials", font_size=24).next_to(axes.x_axis, DOWN)
        y_label = Text("Average", font_size=24).rotate(90 * DEGREES).next_to(axes.y_axis, LEFT)
        
        # Theoretical Mean Line
        mean_line = axes.get_horizontal_line(axes.c2p(n_trials, 0.5), color=BLUE)
        mean_label = Text("Target (0.5)", color=BLUE, font_size=18).next_to(mean_line, RIGHT)

        self.add(axes, x_label, y_label, mean_line, mean_label)

        # --- 3. UI TRACKERS ---
        trial_text = Text("Trial: 0", font_size=32).to_edge(UP).shift(LEFT * 3)
        avg_text = Text("Avg: 0.000", font_size=32, color=YELLOW).to_edge(UP).shift(RIGHT * 3)
        self.add(trial_text, avg_text)

        # --- 4. ANIMATION LOOP ---
        # We use a VGroup to store the path so we don't have to 'play' every segment
        path = VGroup()
        
        for i in range(n_trials):
            new_point = axes.c2p(i + 1, running_averages[i])
            
            # Update labels
            new_trial_text = Text(f"Trial: {i+1}", font_size=32).align_to(trial_text, UL)
            new_avg_text = Text(f"Avg: {running_averages[i]:.3f}", font_size=32, color=YELLOW).align_to(avg_text, UL)
            
            if i > 0:
                prev_point = axes.c2p(i, running_averages[i-1])
                line = Line(prev_point, new_point, color=YELLOW, stroke_width=2)
                self.add(line)
            
            self.remove(trial_text, avg_text)
            trial_text, avg_text = new_trial_text, new_avg_text
            self.add(trial_text, avg_text)
            
            # Use wait instead of play for the loop to keep it stable
            self.wait(0.05) 

        self.wait(2)