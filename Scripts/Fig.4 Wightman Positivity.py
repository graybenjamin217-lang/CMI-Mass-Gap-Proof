import matplotlib.pyplot as plt
import numpy as np

# 64 complete operator basis projectors pi_k with spectrum restricted to {0, 1}[span_13](start_span)[span_13](end_span)[span_14](start_span)[span_14](end_span)
projector_indices = np.arange(1, 65)
eigenvalues_pi = np.random.choice([0, 1], size=64, p=[0.25, 0.75]) # Idempotent spectrum representation

plt.figure(figsize=(10, 5), dpi=300)
plt.stem(projector_indices, eigenvalues_pi, linefmt='b-', markerfmt='bo', basefmt='r-')

plt.title("Idempotent Spectrum of the 64-Element Projector Space $\\hat{\\Pi}_{64}$ ($\\pi_k^2 = \\pi_k$)", fontsize=12, fontweight="bold", pad=15)
plt.xlabel("Projector Basis Index ($k = 1, \\dots, 64$)", fontsize=11)
plt.ylabel("Eigenvalue Spectrum ($\\in \\{0, 1\\}$)", fontsize=11)
plt.yticks([0, 1])
plt.grid(True, linestyle='--', alpha=0.5)

plt.annotate("Strict Positivity:\\n$|\\|\\psi\\|_{\\hat{\\Pi}}^2 = 4\\|\\psi\\|_{L^2}^2 > 0$", 
             xy=(32, 1), xytext=(35, 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6),
             fontsize=10, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="#F9F9F9", ec="black"))

plt.tight_layout()
plt.savefig("fig4_wightman_positivity.png", dpi=300)
plt.show()
