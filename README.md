# Digital Physics Lab: Manim Visualizations 🧪

A collection of mathematical experiments exploring the intersection of geometry and motion. 

## 🔬 Lab Experiments

### 01\. The Pulse of a Circle

An introductory look at the vertical displacement of a rotating vector.

-   **Concept:** $y = \\sin(\\theta)$
    
-   **Key Visual:** Projection of circular motion onto a linear path.
    
-   **File:** `sine_projection.py`
    

### 02\. Sine Amplitude Projection

Demonstrating how the Circle's Radius acts as the "DNA" for Wave Amplitude.

-   **Concept:** $y = A \\sin(\\theta)$
    
-   **Key Visual:** Scaled radius ($R=1.8$) projection showing vertical stretching.
    
-   **File:** `sine_amplitude_projection.py`
    

### 03\. High-Frequency Waves

Exploring rotational velocity and the transformation of a "swing" into a "vibration."

-   **Concept:** $y = \\sin(B \\cdot \\theta)$
    
-   **Key Visual:** Side-by-side comparison of base speed ($B=1$) vs. high frequency ($B=5$).
    
-   **File:** `high-frequency-sine-waves.py`
    

### 04\. Beyond the Numbers: The Fibonacci Connection

Exploring how simple addition transforms into the universe’s favorite design blueprint.

-   **Concept:** Recursive Growth vs. Binet's Formula.
    
-   **Key Visual:** The "Growth Spiral" accelerating from arithmetic sums into organic architecture.
    
-   **File:** `the-geometry-of-growth-the-fibonacci-connection.py`
    

### 05\. The Geometry of the Sine Wave: Phase Shifts and Timing

Exploring how temporal offsets transform into spatial displacement.

-   **Concept:** Horizontal Translation and Angular Offset.
    
-   **Key Visual:** The "Temporal Gap" between two identical frequencies, visualizing lead and lag states.
    
-   **File:** `the-geometry-of-the-sine-wave-phase-shifts-and-timing.py`
    

### 06\. The Geometry of the Sine Wave: Interference and Superposition

Exploring how independent vibrations merge into complex harmonic systems.

-   **Concept:** Linear Summation and Wave Interference.
    
-   **Key Visual:** The "Composite Wave" formed by merging a fundamental frequency (Wave A) with its third harmonic (Wave B).
    
-   **File:** `the-geometry-of-the-sine-wave-wave-interference-and-superposition.py`

  
### 07\. The Geometry of Decay: Damped Harmonic Motion

Exploring how friction and resistance sculpt the sine wave over time by visualizing the transition from eternal oscillation to silence.

-   **Concept:** $y = e^{-at} \\cdot \\sin(Bt + \\phi)$
    
-   **Key Visual:** A sine wave trapped inside a shrinking "envelope" (exponential curves), showing the loss of energy over time.
    
-   **File:** `the-geometry-of-decay-damped-harmonic-motion.py`

  ### 08\. The Geometry of Information: Frequency Modulation (FM)

Exploring how one wave can "carry" another by stretching and squeezing time, visualizing the geometry of variable frequency.

-   **Concept:** $y = \\sin(B \\cdot t + M \\sin(C \\cdot t))$
    
-   **Key Visual:** The "Elastic Wave" or "Accordion Effect," where the wavelength varies dynamically across the x-axis, constrained by a modulator.
    
-   **File:** `the-geometry-of-information-frequency-modulation.py`

### 09\. The Geometry of Resonance: Driven Harmonic Motion

Visualizing the geometric "explosion" of amplitude when a system is pushed at its natural frequency.

-   **Concept:** $y = (G \\cdot t) \\sin(Bt)$
    
-   **Key Visual:** An expanding "V-shaped" envelope where the sine wave grows larger with every cycle, demonstrating the additive power of synchronized energy.
    
-   **File:** `the-geometry-of-resonance-driven-harmonic-motion.py`

### 10\. The Geometry of Complexity: Fourier Synthesis

Visualizing how any complex shape in the universe is constructed by "stacking" simple, smooth sine waves.

-   **Concept:** $y = \\sum\_{n=1,3,5}^{k} \\frac{1}{n} \\sin(n \\cdot t + \\frac{\\pi}{2})$
    
-   **Key Visual:** A "Harmonic Stack" where higher-frequency sine waves are layered onto a fundamental note, gradually transforming a smooth curve into a sharp, architectural square wave.
    
-   **File:** `the-geometry-of-complexity-fourier-series.py`
---
### 1\. The Birthday Paradox: Counterintuitive Probability

Visualizing the surprising mathematical truth that in a group of just 23 people, there is a >50% chance that two share a birthday.

-   **Concept:** $P(A) = 1 - \\frac{365!}{365^n(365-n)!}$
    
-   **Key Visual:** An exponential "S-Curve" that starts flat but climbs aggressively, crossing the 50% threshold much earlier than human intuition expects.
    
-   **File:** `the-birthday-paradox-why-your-intuition-is-wrong.py`

### 2\. The Monty Hall Problem: The Logic of Switching

Visualizing why your initial 1/3 chance of winning a car jumps to 2/3 simply by choosing to switch doors after the host reveals a "goat."

-   **Concept:** $P(\\text{Win by Switching}) = 1 - P(\\text{Initial Pick})$
    
-   **Key Visual:** A "Probability Shift" where the weight of a discarded door is transferred to the remaining unopened door, highlighted by a bold directional arrow.
    
-   **File:** `the-monty-hall-problem-why-switching-is-the-only-logical-choice.py`

### 3\. Buffon’s Needle: Estimating $\\pi$ Through Randomness

