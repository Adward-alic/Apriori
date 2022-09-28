import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

data={'ID':[1,2,3,4,5,6],
      "Onion":[1,0,0,1,1,1],
      "Potato":[1,1,0,1,1,1],
      "Burger":[1,1,0,0,1,1],
      "Milk":[0,1,1,1,0,1],
      "Beer":[0,0,1,0,1,0]}

df=pd.DataFrame(data)
df=df[["Onion","Potato","Burger","Milk","Beer"]]

frequent_items= apriori(df,min_support=0.50,use_colnames=True)

rules = association_rules(frequent_items,metric='lift',min_threshold=1)

print(rules)