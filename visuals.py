###########################################
# Suppress matplotlib user warnings
# Necessary for newer version of matplotlib
import warnings
warnings.filterwarnings("ignore", category = UserWarning, module = "matplotlib")
#
# Display inline matplotlib plots with IPython
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
###########################################

import matplotlib.pyplot as pl
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
from time import time
from sklearn.metrics import f1_score, accuracy_score


def distribution(data, transformed = False):
    """
    Visualization code for displaying skewed distributions of features
    """

    # Create figure
    fig = pl.figure(figsize = (11,5));

    # Skewed feature plotting
    for i, feature in enumerate(['compression-ratio','engine-size']):
        ax = fig.add_subplot(1, 2, i+1)
        ax.hist(data[feature], bins = 25, color = '#00A0A0')
        ax.set_title("Distribucion del atributo '%s'"%(feature), fontsize = 14)
        ax.set_xlabel("Valor")
        ax.set_ylabel("Numero de registros")
        ax.set_ylim((0, 200))
        ax.set_yticks([0, 50, 100, 150, 200])
        ax.set_yticklabels([0, 50, 100, 150, ">200"])

    # Plot aesthetics
    if transformed:
        fig.suptitle("Transformacion logaritmica de atributos continuos de automoviles", \
            fontsize = 16, y = 1.03)
    else:
        fig.suptitle("Distribuciones sesgadas de atributos continuos de automoviles", \
            fontsize = 16, y = 1.03)

    fig.tight_layout()
    fig.show()
