from manim import *
import numpy as np

class DistributionSimulation(Scene): # Renamed to avoid syntax errors
    def construct(self):
        # 1. Title and Header
        title = Text("Central Limit Theorem", font_size=40).to_edge(UP, buff=0.3)
        subtitle = Text("Order Emerging from Chaos", font_size=20, color=BLUE_A).next_to(title, DOWN)
        self.add(title, subtitle)

        # 2. Setup BarChart 
        # labels
        hist_chart = BarChart(
            values=[0] * 30,
            y_range=[0, 150, 30], 
            x_length=10,
            y_length=4,
            y_axis_config={"font_size": 18, "label_constructor": Text},
            x_axis_config={"font_size": 18, "label_constructor": Text},
            bar_colors=[BLUE_C, BLUE_E, PURPLE_E],
            bar_fill_opacity=0.8,
        ).shift(DOWN * 0.5)

        self.add(hist_chart)

        # 3. Data Simulation Variables
        all_means = []
        sample_size = 30
        iterations = 1000 

        # 4. Animation Loop
        # We update the bars every 5 samples to keep the animation smooth but fast
        for i in range(iterations):
            # Generating uniform samples between 0 and 10
            samples = np.random.uniform(0, 10, sample_size)
            all_means.append(np.mean(samples))
            
            if i % 5 == 0: 
                # Create the histogram counts based on current data
                counts, _ = np.histogram(all_means, bins=30, range=(3, 7))
                
                # Update the chart bars
                # run_time is set to be compatible with 60fps renders
                self.play(
                    hist_chart.animate.change_bar_values(counts),
                    run_time=0.02, 
                    rate_func=linear
                )

        # 5. Conclusion Text
        conclusion = Text(
            f"{iterations} Samples: The distribution settles into a bell shape", 
            font_size=22, 
            color=YELLOW
        ).to_edge(DOWN, buff=0.5)
        
        self.play(Write(conclusion))
        self.wait(3)