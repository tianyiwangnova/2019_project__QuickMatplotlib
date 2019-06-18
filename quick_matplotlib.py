import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns

class QuickMatplotlib:
    """docstring for ClassName"""
    def __init__(self, style = "fivethirtyeight"):
        self.style = style

    def chart_set(self,
                  figsize = (10, 10),
                  title_size = 10,
                  xtick_labelsize = 10,
                  ytick_labelsize = 10,
                  xtick_rotate = 45,
                  style_ = None):
        style.use(self.style) if style_ is None else style.use(style_)
        plt.rcParams['figure.figsize'] = figsize
        plt.rcParams['xtick.labelsize'] = xtick_labelsize
        plt.rcParams['ytick.labelsize'] = ytick_labelsize
        plt.rcParams['axes.titlesize'] = title_size
        plt.xticks(rotation = xtick_rotate)
    
    @staticmethod
    def ax_set(ax,
               title = None,
               xlabel = None,
               ylabel = None):
        ax.set_title(title)
        if xlabel is not None:
            ax.set_xlabel(xlabel)
        if ylabel is not None:
            ax.set_ylabel(ylabel)

    def bar_chart(self,
                  data, 
                  x, 
                  y, 
                  figsize = (10, 10),
                  title_size = 10,
                  xtick_labelsize = 10,
                  ytick_labelsize = 10,
                  xtick_rotate = 45,
                  title = None,
                  xlabel = None,
                  ylabel = None,
                  style_ = None):

        self.chart_set(figsize,
                      title_size,
                      xtick_labelsize,
                      ytick_labelsize,
                      xtick_rotate,
                      style_)
        
        ax = sns.barplot(x = x, y = y, data = data)

        self.ax_set(ax,
                   title,
                   xlabel,
                   ylabel)

    def hist(self,
             data,
             bins = 10,
             figsize = (10, 10),
             title_size = 10,
              xtick_labelsize = 10,
              ytick_labelsize = 10,
              xtick_rotate = 45,
              title = None,
              xlabel = None,
              ylabel = None,
              style_ = None):

        self.chart_set(figsize,
                      title_size,
                      xtick_labelsize,
                      ytick_labelsize,
                      xtick_rotate,
                      style_)
        
        n, bins, patches = plt.hist(data, color="cornflowerblue", bins=bins)
        
        plt.title(title)
        if xlabel is not None:
            plt.xlabel(xlabel)
        if ylabel is not None:
            plt.ylabel(ylabel)
        
    def heatmap(self,
               df,
               figsize = (10, 10),
               title_size = 10,
                xtick_labelsize = 10,
                ytick_labelsize = 10,
                xtick_rotate = 45,
                title = None,
                xlabel = None,
                ylabel = None,
                style_ = None,
                cmap = "YlGnBu"):

        self.chart_set(figsize,
                      title_size,
                      xtick_labelsize,
                      ytick_labelsize,
                      xtick_rotate,
                      style_)

        ax = sns.heatmap(df, cmap=cmap)

        self.ax_set(ax,
                   title,
                   xlabel,
                   ylabel)

        