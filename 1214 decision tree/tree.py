import pandas as pd  # 用於處理 CSV 檔案
from sklearn.preprocessing import StandardScaler  # 用於將資料標準化
from sklearn.model_selection import train_test_split  # 用於分割訓練資料集與測試集
from sklearn.tree import DecisionTreeClassifier  # 決策樹分類器 (適用分類資料集) (根據需求引用不同的預測模型: 分類/回歸)

# 讀取檔案
df = pd.read_csv("healthcare_dataset.csv")  # data frame

# 移除無關資料
df = df.drop(['Name', 'Age', 'Date of Admission', 'Doctor', 'Hospital', 
              'Insurance Provider', 'Billing Amount', 'Room Number', 'Discharge Date'], axis=1)

# 利用 LabelEncoder 將類別資料轉為數值資料
from sklearn.preprocessing import LabelEncoder
lc = LabelEncoder()
cols = ['Gender', 'Blood Type', 'Medical Condition', 'Admission Type', 'Medication', 'Test Results']
for i in cols: 
    df[i] = lc.fit_transform(df[i])
df.head()

# 填補清除空值 (略過)
# df.loc[:, df.isnull().any()] = df.loc[:, df.isnull().any()].fillna(df.mean())

# 指定 x, y 資料
dy = df['Test Results']
dx = df.drop(['Test Results'], axis=1)

# 標準化
dx_std = StandardScaler().fit_transform(dx)

# 分割訓練資料集與測試集 (此專案無須此步驟)
dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, train_size=0.15, random_state=0)

# 建立模型
tree = DecisionTreeClassifier()
tree.fit(dx_train, dy_train)

print (tree.score(dx_test, dy_test))

