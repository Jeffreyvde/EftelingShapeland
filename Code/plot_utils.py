import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from tabulate import tabulate


def make_bar_plot(dict_list, figure_size: tuple[float, float], x, y, hue, y_max, title, location, estimator=None,
                  show=False):
    """
    Create a hued bar plot derived from a list of dictionaries
    """

    df = pd.DataFrame(dict_list)
    plt.figure(figsize=figure_size)
    if estimator:
        ax = sns.barplot(data=df, x=x, y=y, hue=hue, ci=None, estimator=estimator)
    else:
        ax = sns.barplot(data=df, x=x, y=y, hue=hue)
    ax.set(title=title)
    if y_max:
        ax.set(ylim=(0, y_max))
    plt.savefig(location, transparent=False, facecolor="white", bbox_inches="tight")
    plt.savefig(f"{location} Transparent", transparent=True, bbox_inches="tight")
    plt.show()
    if show and not estimator:
        print(
            tabulate(
                df.sort_values(hue),
                headers='keys',
                tablefmt='psql',
                showindex=False,
                floatfmt=('.2f')
            )
        )
    if show and estimator == sum:
        print(
            tabulate(
                df.groupby(x).sum().reset_index(),
                headers='keys',
                tablefmt='psql',
                showindex=False,
            )
        )
    if not show:
        plt.close()

