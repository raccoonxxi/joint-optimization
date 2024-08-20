import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from matplotlib import ticker

plt.rcParams["font.family"] = "arial"

fig_filename = "compare_opt_llama.pdf"

yaxis_name = r"Perplexity on raw-WikiText2"

# Updated figure size with a reduced width (from 12 to 6)
fig, ax = plt.subplots(figsize=(6, 2.4))

results = [
    [10.859849, 7.263283, 10.128001, 6.727351],
    [11.582367, 9.607524, 10.839114, 8.485275],
    [12.541007, 11.305843, 11.197624, 9.757555],
    [14.157989, 14.549644, 11.80208, 11.966681]
]

pattern_names = [
    "Dense",
    "50% Unstructured",
    "4:8",
    "2:4",
]

model_names = [
    "OPT-6.7B",
    "LLaMA-7B",
    "OPT-13B",
    "LLaMA-13B",
]

colors = [
    "#000000",
    "#FFC300",
    "#27ae60",
    "#e74c3c",
]

fontcolors = [
    "#FFFFFF",
    "#000000",
    "#000000",
    "#000000",
]

bar_width = 0.2

for i in range(len(pattern_names)):
    positions = np.arange(len(model_names))
    offset = (-len(pattern_names) / 2 + 0.5 + i) * bar_width
    positions = positions + offset

    plt.bar(positions, results[i], bar_width,
            color=colors[i],
            edgecolor="#000000",
            zorder=2
            )

    for li in range(len(results[i])):
        text_label = r"{:.2f}".format(results[i][li])
        plt.text(positions[li], results[i][li], text_label, ha='center', va='top', rotation=90, fontsize=9, color=fontcolors[i], zorder=2)

ax.set_ylabel(yaxis_name)

handles, labels = ax.get_legend_handles_labels()

legend = ax.legend(pattern_names, ncol=len(pattern_names),
                   fancybox=False, shadow=False, title="",
                   facecolor='white', framealpha=1,
                   bbox_to_anchor=(0.5, 1.2),
                   loc='upper center'
                   )

ymin, ymax = ax.get_ylim()

# Updated y-axis to display integers without the 'x' multiplier
ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(lambda x, pos: r"{:.0f}".format(x)))

ax.xaxis.set_ticks(np.arange(len(model_names)))
ax.set_xticklabels(model_names, fontsize=9, rotation=15)

plt.tight_layout()

box = ax.get_position()
ax.set_position([box.x0 + box.width * 0.0, box.y0 + box.height * -0.1,
                 box.width * 1, box.height * 1.2])

plt.savefig(fig_filename)
plt.show()
