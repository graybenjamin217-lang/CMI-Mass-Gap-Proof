import matplotlib.pyplot as plt
import numpy as np

# Metric drag parameter domain [0, 1)[span_3](start_span)[span_3](end_span)
eta_drag = np.linspace(0, 0.99, 300)

# Paired singular values for QCD coupling block: lambda = ±(1 ± eta_drag)[span_4](start_span)[span_4](end_span)
lambda_1_2_pos = 1 + eta_drag
lambda_1_2_neg = -(1 + eta_drag)
lambda_3_4_pos = 1 - eta_drag  # Minimum absolute eigenvalue branch[span_5](start_span)[span_5](end_span)
lambda_3_4_neg = -(1 - eta_drag)

plt.figure(figsize=(9, 6), dpi=300)

plt.plot(eta_drag, lambda_1_2_pos, color='#1F77B4', linewidth=2, label='$\\lambda_{1,2} = \\pm(1 + \\eta_{\\text{drag}})$')
plt.plot(eta_drag, lambda_1_2_neg, color='#1F77B4', linewidth=2, linestyle='--')
plt.plot(eta_drag, lambda_3_4_pos, color='#D9534F', linewidth=2.5, label='$\\lambda_{3,4} = \\pm(1 - \\eta_{\\text{drag}})$ (Min Branch)')
plt.plot(eta_drag, lambda_3_4_neg, color='#D9534F', linewidth=2.5, linestyle='--')

plt.axhline(0, color='black', linestyle=':', linewidth=1)
plt.fill_between(eta_drag, 0, lambda_3_4_pos, color='#D9534F', alpha=0.1, label='Strict Positive Spectral Floor ($\\lambda_{\\min} > 0$)')

plt.title("Eigenvalue Spectrum and Minimum Spectral Bound of $\\Gamma_{QCD}$", fontsize=12, fontweight="bold", pad=15)
plt.xlabel("Metric Drag Parameter ($\\eta_{\\text{drag}}$)", fontsize=11)
plt.ylabel("Singular Value Magnitude ($\\lambda$)", fontsize=11)
plt.ylim(-2.2, 2.2)
plt.legend(loc='lower left', frameon=True, facecolor="#F9F9F9")
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig("fig2_spectral_floor.png", dpi=300)
plt.show()
