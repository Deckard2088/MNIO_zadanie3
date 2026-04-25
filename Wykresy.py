import matplotlib.pyplot as plt


def rysuj_wykres(x_lista, y_funkcja, y_interp, x_nodes, y_nodes, tytul):
	plt.figure(figsize=(10, 6))
	plt.plot(x_lista, y_funkcja, label="funkcja oryginalna")
	plt.plot(x_lista, y_interp, label="wielomian interpolacyjny", linestyle="--")
	plt.scatter(x_nodes, y_nodes, color="red", label="wezly interpolacji")
	plt.title(tytul)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.grid(True)
	plt.legend()
	plt.tight_layout()
	plt.show()
