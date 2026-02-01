# Digital Physics Lab: Manim Visualizations 🧪

A collection of mathematical experiments exploring the intersection of geometry and motion. This repository serves as the source code for the "Digital Lab" blog series at [AnimateMath.com](https://animatemath.com).

## 🔬 Lab Experiments

### 01. The Pulse of a Circle
An introductory look at the vertical displacement of a rotating vector.
- **Concept:** $y = \sin(\theta)$
- **Key Visual:** Projection of circular motion.
- **File:** `pulse_of_a_circle.py`

### 02. Sine Amplitude Projection
Demonstrating how the Circle's Radius acts as the "DNA" for Wave Amplitude.
- **Concept:** $y = A \sin(\theta)$
- **Key Visual:** Scaled radius ($R=1.8$) projection.
- **File:** `sine_amplitude_projection.py`

### 03. High-Frequency Waves
Exploring rotational velocity and the transformation of a "swing" into a "vibration."
- **Concept:** $y = \sin(B \cdot \theta)$
- **Key Visual:** Side-by-side comparison of base speed ($B=1$) vs. high frequency ($B=5$).
- **File:** `high-frequency-sine-waves.py`

### 04. Beyond the Numbers: The Fibonacci Connection
Exploring how simple addition transforms into the universe’s favorite design blueprint.
- **Concept:** Recursive Growth vs. Binet's Formula.
- **Key Visual:** The "Growth Spiral" accelerating from arithmetic sums into organic architecture.
- **File:**  the-geometry-of-growth-the-fibonacci-connection.py

---

## 🛠️ How to Run
To render these animations locally, ensure you have the [Manim Library](https://docs.manim.community/en/stable/installation.html) installed.

Use the following command in your terminal:

**For a quick low-quality preview:**
```bash
manim -pql [filename].py [ClassName]
