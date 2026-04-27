from pathlib import Path

import matplotlib.pyplot as plt


plt.style.use("seaborn-v0_8-whitegrid")


def rysuj_wykres(x_lista, y_funkcja, y_interp, x_nodes, y_nodes, tytul, nazwa_pliku=None):
	fig, ax = plt.subplots(figsize=(11, 6.5), dpi=120)
	fig.patch.set_facecolor("white")
	ax.set_facecolor("#fcfcfc")

	ax.plot(
		x_lista,
		y_funkcja,
		label="funkcja oryginalna",
		color="#1f77b4",
		linewidth=2.2,
	)
	ax.plot(
		x_lista,
		y_interp,
		label="wielomian interpolacyjny",
		color="#ff7f0e",
		linestyle="--",
		linewidth=2.2,
	)
	ax.scatter(
		x_nodes,
		y_nodes,
		color="#d62728",
		edgecolors="black",
		linewidths=0.6,
		s=55,
		label="węzły interpolacji",
		zorder=3,
	)

	ax.set_title(tytul, fontsize=14, fontweight="bold", pad=12)
	ax.set_xlabel("x", fontsize=11)
	ax.set_ylabel("y", fontsize=11)
	ax.grid(True, which="major", linestyle="-", linewidth=0.7, alpha=0.65)
	ax.grid(True, which="minor", linestyle=":", linewidth=0.5, alpha=0.35)
	ax.minorticks_on()
	ax.legend(frameon=True, facecolor="white", framealpha=0.95)

	for spine in ax.spines.values():
		spine.set_linewidth(0.9)

	fig.tight_layout()

	if nazwa_pliku:
		folder = Path("wykresy")
		folder.mkdir(exist_ok=True)
		sciezka = folder / nazwa_pliku
		fig.savefig(sciezka, dpi=300, bbox_inches="tight")
		print(f"Zapisano wykres do pliku: {sciezka}")

	plt.show()
