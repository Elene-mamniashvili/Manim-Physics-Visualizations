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

## 🛠️ How to Run
To render these animations locally, ensure you have the [Manim Library](https://docs.manim.community/en/stable/installation.html) installed.

Use the following command in your terminal:

**For a quick low-quality preview:**
```bash
manim -pql [filename].py [ClassName]