A geometric probability simulation that demonstrates how dropping needles onto a lined surface can converge on the value of $\\pi$.

-   **Concept:** The probability $P$ that a needle of length $l$ will cross a line among parallel lines spaced $d$ apart is $P = (2l) / (\\pi d)$. By rearranging, we estimate $\\pi \\approx (2l \\cdot n) / (d \\cdot h)$, where $n$ is the total drops and $h$ is the number of hits.
    
-   **Key Visual:** A "Hit vs. Miss" color-coding system where needles turn **Green** upon crossing a line and **Red** otherwise, paired with a real-time counter that recalculates the $\\pi$ approximation with every drop.
    
-   **File:** `buffons-needle-estimating-pi-through-randomness.py`

### 4\. The Law of Large Numbers: Chaos Finding its Balance

Visualizing the mathematical bridge between short-term randomness and long-term certainty as the sample average converges to the expected value.

-   **Concept:** As the number of trials $n$ increases, the sample mean $\\bar{X}\_n$ converges to the theoretical expected value $\\mu$. In this simulation of coin flips, the erratic initial fluctuations eventually smooth out into a stable line at $0.5$.
    
-   **Key Visual:** A dynamic line graph where the "vibration" of the line decreases over time, moving from high-variance chaos to a flat horizontal line, accompanied by a real-time "Trial vs. Average" HUD.
    
-   **File:** `the-law-of-large-numbers-chaos-finding-its-balance.py`

### 5\. Random Walk (Drunkard’s Walk): Finding Order in Drunken Footsteps

A simulation of a stochastic process where a path is determined by a series of random steps, illustrating how local chaos creates a global statistical structure.

-   **Concept:** Each step is chosen randomly from four cardinal directions (Up, Down, Left, Right). While individual movements are unpredictable, the **Root Mean Square (RMS)** distance from the origin follows the law $D \\approx L \\cdot \\sqrt{n}$, where $n$ is the number of steps and $L$ is the step length.
    
-   **Key Visual:** A dynamic path trace on a coordinate grid where a yellow dot (the "wanderer") leaves a persistent trail. The simulation features a **Stationary HUD** in the top-left corner that anchors the "Steps" and "Distance" values in place, providing real-time displacement data without visual jitter.
    
-   **File:** `the-random-walk-finding-order-in-drunken-footsteps.py`

### 6\. Simpson’s Paradox: How Data Can Be a Mathematical Illusion

A visual investigation into how aggregated data can reverse localized trends, illustrating the importance of weighting and context in data science.

-   **Concept:** Simpson’s Paradox occurs when a trend appearing in different groups of data disappears or reverses when those groups are combined. It highlights how "lurking variables"—specifically the distribution of data points—can create a misleading global average.
    
-   **Key Visual:** The paradox is visualized using two distinct data clusters. While the **Local Truths** (Blue and Red vectors) clearly show positive upward trends, the **Aggregate Trend** (White dashed line) connects the clusters in a way that tilts downward. This "Global Lie" visually demonstrates how the relative positioning of groups can flip the perceived narrative of the data.
    
-   **The HUD:** A stationary scoreboard tracks the trends in real-time, highlighting the "Upward" local performance against the "Downward" global illusion to ensure the viewer catches the reversal.
    
-   **File:** `simpsons-paradox-how-data-can-be-a-mathematical-illusion.py`
-   
### 7\. The Coupon Collector Problem: The Tax of the Final Item

A simulation-driven exploration of diminishing returns and the mathematical "waiting time" required to complete a set of random variables.

-   **Concept:** The Coupon Collector Problem describes the expected number of trials required to collect all unique types of an item. It reveals a non-linear difficulty curve: while the first few items are easy to find, the "last item" represents a statistical bottleneck where the probability of success plummets.
    
-   **Key Visual:** The experiment uses a **Collection Grid** alongside a real-time **Efficiency Tracker**. As the grid fills with blue (unique) items, the frequency of red (duplicate) flashes increases. The animation highlights the "Efficiency Collapse" phase, where the simulation time accelerates but progress in the grid slows to a crawl.
    
-   **The HUD:** A dynamic dashboard tracks **Total Trials**, **Collection Progress**, and **Simulation Time**. An integrated "Efficiency Status" monitor shifts from **HIGH (Green)** to **COLLAPSED (Red)** as the probability of finding a new item becomes mathematically unfavorable.
    
-   **File:** `the-coupon-collector-problem-the-tax-of-the-final-item.py`
  
### 8\. Central Limit Theorem: Order Emerging from Chaos

A visual proof of the most powerful theorem in statistics, showing how random sampling transforms messy data into a predictable Bell Curve.

-   **Concept:** The Central Limit Theorem (CLT) establishes that when independent random variables are added, their properly normalized sum tends toward a normal distribution, even if the original variables themselves are not normally distributed.
    
-   **Key Visual:** The animation simulates hundreds of samples being drawn from a "Uniform" (flat) distribution. It tracks the mean of each sample and plots it on a second histogram, showing the step-by-step formation of a **Gaussian Bell Curve**.
    
-   **The HUD:** Real-time counters track the **Sample Size (n)** and the **Standard Error**, visually demonstrating how the curve narrows and sharpens as more data is processed.
    
-   **File:** `central-limit-theorem-order-emerging-from-chaos.py`


## 🛠️ How to Run
To render these animations locally, ensure you have the [Manim Library](https://docs.manim.community/en/stable/installation.html) installed.

Use the following command in your terminal:

**For a quick low-quality preview:**
```bash
manim -pql [filename].py [ClassName]
