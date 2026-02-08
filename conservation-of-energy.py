from manim import *
import numpy as np

class ConservationOfEnergy(Scene):
    def construct(self):
        # 1. Physics Setup - Moved PIVOT DOWN
        length = 3.2 # Slightly shorter string
        gravity = 9.8
        theta_max = 40 * DEGREES
        pivot = UP * 1.0 
        
        pendulum_bob = Dot(radius=0.2, color=BLUE).move_to(pivot + DOWN * length)
        line = always_redraw(lambda: Line(pivot, pendulum_bob.get_center(), color=WHITE))
        
        # 2. Energy Bars Setup
       
        bar_containers = VGroup(
            Rectangle(width=0.5, height=2.0, stroke_opacity=0.3),
            Rectangle(width=0.5, height=2.0, stroke_opacity=0.3),
            Rectangle(width=0.5, height=2.0, stroke_opacity=0.3)
        ).arrange(RIGHT, buff=0.4)

        labels = VGroup(
            Text("PE", font_size=16).next_to(bar_containers, DOWN, buff=0.1), # Smaller font
            Text("KE", font_size=16).next_to(bar_containers[1], DOWN, buff=0.1),
            Text("Total", font_size=16).next_to(bar_containers[2], DOWN, buff=0.1)
        )

        # Align Labels to the containers individually for precision
        labels[0].next_to(bar_containers[0], DOWN, buff=0.1)
        labels[1].next_to(bar_containers[1], DOWN, buff=0.1)
        labels[2].next_to(bar_containers[2], DOWN, buff=0.1)

        chart = VGroup(bar_containers, labels)
        chart.to_corner(DR, buff=0.3) # Tight buffer to the corner

        # 3. Physics Logic
        h_max = length * (1 - np.cos(theta_max))
        E_total = gravity * h_max
        # Multiplier adjusted to 0.7 to fit in the new 2.0 height containers
        mult = 0.7 

        def get_energies():
            current_pos = pendulum_bob.get_center() - pivot
            theta = np.arctan2(current_pos[0], -current_pos[1])
            h = length * (1 - np.cos(theta))
            pe = gravity * h
            ke = E_total - pe
            return pe, ke

        # 4. The Animated Bars (Pinned to the bottom)
        pe_bar = always_redraw(lambda: Rectangle(
            width=0.5, height=max(0.01, get_energies()[0] * mult), 
            color=ORANGE, fill_opacity=0.8, stroke_width=0
        ).move_to(bar_containers[0].get_bottom(), aligned_edge=DOWN))
        
        ke_bar = always_redraw(lambda: Rectangle(
            width=0.5, height=max(0.01, get_energies()[1] * mult), 
            color=BLUE, fill_opacity=0.8, stroke_width=0
        ).move_to(bar_containers[1].get_bottom(), aligned_edge=DOWN))
        
        total_bar = Rectangle(
            width=0.5, height=E_total * mult, 
            color=GREEN, fill_opacity=0.8, stroke_width=0
        ).move_to(bar_containers[2].get_bottom(), aligned_edge=DOWN)

        # 5. Render
        self.add(line, pendulum_bob, bar_containers, labels, pe_bar, ke_bar, total_bar)
        
        path = Arc(radius=length, start_angle=-TAU/4 - theta_max, angle=theta_max*2).shift(pivot)
        
        for _ in range(3):
            self.play(
                MoveAlongPath(pendulum_bob, path),
                run_time=2, rate_func=there_and_back
            )
        self.wait()