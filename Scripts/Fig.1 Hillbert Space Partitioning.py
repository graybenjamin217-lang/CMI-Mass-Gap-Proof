import matplotlib.pyplot as plt
import numpy as np

# Four 4x4 sub-block sectors on C^16 representing EW, QCD, GR, and Spin sectors[span_0](start_span)[span_0](end_span)
sectors = [
    'Sector 1 ($\\Gamma_{EW}$)\nElectroweak', 
    'Sector 2 ($\\Gamma_{QCD}$)\nStrong Interaction', 
    'Sector 3 ($\\Gamma_{GR}$)\nGravitational Coupling', 
    'Sector 4 ($\\Gamma_{\\text{spin}}$)\nSpinor Representation'
]
dimensions = [4, 4, 4, 4]  # Summing to 16-dim internal channel space C^16[span_1](start_span)[span_1](end_span)[span_2](start_span)[span_2](end_span)
colors = ['#1F77B4', '#D9534F', '#2CA02C', '#9467BD']

fig, ax = plt.subplots(figsize=(9, 6), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(dimensions, labels=sectors, autopct='%1.0f-Dim',
                                  startangle=90, colors=colors, 
                                  textprops=dict(color="black", fontweight='bold'),
                                  wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2.5))

plt.setp(autotexts, size=10, weight="bold", color="white")
plt.title("16-Dimensional Internal Channel Space Partitioning ($\\mathcal{H} = L^2(\\mathbb{R}^4) \\otimes \\mathbb{C}^{16}$)", fontsize=12, fontweight="bold", pad=20)

plt.tight_layout()
plt.savefig("fig1_hilbert_partition.png", dpi=300)
plt.show()
