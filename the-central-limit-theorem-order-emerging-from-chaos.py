from manim import *
import numpy as np

class CentralLimitTheorem(Scene):
    def construct(self):
        # 1. Title
        title = Text("Central Limit Theorem", font_size=40).to_edge(UP, buff=0.5)
        self.add(title)

        # 2. Main Histogram
        hist_chart = BarChart(
            values=[0] * 10,
            y_range=[0, 40, 10],
            x_length=10, 
            y_length=3.5, 
            y_axis_config={"font_size": 22, "label_constructor": Text},
            x_axis_config={"label_constructor": Text},
            bar_colors=[PURPLE_A, PURPLE_C, PURPLE_E]
        ).shift(UP * 0.2) 

        chart_label = Text("Distribution of Sample Means", font_size=24, color=PURPLE_A)
        chart_label.next_to(hist_chart, UP, buff=0.5)
        
        self.add(hist_chart, chart_label)

        # --- Simulation Logic ---
        all_means = []
        sample_size = 10
        iterations = 80 

        for i in range(iterations):
            samples = np.random.uniform(0, 10, sample_size)
            all_means.append(np.mean(samples))
            counts, _ = np.histogram(all_means, bins=10, range=(0, 10))
            
            rt = 0.15 if i < 15 else 0.05
            
            self.play(
                hist_chart.animate.change_bar_values(counts),
                run_time=rt,
                rate_func=linear 
            )

        # 3. Final Label - Moved "half-way" closer
        conclusion = Text("Average samples always form a Bell Curve!", font_size=24, color=YELLOW)
        
        # Changed buff from 0.8 (too far) or 0.4 (previous) to 0.6 
        # for that perfect middle ground below the X-axis labels.
        conclusion.next_to(hist_chart, DOWN, buff=0.6)

        self.play(Write(conclusion))
        self.wait(3)