import json
import matplotlib.pyplot as plt

def save_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def plot_hist(data, path, title="Terminal Wealth"):
    plt.hist(data, bins=50, alpha=0.7)
    plt.title(title)
    plt.savefig(path)
    plt.close()

def plot_value_function(X, V, path, title="Value Function"):
    plt.plot(X, V[0,:], label="t=0")
    plt.title(title)
    plt.legend()
    plt.savefig(path)
    plt.close()
