from manim import *
import numpy as np

class RandomWalk(Scene):
    def construct(self):
        # 1. Setup Parameters
        step_length = 0.5
        num_steps = 150
        directions = [UP, DOWN, LEFT, RIGHT]
        
        # 2. Background Grid
        grid = NumberPlane(
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        )
        self.add(grid)

        # 3. FROZEN HUD (Fixed Coordinates)
        # We define exact points so they NEVER move
        STEP_X, STEP_Y = -6.5, 3.5
        DIST_X, DIST_Y = -6.5, 3.0

        step_label = Text("Steps:", font_size=24, font="Consolas").move_to([STEP_X, STEP_Y, 0], aligned_edge=LEFT)
        dist_label = Text("Dist: ", font_size=24, font="Consolas").move_to([DIST_X, DIST_Y, 0], aligned_edge=LEFT)
        
        self.add(step_label, dist_label)

        # We store the numeric values in a dictionary
        stats = {"steps": 0, "dist": 0.00}

        # The key: we anchor the LEFT edge of the number to a FIXED point 
        # (exactly 1.5 units to the right of the label start)
        step_num_display = always_redraw(lambda: 
            Text(str(stats["steps"]), font_size=24, font="Consolas")
            .move_to([STEP_X + 1.5, STEP_Y, 0], aligned_edge=LEFT)
        )
        
        dist_num_display = always_redraw(lambda: 
            Text(f"{stats['dist']:.2f}", font_size=24, font="Consolas")
            .move_to([DIST_X + 1.5, DIST_Y, 0], aligned_edge=LEFT)
        )

        self.add(step_num_display, dist_num_display)

        # 4. The Wanderer & Path
        wanderer = Dot(color=YELLOW, radius=0.1)
        path = TracedPath(
            wanderer.get_center, 
            stroke_color=YELLOW, 
            stroke_width=3,
            stroke_opacity=0.8
        )
        self.add(path, wanderer)

        # 5. Animation Loop
        current_pos = ORIGIN
        for i in range(1, num_steps + 1):
            move = directions[np.random.randint(0, 4)]
            current_pos += (move * step_length)
            
            # Update values
            stats["steps"] = i
            stats["dist"] = np.linalg.norm(current_pos)
            
            # Animation
            self.play(
                wanderer.animate.move_to(current_pos),
                run_time=0.08,
                rate_func=linear
            )

        self.wait(2)