import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

# --- Data ---
environments = [
    "default",
    "one message exchange",
    "one message exchange \n+ collaborating",
    "one message exchange \n+ competing ",
    "one message exchange \n+ competing + \nperformance leak",
    "one message exchange \n+ private channel",
    "one message exchange \n+ competing + private channel\n+ performance leak",
    "one message exchange \n+ oversight in meeting purpose",
    "two message exchange",

]

data = {
    "blue":    [0.5,  0.15, 5/18, 7/19,     0.4,    4/19,  0.35, 8/19,  0.25],
    "green":   [None, 0.15, 2/18, (3-2)/19, 0.05, (5-1)/19, 0.1,   1/19,  (0.05-0.05)],
}

# Agent 1
agent_1_color = {
    "blue":   "#0072B2",

# Agent 2
}
agent_2_color = {
    "green":   "#009E73",
}

all_colors = {**agent_1_color, **agent_2_color}

markers = {
    "blue":         "x",
    "green":   "x",
}

model_labels = {
    "blue":   "GPT-4-0613",
}

# --- Plot ---
fig, ax = plt.subplots(figsize=(9, 5.5))

y_positions = np.arange(len(environments))[::-1]
marker_size = 100

draw_order = ["blue", "green"]


for key in draw_order:
    vals   = data[key]
    color  = all_colors[key]
    marker = markers[key]

    for i, (y, x) in enumerate(zip(y_positions, vals)):
        if x is None:
            continue
        ax.scatter(
            x, y,
            marker=marker,
            s=marker_size,
            linewidths=2.5,
            color=color,
            alpha=1.0,
            label="_nolegend_",
            zorder=4,
            path_effects=[
                pe.withStroke(linewidth=4.5, foreground="white"),
            ],
        )

# --- Axes formatting ---
ax.set_yticks(y_positions)
ax.set_yticklabels(environments, fontsize=10)
ax.yaxis.tick_right()
ax.yaxis.set_label_position("left")
ax.set_xlabel("% LING Buy", fontsize=12)
ax.set_ylabel("Environment", fontsize=12)

ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x*100)}%"))
ax.set_xlim(-0.05, 1.08)
ax.set_ylim(-0.6, len(environments) - 0.4)

ax.set_axisbelow(True)
ax.yaxis.grid(True, color="#e0e0e0", linewidth=0.7, linestyle="-")
ax.xaxis.grid(True, color="#e0e0e0", linewidth=0.7, linestyle="-")

for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_edgecolor("black")
    spine.set_linewidth(1.2)

# ── Table-style legend ──────────────────────────────────────────────────────
#
#  Layout (3 cols):
#           [model label]  [Agent 1 marker]  [Agent 2 marker]
#  gpt-4-0613              x blue            x green
#
#  We draw this as an inset axes table inside a legend-style box.

agent_1_keys   = ["blue"]
agent_2_keys  = ["green"]

# Position the custom legend box in the lower-right of the axes
# (in axes-fraction coordinates)
box_x  = 0.63  # left edge of box
box_y  = 0.78  # bottom edge of box
box_w  = 0.35
box_h  = 0.2

# Draw a box (fancy bbox) for the legend
from matplotlib.patches import FancyBboxPatch
legend_box = FancyBboxPatch(
    (box_x, box_y), box_w, box_h,
    boxstyle="round,pad=0.01",
    transform=ax.transAxes,
    facecolor="white", edgecolor="#cccccc",
    linewidth=1.0, zorder=5, clip_on=False,
    alpha=0.95,
)
ax.add_patch(legend_box)

# Column header positions (in axes coords)
col_x = [box_x + 0.035, box_x + 0.175, box_x + 0.295]
header_y = box_y + box_h - 0.065

# Header text
ax.text(col_x[0], header_y, "Model",
        transform=ax.transAxes, fontsize=8, fontweight="bold",
        va="center", ha="left", zorder=6)
ax.text(col_x[1], header_y, "Agent 1",
        transform=ax.transAxes, fontsize=8, fontweight="bold",
        va="center", ha="center", zorder=6)
ax.text(col_x[2], header_y, "Agent 2",
        transform=ax.transAxes, fontsize=8, fontweight="bold",
        va="center", ha="center", zorder=6)

# Thin separator line under headers
sep_y = header_y - 0.045
ax.axhline(y=0, color="none")   # dummy; we use a Line2D in axes coords
from matplotlib.lines import Line2D as MLine2D
sep_line = MLine2D(
    [box_x + 0.01, box_x + box_w - 0.01],
    [sep_y, sep_y],
    transform=ax.transAxes,
    color="#000000", linewidth=0.8, zorder=6,
)
ax.add_line(sep_line)

# Row spacing
n_rows   = len(agent_1_keys)
row_ys   = [sep_y - 0.055 * (i + 0.9) for i in range(n_rows)]

trans = ax.transAxes

for i, (bk, lk) in enumerate(zip(agent_1_keys, agent_2_keys)):
    ry = row_ys[i]

    # Model name
    ax.text(col_x[0]-0.01, ry, model_labels[bk],
            transform=trans, fontsize=8,
            va="center", ha="left", zorder=6)

    # Agent 1 marker
    pt_dark = ax.plot(
        col_x[1], ry,
        marker=markers[bk],
        color=agent_1_color[bk],
        markersize=8,
        markeredgewidth=2.2,
        linestyle="None",
        transform=trans,
        zorder=7,
        clip_on=False,
    )

    # Agent 2 marker
    pt_light = ax.plot(
        col_x[2], ry,
        marker=markers[lk],
        color=agent_2_color[lk],
        markersize=8,
        markeredgewidth=2.2,
        linestyle="None",
        transform=trans,
        zorder=7,
        clip_on=False,
    )

plt.tight_layout()
plt.savefig("figures/exp_2.png", dpi=1200, bbox_inches="tight")
plt.savefig("figures/exp_2.svg", dpi=1200, bbox_inches="tight")
