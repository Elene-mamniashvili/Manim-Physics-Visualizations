from manim import *
import numpy as np

class ConservationOfEnergy(Scene):
    def construct(self):
        # 1. Setup Pendulum Physics
        length = 3.5
        gravity = 9.8
        theta_max = 40 * DEGREES
        
        # Pendulum anchor and pivot
        pivot = UP * 2
        pendulum_bob = Dot(radius=0.2, color=BLUE).move_to(pivot + DOWN * length)
        line = always_redraw(lambda: Line(pivot, pendulum_bob.get_center(), color=WHITE))
        
        
        # 2. Energy Bars Setup
        bars = VGroup(
            Rectangle(width=0.5, height=4, color=ORANGE, fill_opacity=0.8), # PE
            Rectangle(width=0.5, height=4, color=BLUE, fill_opacity=0.8),   # KE
            Rectangle(width=0.5, height=4, color=GREEN, fill_opacity=0.8)  # Total
        ).arrange(RIGHT, buff=0.5).to_edge(RIGHT, buff=1)
        
        labels = VGroup(
            Text("PE", font_size=20).next_to(bars[0], DOWN),
            Text("KE", font_size=20).next_to(bars[1], DOWN),
            Text("Total", font_size=20).next_to(bars[2], DOWN)
        )

        # 3. Dynamic Scaling Logic
        # Total Energy is constant based on max height
        h_max = length * (1 - np.cos(theta_max))
        E_total = gravity * h_max
        
        def get_energies():
            # Current angle calculation
            current_pos = pendulum_bob.get_center() - pivot
            theta = np.arctan2(current_pos[0], -current_pos[1])
            h = length * (1 - np.cos(theta))
            pe = gravity * h
            ke = E_total - pe
            return pe, ke

        # Redraw bars based on energy
        pe_bar = always_redraw(lambda: Rectangle(
            width=0.5, height=max(0.01, get_energies()[0] * 1.5), 
            color=ORANGE, fill_opacity=0.8
        ).move_to(bars[0].get_bottom(), aligned_edge=DOWN))
        
        ke_bar = always_redraw(lambda: Rectangle(
            width=0.5, height=max(0.01, get_energies()[1] * 1.5), 
            color=BLUE, fill_opacity=0.8
        ).move_to(bars[1].get_bottom(), aligned_edge=DOWN))
        
        total_bar = Rectangle(
            width=0.5, height=E_total * 1.5, 
            color=GREEN, fill_opacity=0.8
        ).move_to(bars[2].get_bottom(), aligned_edge=DOWN)

        # 4. Animation
        self.add(line, pendulum_bob, bars, labels, pe_bar, ke_bar, total_bar)
        
        # Swing Pendulum
        self.play(
            MoveAlongPath(pendulum_bob, Arc(radius=length, start_angle=-TAU/4 - theta_max, angle=theta_max*2).shift(pivot)),
            run_time=2, rate_func=there_and_back
        )
        # Loop the swing
        for _ in range(2):
            self.play(
                MoveAlongPath(pendulum_bob, Arc(radius=length, start_angle=-TAU/4 - theta_max, angle=theta_max*2).shift(pivot)),
                run_time=2, rate_func=there_and_back
            )
        
        self.wait()