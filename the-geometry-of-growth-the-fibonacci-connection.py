from manim import *
import numpy as np

class FibonacciGrowth(Scene):
    def construct(self):
        # 1. Sequence and directions
        fibs = [1, 1, 2, 3, 5, 8, 13]
        squares = VGroup()
        labels = VGroup()
        directions = [RIGHT, UP, LEFT, DOWN]
        
        # 2. Build Squares and Scaled Labels
        for i, side in enumerate(fibs):
            sq = Square(side_length=side)
            if i > 0:
                sq.next_to(squares, directions[i % 4], buff=0)
            
            # Label with dynamic scaling based on the square size
            num = Text(str(side), font_size=36) # Increased base size
            num.scale(side * 0.5 if side < 3 else side * 0.2) # Dynamic scaling
            num.move_to(sq.get_center())
            
            squares.add(sq)
            labels.add(num)
        
        # Center and zoom out slightly so the 13x13 square fits
        all_elements = VGroup(squares, labels).center().scale(0.35)
        
        # 3. The Arcs (The "Path of Growth")
        arcs = VGroup()
        for i, sq in enumerate(squares):
            arc = ArcBetweenPoints(
                sq.get_corner(self.get_start_corner(i)),
                sq.get_corner(self.get_end_corner(i)),
                angle=-PI/2,
                color=GOLD,
                stroke_width=6 # Made the arc thicker
            )
            arcs.add(arc)

        # 4. Animation
        for i in range(len(squares)):
            self.play(
                Create(squares[i]),
                Write(labels[i]),
                run_time=0.4
            )
        
        self.play(Create(arcs), run_time=3)
        self.wait(2)

    def get_start_corner(self, i):
        return [DL, DR, UR, UL][i % 4]

    def get_end_corner(self, i):
        return [DR, UR, UL, DL][i % 4]