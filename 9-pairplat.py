import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'preco': [20, 25, 30, 18, 22],
    'quantidade': [100, 120, 90, 110, 105],
    'receita': [2000, 3000, 2700, 198, 2310]
}

df = pd.DataFrame(data)

sns.set(style='ticks')
sns.pairplot(df, diag_kind='kde')
plt.suptitle('relaçoes entre preco, quantidade e receita', y=1.02)
plt.show()