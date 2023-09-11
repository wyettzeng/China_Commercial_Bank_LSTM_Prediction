import pandas
from Yahoo import goodFileName
import matplotlib.pyplot as plt
import seaborn as sns


def useChineseFont():
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False


def mySaveFig(fig, imageName):
    '''Arguments:

    fig: a figure object
    imageName: the image name you want it to be, ex: "cumulative return"'''
    fig.savefig(f"python images/{goodFileName(imageName)}.png", bbox_inches="tight")
    plt.close(fig)
    plt.clf()
    plt.cla()


def lineGraphWithMultipleLines(
    df: pandas.DataFrame, title: str, xlabel: str, ylabel: str
):
    """Return a Figure Object"""
    ax = sns.lineplot(df)
    ax.set_title(title, fontsize=16)
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    fig = ax.get_figure()
    fig.set_size_inches(24, 16)
    return fig


def lineGraphWithMultipleLines_backup(
    df: pandas.DataFrame, title: str, xlabel: str, ylabel: str
):
    """Return a Figure Object"""
    ax = df.plot(
        figsize=(24, 16),
        title=title,
        xlim=(min(df.index), max(df.index)),
        xlabel=xlabel,
        ylabel=ylabel,
        fontsize=12,
    )
    ax.title.set_size(16)
    ax.yaxis.get_label().set_fontsize(14)
    ax.xaxis.get_label().set_fontsize(14)
    return ax.get_figure()


def barGraphSimple(df: pandas.Series, title: str, xlabel: str, ylabel: str):
    """Return a Figure Object"""
    ax = df.plot(
        kind="barh",
        figsize=(24, 16),
        title=title,
        xlim=(min(df.index), max(df.index)),
        xlabel=xlabel,
        ylabel=ylabel,
        fontsize=12,
    )
    ax.title.set_size(16)
    ax.yaxis.get_label().set_fontsize(14)
    ax.xaxis.get_label().set_fontsize(14)
    return ax.get_figure()


def scatterGraph(df: pandas.DataFrame, title: str):
    df = df.reset_index()
    ax = sns.scatterplot(
        data=df,
        x=df.columns.values[1],
        y=df.columns.values[2],
        hue=df.columns.values[0],
        style=df.columns.values[0],
    )
    ax.set_title(title, fontsize=16)
    ax.set_xlabel(df.columns.values[1], fontsize=14)
    ax.set_ylabel(df.columns.values[2], fontsize=14)
    ax.collections[0].set_sizes([500])
    fig = ax.get_figure()
    fig.set_size_inches(18, 12)
    return fig


def lineGraphWithSingleLine(ser: pandas.Series, title: str, xlabel: str, ylabel: str):
    ax = ser.plot(xlim=(min(ser.index), max(ser.index)))
    ax.set_title(title, fontsize=16)
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    fig = ax.get_figure()
    fig.set_size_inches(18, 12)
    return fig


def tableToPng(df: pandas.DataFrame, title: str):
    """Turns a pandas dataframe into a png file"""
    ax = plt.subplot(111, frame_on=False)  # no visible frame
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)  # hide the y axis
    ax.set_title(title, fontsize=16)
    pandas.plotting.table(ax, df, loc="center")
    fig = ax.get_figure()
    fig.set_size_inches(18, 12)
    return fig


def heatMap(df: pandas.DataFrame, title: str):
    ax = sns.heatmap(data=df, cmap="coolwarm")
    ax.set_title(title, fontsize=16)
    ax.tick_params(axis="x", labelsize=14, rotation=90)
    ax.tick_params(axis="y", labelsize=14, rotation=0)
    fig = ax.get_figure()
    fig.set_size_inches(24, 16)
    return fig


def normalDistributionGraph(df: pandas.DataFrame, title: str, xlabel: str, ylabel: str):
    fg = sns.displot(df, kind="kde", height=16, aspect=1.5)
    fg.set_axis_labels(xlabel, ylabel, fontsize=16)
    fg.ax.set_title(title, fontsize=16)
    fg.ax.axvline(x=0)
    fig = fg.figure
    return fig
