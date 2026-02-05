from manim import *
import numpy as np
import random

class PercolationExperiment(Scene):
    def construct(self):
        # 1. Title and Probability Tracker
        title = Text("Percolation Threshold Experiment", font_size=32).to_edge(UP)
        p_tracker = ValueTracker(0)
        
        prob_label = always_redraw(lambda: 
            Text(f"Density (p) = {p_tracker.get_value():.3f}", font_size=24, color=YELLOW)
            .to_edge(RIGHT, buff=0.5)
        )
        self.add(title, prob_label)

        # 2. Grid Setup
        grid_size = 12 
        cell_size = 0.45
        grid = VGroup()
        cells = []

        for r in range(grid_size):
            row_cells = []
            for c in range(grid_size):
                rect = Square(side_length=cell_size, stroke_width=1, stroke_color=GRAY_D)
                rect.move_to(np.array([c * cell_size, -r * cell_size, 0]))
                grid.add(rect)
                row_cells.append(rect)
            cells.append(row_cells)

        grid.center().shift(LEFT * 1.5)
        self.add(grid)

        # 3. Path Logic (Stochastic Jagged Path)
        path_coords = []
        curr_c = random.randint(3, 8)
        for r in range(grid_size):
            path_coords.append((r, curr_c))
            curr_c = np.clip(curr_c + random.choice([-1, 0, 1]), 0, grid_size - 1)
        
        path_set = set(path_coords)
        spanning_path_group = VGroup(*[cells[r][c] for r, c in path_coords])

        # 4. Background Filling (Random Noise)
        all_indices = [(r, c) for r in range(grid_size) for c in range(grid_size) if (r, c) not in path_set]
        random.shuffle(all_indices)

        batch_size = 5 
        target_filled = int(0.58 * (grid_size**2)) 

        for i in range(0, target_filled, batch_size):
            batch = all_indices[i : i + batch_size]
            animations = [cells[r][c].animate.set_fill(BLUE_E, opacity=0.7) for r, c in batch]
            p_val = (i + batch_size) / (grid_size**2)
            self.play(*animations, p_tracker.animate.set_value(p_val), run_time=0.08)

        # 5. THE THRESHOLD MOMENT (Tied to the Path)
        # We update the value to the critical threshold
        self.play(p_tracker.animate.set_value(0.592), run_time=0.2)
        
        # Calculate the center of the actual yellow path
        path_center = spanning_path_group.get_center()
        
        # Create flash and message relative to the path's position
        flash = Circumscribe(spanning_path_group, color=YELLOW, fade_out=True)
        threshold_msg = Text("PATH CONNECTED!", color=YELLOW, font_size=30).next_to(spanning_path_group, RIGHT, buff=0.5)
        
        self.play(
            spanning_path_group.animate.set_fill(YELLOW, opacity=1),
            flash,
            Write(threshold_msg),
            run_time=1.2
        )

        # Pulse the path to show "Current" flowing through it
        self.play(Indicate(spanning_path_group, color=GOLD, scale_factor=1.2))
        self.wait(2)