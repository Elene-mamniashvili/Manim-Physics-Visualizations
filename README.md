#Animations Created for AnimateMath.com

# Digital Math & Physics Lab: Manim Visualizations 🧪

A collection of mathematical experiments exploring the intersection of geometry and motion. 

## 🔬 Lab Experiments
## Math Foundations
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
## Math Simulations
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

### 9\. The Percolation Threshold: The Sudden Click of Connectivity 

A visual exploration of phase transitions and network theory, showing the exact moment a system of "local" connections transforms into a "global" flow.

**Concept:** Percolation theory models the behavior of connected clusters in a random graph. It reveals a "tipping point" (the critical threshold $p\_c \\approx 0.592$) where a system goes from being a collection of isolated islands to a fully connected network that allows for flow, communication, or travel.

**Key Visual:** The animation fills a grid with "open" sites at a random, increasing density ($p$). As the occupancy probability approaches the critical threshold, the animation slows down to capture the "Critical Jump." Once $p\_c$ is reached, the software identifies and illuminates the first **Spanning Cluster**—a jagged, fractal path that bridges the entire grid from top to bottom.

**The HUD:** A real-time tracker monitors the **Density ($p$)**, correlating the visual "clutter" of the grid with the mathematical probability of connectivity. When the path is completed, a localized **Circumscribe** effect highlights the specific geometry of the successful connection.

**File:** `the-percolation-threshold-why-systems-suddenly-click.py`

### 10\. Paradox of Choice: The Decision Paralysis Threshold

A psychological and mathematical simulation of "Satisficing" vs. "Maximizing," illustrating how an abundance of options leads to a collapse in user satisfaction.

-   **Concept:** The Paradox of Choice posits that while some choice is good, an excess of it leads to anxiety, higher opportunity costs, and eventually "Analysis Paralysis." In optimization terms, it shows a system where the cost of searching (cognitive load) eventually outpaces the marginal utility of finding a better option.

-   **Key Visual:** The animation plots a **Utility Curve** that begins with a steep climb (representing the freedom of choice) but eventually peaks and enters a sharp decline. As the number of options increases, the "Search Cost" is visualized as a rising shadow that eats away at the total "Joy" area.

-   **The HUD:** Real-time metrics track the **Option Count**, the **Opportunity Cost**, and the **Decision Time (Hick’s Law)**. When the "Optimal Choice" point is passed, the HUD triggers a "Warning: Paralysis Zone" alert, and the curve shifts from a vibrant Teal to a muted, flickering Red to represent stress.
-   **File:** `the-paradox-of-choice-why-more-is-actually-less.py`
---

## Engineering Physics
### 01\. The Law of Inertia: Why Things Keep Moving

A side-by-side comparison of friction-induced decay versus the infinite "status quo" of deep space.

-   **Concept:** Sum of Forces = 0 → Constant Velocity
    
-   **Key Visual:** A physical "Impulse" event followed by the separation of the object from the force that started its journey.
    
-   **File:** `the-law-of-inertia-why-things-keep-moving.py`
-   
### 02\. Newton's Second Law: The Fundamental Trio

A visual breakdown of the proportional relationship between mass, force, and the resulting acceleration.

-   **Concept:** $F = m \\cdot a$ (Force equals Mass times Acceleration)
    
-   **Key Visual:** Two distinct masses (1kg vs 3kg) subjected to the exact same pulling force. The animation demonstrates how the lighter object achieves significantly higher velocity over the same duration, while the heavier object resists the change in motion.
    
-   **File:** `force-mass-and-acceleration-the-fundamental-trio.py`

### 03\. Newton's Third Law: Action and Reaction

A visual proof that forces never exist in isolation but always as simultaneous, equal, and opposite pairs.

-   **Concept:** $F\_{A \\to B} = -F\_{B \\to A}$ (Reciprocal Interaction)
    
