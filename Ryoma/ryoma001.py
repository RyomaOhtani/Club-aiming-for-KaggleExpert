#%%
import seaborn as sns
#%%
# データの準備
tips = sns.load_dataset("tips")

# グラフの作成
sns.barplot(x="day", y="total_bill", data=tips)

# グラフの表示
plt.show()
# %%