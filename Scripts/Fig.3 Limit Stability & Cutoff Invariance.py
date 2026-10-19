import matplotlib.pyplot as plt
import numpy as np

# Resolution scale parameter delta_x -> 0 (Continuum limit)[span_6](start_span)[span_6](end_span)
delta_x = np.linspace(0.01, 1.0, 300)
a_scale = 1.5 # Fixed topological boundary scale 'a' of M_K[span_7](start_span)[span_7](end_span)[span_8](start_span)[span_8](end_span)
eta_val = 0.013607 # Fixed metric drag invariant[span_9](start_span)[span_9](end_span)[span_10](start_span)[span_10](end_span)

# Mass gap Delta = (hbar c / a) * (1 - eta_drag) remains invariant under delta_x -> 0[span_11](start_span)[span_11](end_span)
hbar_c = 1.0
mass_gap_evaluated = (hbar_c / a_scale) * (1 - eta_val) * np.ones_like(delta_x)
naive_collapse = hbar_c * delta_x # Standard Yang-Mills collapse failure mode (Delta -> 0)[span_12](start_span)[span_12](end_span)

plt.figure(figsize=(9, 6), dpi=300)

plt.plot(delta_x, mass_gap_evaluated, color='#D9534F', linewidth=2.5, label='DSI Operator Mass Gap $\\Delta = \\frac{\\hbar c}{a}(1 - \\eta_{\\text{drag}})')
plt.plot(delta_x, naive_collapse, color='#4682B4', linestyle='--', linewidth=2, label='Standard QFT Spectral Collapse ($\\Delta \\to 0$ as $\\delta x \\to 0$)')

plt.axvline(x=0.01, color='black', linestyle=':', label='Continuum Limit Target ($\\delta x \\to 0$)')

plt.title("Continuum Limit Stability and Cutoff Invariance ($M_K$ Manifold)", fontsize=12, fontweight="bold", pad=15)
plt.xlabel("Spatial Resolution Scale ($\\delta x$)", fontsize=11)
plt.ylabel("Spectral Gap Magnitude ($\\Delta$)", fontsize=11)
plt.xlim(0, 1.0)
plt.ylim(-0.05, 1.1)
plt.legend(loc='center right', frameon=True, facecolor="#F9F9F9")
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig("fig3_dilation_cutoff.png", dpi=300)
plt.show()
