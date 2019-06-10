import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns

class QuickMatplotlib:
    """docstring for ClassName"""
    def __init__(self, style = "fivethirtyeight"):
        self.style = style

    def bar_chart(self,
                  data, 
                  x, 
                  y, 
                  figsize = (10, 10),
                  xtick_labelsize = 10,
                  ytick_labelsize = 10,
                  xtick_rotate = 45,
                  title = None,
                  xlabel = None,
                  ylabel = None,
                  style_ = None):

        style.use(self.style) if style_ is None else style.use(style_)
        plt.rcParams['figure.figsize'] = figsize
        plt.rcParams['xtick.labelsize'] = xtick_labelsize
        plt.rcParams['ytick.labelsize'] = ytick_labelsize
        plt.xticks(rotation = xtick_rotate)

        ax = sns.barplot(x = x, y = y, data = data)
        ax.set_title(title)
        if xlabel is not None:
            ax.set(xlabel = xlabel)
            ax.set(ylabel = ylabel) 	