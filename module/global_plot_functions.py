import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def hide_borders(ax, borders):
    for b in borders:
        ax.spines[b].set_visible(False)  # hide plot's border

def annotate_plot(ax, rotation=0, precision=0, pct_precision=0, y_offset=0, n=0, annotate=True):
    for p in ax.patches:
        if n == 0: h_adj = 1
        else: h_adj = 2
        
        x_offset = p.get_width() / 2
        format_str = ',.' + str(precision) + 'f'
        label = format(p.get_height(), format_str)
        x = p.get_x() + x_offset
        y = (p.get_height() + y_offset) / h_adj
        
        if annotate == True:  # annotate value in the middle of bar
            ax.annotate(label, (x,y), ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points', rotation=rotation)
        
        if n > 0:    # annotate percentage at the top of each bar
            pct_format_str = '.' + str(pct_precision) + 'f'
            ax.annotate(format(p.get_height()*100 / n, pct_format_str) + '%', 
               (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', 
                xytext = (0, 10), textcoords = 'offset points')