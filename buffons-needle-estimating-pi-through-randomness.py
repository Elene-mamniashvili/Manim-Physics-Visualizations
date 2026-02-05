from manim import *
import numpy as np

class BuffonsNeedle(Scene):
    def construct(self):
        # 1. Force Manim to use standard Text for everything
        # --------------------------------------------------
        num_needles = 50 # Reduced for faster testing
        l = 0.8  # length
        hits = 0
        total = 0

        # Draw the lines
        lines = VGroup(*[
            Line(LEFT * 4 + UP * i, RIGHT * 4 + UP * i)
            for i in range(-3, 4)
        ])
        self.add(lines)

        # 2. Replaced Integer/DecimalNumber with plain Text updates
        # --------------------------------------------------
        # We use Text() and change it manually to avoid ANY math-rendering logic
        hit_display = Text("Hits: 0", font_size=30).to_edge(UL)
        total_display = Text("Total: 0", font_size=30).next_to(hit_display, DOWN, aligned_edge=LEFT)
        pi_display = Text("Pi Approx: 0.0000", font_size=30, color=YELLOW).to_edge(UR)

        self.add(hit_display, total_display, pi_display)

        # 3. Animation Loop
        # --------------------------------------------------
        for _ in range(num_needles):
            x, y = np.random.uniform(-3, 3), np.random.uniform(-2, 2)
            theta = np.random.uniform(0, PI)
            
            y_start = y - (l/2) * np.sin(theta)
            y_end = y + (l/2) * np.sin(theta)
            
            # Check for hit
            is_hit = any(min(y_start, y_end) <= line <= max(y_start, y_end) for line in range(-3, 4))

            needle = Line(
                [x - l/2 * np.cos(theta), y - l/2 * np.sin(theta), 0],
                [x + l/2 * np.cos(theta), y + l/2 * np.sin(theta), 0],
                stroke_width=2,
                color=GREEN if is_hit else RED
            )

            total += 1
            if is_hit: hits += 1

            # Manually update text by replacing the mobject
            # This avoids the "DecimalNumber" class which sometimes peeps at LaTeX
            new_hit_display = Text(f"Hits: {hits}", font_size=30).align_to(hit_display, UL)
            new_total_display = Text(f"Total: {total}", font_size=30).align_to(total_display, UL)
            
            pi_val = (2 * l * total) / (hits) if hits > 0 else 0
            new_pi_display = Text(f"Pi Approx: {pi_val:.4f}", font_size=30, color=YELLOW).align_to(pi_display, UR)

            self.add(needle)
            self.remove(hit_display, total_display, pi_display)
            
            hit_display, total_display, pi_display = new_hit_display, new_total_display, new_pi_display
            self.add(hit_display, total_display, pi_display)
            
            self.wait(0.05) # Super fast "animation" without play() overhead

        self.wait(2)