-   **Key Visual:** Two objects interact (such as a collision or a person pushing off a wall), showing force vectors of identical magnitude appearing instantly in opposite directions. It highlights that "reaction" is not a delay, but a simultaneous partner to "action."
    
-   **File:** `newtons-third-law-action-reaction.py`

### 04\. Newton's Law of Universal Gravitation: The Invisible Thread

A dynamic visualization of gravity as a field of influence that weakens with the square of the distance between two masses.

-   **Concept:** $F = G \\frac{m\_1 m\_2}{r^2}$ (The Inverse Square Law)
    
-   **Key Visual:** A stationary central mass creates a "gravitational ripple" that intensity-scales in real-time as a smaller planet swoops through its field. Instead of simple static vectors, the animation uses a **dynamic tether** that thickens and glows based on proximity, visually proving how attraction intensifies exponentially as objects approach one another.
    
-   **File:** `gravity-the-invisible-thread.py`

### 05\. Thermodynamics: The Soda Glass Analogy

A multi-stage visualization that simplifies the complex laws of energy and disorder into a relatable metaphor: filling, spending, and the inevitable "fizz" of the universe.

-   **Concept:** The four fundamental laws (0th through 3rd) governing energy transfer and entropy.
    
    -   **0th Law:** Thermal Equilibrium (Defining the Thermometer).
        
    -   **1st Law:** Energy Conservation ($dU = Q - W$).
        
    -   **2nd Law:** Entropy Increase ($dS > 0$).
        
    -   **3rd Law:** The Absolute Zero Limit ($T \\to 0$).
        
-   **Key Visual:** \* **The Bank Account:** A glass fills with liquid as **Heat (Q)** is poured in and drops as **Work (W)** is extracted, demonstrating that internal energy is a perfect balance of inputs and outputs.
    
    -   **The Inescapable Fizz:** Even when energy is stable, the 2nd Law is visualized through rising bubbles that represent **Entropy**. This proves that while energy is conserved, its "quality" is constantly being taxed by disorder.
        
    -   **The Frozen Limit:** The 3rd Law is depicted through a solidification effect and a "physical block" (Red Cross), visually communicating why absolute zero is an asymptotic limit that can never be reached.
        
-   **Technical Implementation:** Uses a custom `Polygon` liquid-logic system that scales and stretches in real-time, synced with directional vectors representing heat flow and work extraction.
    
-   **File:** `thermodynamics-the-soda-glass.py`

### 06\. Conservation of Momentum: The Law of Cosmic Balance

A precise simulation of an elastic collision within an isolated system, demonstrating how momentum is traded between objects but never lost.

-   **Concept:** p = m \* v (Momentum equals Mass times Velocity)
    
-   **Key Visual:** A collision between a large mass (2kg) and a smaller mass (1kg) inside a dashed "Isolated System" boundary. The animation uses dynamic velocity arrows that morph in real-time to show the transfer of momentum. As the large mass strikes the smaller one, the total system momentum—tracked by a live counter—remains perfectly constant, even as the individual balls change direction and speed.
    
-   **The Finale:** To emphasize the end of the interaction, the blue ball's velocity vector fades away upon reaching its final state, leaving the viewer to focus on the "Total Momentum" constant that ruled the entire event.
    
-   **File:** `conservation-of-momentum.py`

### 07\. Conservation of Energy: The Pendulum Balance

A synchronized physical simulation demonstrating the eternal exchange between gravitational potential and kinetic motion, proving that energy is never lost, only transformed.

-   **Concept:** $E\_{total} = PE + KE$ (Total Energy equals Potential plus Kinetic)
    
-   **Key Visual:** A swinging pendulum linked to three dynamic bar charts (PE, KE, and Total). As the pendulum reaches its apex, the **Potential Energy** bar peaks; as it swings through the center at maximum speed, the energy "liquifies" into **Kinetic Energy**. The animation highlights the "checkbook of the universe"—while the individual components fluctuate, the **Total Energy** bar remains rock-solid and immobile.
    
