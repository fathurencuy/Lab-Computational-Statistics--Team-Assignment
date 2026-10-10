
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score

# Load Boston Housing dataset
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(
    data_url, sep=r"\s+", skiprows=22, header=None
)

# Prepare dataset
data = np.hstack([
    raw_df.values[::2, :],
    raw_df.values[1::2, :2]
])
target = raw_df.values[1::2, 2]

columns = [
    "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM",
    "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"
]

df = pd.DataFrame(data, columns=columns)
df["MEDV"] = target

# Build regression models
model1 = smf.ols(
    "MEDV ~ RM + LSTAT", data=df
).fit()

model2 = smf.ols(
    "MEDV ~ RM + LSTAT + PTRATIO + AGE", data=df
).fit()

# Calculate AIC
print("AIC Model 1:", model1.aic)
print("AIC Model 2:", model2.aic)

# Prepare 5-fold cross-validation
X1 = df[["RM", "LSTAT"]]
X2 = df[["RM", "LSTAT", "PTRATIO", "AGE"]]
y = df["MEDV"]

cv = KFold(n_splits=5, shuffle=True, random_state=42)

# Model 1
scores1 = -cross_val_score(
    LinearRegression(), X1, y,
    cv=cv, scoring="neg_mean_squared_error"
)
rmse1 = np.sqrt(scores1)

# Model 2
scores2 = -cross_val_score(
    LinearRegression(), X2, y,
    cv=cv, scoring="neg_mean_squared_error"
)
rmse2 = np.sqrt(scores2)

print("\nModel 1 Mean CV RMSE:", rmse1.mean())
print("Model 2 Mean CV RMSE:", rmse2.mean())
