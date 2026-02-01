from manim import *

class HighFrequencyComparison(Scene):
    def construct(self):
        # 1. Create Axes and scale them down more to leave room for titles
        # Use .shift(DOWN * 0.5) to pull them away from the top edge
        axes_slow = Axes(x_range=[0, 10, 1], y_range=[-1.5, 1.5, 1], axis_config={"include_tip": False}).scale(0.45).to_edge(UP, buff=1.0)
        axes_fast = Axes(x_range=[0, 10, 1], y_range=[-1.5, 1.5, 1], axis_config={"include_tip": False}).scale(0.45).to_edge(DOWN, buff=0.5)

        # 2. Labels - Use a slightly smaller scale and more "buff" (padding)
        label_slow = Text("Low Frequency (Slow)", color=WHITE).scale(0.4).next_to(axes_slow, UP, buff=0.3)
        label_fast = Text("High Frequency (Fast)", color=WHITE).scale(0.4).next_to(axes_fast, UP, buff=0.3)

        # 3. Waves
        wave_slow = axes_slow.plot(lambda x: np.sin(1 * x), color=BLUE)
        wave_fast = axes_fast.plot(lambda x: np.sin(5 * x), color=RED)

        # Group them to center the whole thing if needed
        self.add(axes_slow, axes_fast, label_slow, label_fast)
        
        # 4. Animate
        self.play(Create(wave_slow), run_time=4, rate_func=linear)
        self.play(Create(wave_fast), run_time=4, rate_func=linear)
        self.wait(2)