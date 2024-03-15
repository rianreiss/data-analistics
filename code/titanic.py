import pandas as pd
from matplotlib import pyplot as plt

titanic_data = pd.read_csv('./dataset/projeto.csv')

def value_plot(df, y, figscale=1):
    df[y].plot(kind='line', figsize=(8 * figscale, 4 * figscale), title=y)
    plt.gca().spines[['top', 'right']].set_visible(False)
    plt.tight_layout()
    plt.show()


value_plot(titanic_data, 'Survived')