-   **Technical Implementation:** The script utilizes `always_redraw` updaters to calculate instantaneous height ($h$) and velocity ($v$) from the pendulum's angular position, mapping these physical values to the height of the UI bar objects in real-time.
    
-   **File:** `conservation-of-energy.py`

### 08\. Gauss's Law for Magnetism: The No-Monopole Principle

A geometric field visualization demonstrating that magnetic field lines are "eternal loopers," proving that the net magnetic flux through any closed surface is always zero.

-   **Concept:** ∇ · B = 0 (The Divergence of the Magnetic Field is zero).
    
-   **Key Visual:** A moving "Gaussian Surface" (a transparent circle) glides through a scientifically accurate dipole magnetic field. A real-time "Net Flux" counter stays locked at **0.00**, regardless of the surface's proximity to the magnetic poles. This visualizes the fundamental truth that every field line entering the boundary must also leave it, confirming that "North-only" or "South-only" magnetic charges do not exist.
    
-   **Technical Implementation:** The script defines a custom vector field function using the **Dipole Formula**. To ensure cross-platform compatibility without LaTeX dependencies, it utilizes `always_redraw` to link standard `Text` objects to the position of the Gaussian surface, creating a "Heads-Up Display" (HUD) effect.
    
-   **File:** `maxwells-equations-electromagnetism.py`

### 09\. Gauss's Law for Electricity: The Source Principle

A dynamic radial field simulation demonstrating that electric charges act as physical "faucets" or "sources" of flux, providing a sharp contrast to the "loop-only" nature of magnetism.

-   **Concept:** ∇ · E = ρ / ε₀ (The Divergence of the Electric Field is proportional to the enclosed charge).
    
-   **Key Visual:** Replacing static arrows with high-velocity **StreamLines**, the field physically "flows" outward from a central positive charge. As the Gaussian Surface (circle) moves to capture the charge, the "Net Flux" HUD transitions from **0.00** to **1.00**. This demonstrates that while empty space has a balanced inflow/outflow, a physical charge creates a "net" emission of field lines that never return to their source.
    
-   **Technical Implementation:** To simulate a "faucet" effect, the script utilizes `StreamLines` with a $1/r^2$ falloff function. It avoids LaTeX crashes by using a distance-based logic gate (`np.linalg.norm`) within an `always_redraw` function to update standard `Text` mobjects in real-time.
    
-   **File:** `maxwells-gausss-electric-law.py`

### 10\. Faraday's Law: The Induction Bridge

A high-fidelity simulation of electromagnetic induction, visualizing the "birth" of an electric field from a fluctuating magnetic source and demonstrating the kinetic connection between the two forces.

-   **Concept:** $\\nabla \\times E = -\\partial B / \\partial t$ (A time-varying magnetic field creates a curling electric field).
    
-   **Key Visual:** A bar magnet traverses through a stationary wire loop, acting as the catalyst for induction. As the magnet approaches, a "vortex" of yellow electric field arrows materializes and spins around the wire. The animation captures **Lenz's Law** in real-time: the direction of the induced field vortex flips as the magnet enters versus when it exits, visually proving nature's resistance to change in magnetic flux.
    
-   **Technical Implementation:** Uses a Gaussian-style bell curve function (`np.exp`) to calculate "Induction Strength" based on the magnet's relative X-coordinate. This value dynamically scales the magnitude and rotational direction of a `VectorField` via `always_redraw`. To ensure maximum compatibility and prevent environment-specific crashes, the script utilizes standard Unicode characters for mathematical symbols rather than external LaTeX compilers.
    
-   **File:** `maxwells-faradays-law.py`
  
## 🛠️ How to Run
To render these animations locally, ensure you have the [Manim Library](https://docs.manim.community/en/stable/installation.html) installed.

Use the following command in your terminal:

**For a quick low-quality preview:**
```bash
manim -pql [filename].py [ClassName]
