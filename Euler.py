from math import pow
from math import tan

import plotly.figure_factory as ff
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

def euler():
    h = 0.1
    x = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
    y_eval = [0.0]
    delta_y = [0.0]
    y_real = [0.0]
    eps = [0.0]

    for i in range(1, len(x)):
        y_eval.append(y_eval[i - 1] + h * fun(x[i - 1], y_eval[i - 1]))
        delta_y.append(h * fun(y_eval[i], x[i]))
        y_real.append(real_fun(x[i]))
        eps.append(y_real[i] - y_eval[i])

    # print in table format
    print(y_eval)
    print(delta_y)
    print(y_real)
    print(eps)

    data_matrix = [
        ['k', 'x', 'y', 'delta_y', 'y_real', 'eps']
    ]
    for i in range(0, len(x)):
        data_matrix.append([i, x[i], y_eval[i], delta_y[i], y_real[i], eps[i]])

    table = ff.create_table(data_matrix)
    plot(table)


def fun(x, y):
    return pow(x + y, 2)


def real_fun(x):
    return tan(x) - x


euler()
