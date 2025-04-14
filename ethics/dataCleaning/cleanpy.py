import pandas as pd

df = pd.read_csv("/Users/muhammadali/Downloads/crypto_rules_laws_tax_policy_bans-3_results.csv")

#print(df)

filtered_df = df[df["Category"] != "neutral"]

print(filtered_df.head())

negative_sentiment = (filtered_df["Category"] == "negative").sum()
positive_sentiment = (filtered_df["Category"] == "positive").sum()
total = len(filtered_df)

print(f"\nPositive Sentiment: {positive_sentiment}")
print(f"\nNegative Sentiment: {negative_sentiment}")


print(f"\nPositive sentiment: {(positive_sentiment/total)*100:.2f} %")
print(f"Negative sentiment: {(negative_sentiment/total)*100:.2f} %")


print(filtered_df["Category"== "negative"] )