from manim import *

class FibonacciSpiralFixed(Scene):
    def construct(self):
        fibs = [1, 1, 2, 3, 5, 8, 13]
        squares = VGroup()
        arcs = VGroup()
        
        # Placement: we move around the previous blocks clockwise
        directions = [RIGHT, UP, LEFT, DOWN]
        
        # CORNER LOGIC:
        # To mirror the spiral correctly, we map which corners the arc connects.
        # These are carefully chosen to ensure the end of one matches the start of the next.
        start_corners = [UL, DL, DR, UR]
        end_corners = [DR, UR, UL, DL]

        for i, side in enumerate(fibs):
            sq = Square(side_length=side)
            
            if i == 0:
                squares.add(sq)
            else:
                # Place next square relative to the bounding box of all previous squares
                sq.next_to(squares, directions[(i-1) % 4], buff=0)
                squares.add(sq)

            # Creating the arc
            # Angle PI/2 (positive) vs -PI/2 (negative) controls the "mirror" flip
            arc = ArcBetweenPoints(
                sq.get_corner(start_corners[i % 4]),
                sq.get_corner(end_corners[i % 4]),
                angle=TAU/4, # TAU/4 is 90 degrees; use -TAU/4 if it still looks inverted on your setup
                color=GOLD,
                stroke_width=6
            )
            arcs.add(arc)

        # Center and scale to fit the 13-unit square
        spiral_group = VGroup(squares, arcs).center().scale(0.3)
        
        # Clean sequential animation
        for i in range(len(squares)):
            self.play(
                Create(squares[i]),
                Create(arcs[i]),
                run_time=0.6
            )
        
        self.wait(2)