import pandas as pd
import numpy as np

orders = [
    {"User Id": "User 1", "Dok Id": "Dok 1"},
    {"User Id": "User 1", "Dok Id": "Dok 3"},
    {"User Id": "User 1", "Dok Id": "Dok 7"},
    {"User Id": "User 1", "Dok Id": "Dok 6"},
    {"User Id": "User 2", "Dok Id": "Dok 2"},
    {"User Id": "User 2", "Dok Id": "Dok 3"},
    {"User Id": "User 2", "Dok Id": "Dok 4"},
    {"User Id": "User 2", "Dok Id": "Dok 6"},
    {"User Id": "User 2", "Dok Id": "Dok 7"},
    {"User Id": "User 3", "Dok Id": "Dok 1"},
    {"User Id": "User 3", "Dok Id": "Dok 3"},
    {"User Id": "User 3", "Dok Id": "Dok 5"},
    {"User Id": "User 3", "Dok Id": "Dok 6"},
    {"User Id": "User 3", "Dok Id": "Dok 8"},
    {"User Id": "User 4", "Dok Id": "Dok 2"},
    {"User Id": "User 4", "Dok Id": "Dok 4"},
    {"User Id": "User 4", "Dok Id": "Dok 5"},
    {"User Id": "User 4", "Dok Id": "Dok 6"},
    {"User Id": "User 4", "Dok Id": "Dok 7"},
    {"User Id": "User 4", "Dok Id": "Dok 8"},
    {"User Id": "User 5", "Dok Id": "Dok 1"},
    {"User Id": "User 5", "Dok Id": "Dok 2"},
    {"User Id": "User 5", "Dok Id": "Dok 3"},
    {"User Id": "User 5", "Dok Id": "Dok 4"},
    {"User Id": "User 5", "Dok Id": "Dok 5"},
    {"User Id": "User 5", "Dok Id": "Dok 8"},
    {"User Id": "User 6", "Dok Id": "Dok 1"},
    {"User Id": "User 6", "Dok Id": "Dok 4"},
    {"User Id": "User 6", "Dok Id": "Dok 5"},
    {"User Id": "User 6", "Dok Id": "Dok 7"},
    {"User Id": "User 6", "Dok Id": "Dok 8"},
]

df = pd.DataFrame(orders)
print(df.head())

documents = df["Dok Id"].unique()

similarity_matrix = pd.DataFrame(0, index=documents, columns=documents)

for doc1 in documents:
    for doc2 in documents:
        if doc1 != doc2:
            users_doc1 = set(df[df["Dok Id"] == doc1]["User Id"])
            users_doc2 = set(df[df["Dok Id"] == doc2]["User Id"])
            similarity_matrix.loc[doc1, doc2] = len(users_doc1 & users_doc2) / len(users_doc1)

print("\n\n\nМатрица подобия:")
print(similarity_matrix)

def recommend_for_user(user_docs, similarity_matrix, top_n=3):
    recommendations = {}
    for doc in similarity_matrix.index:
        if doc not in user_docs:
            score = sum(
                similarity_matrix.loc[doc, other_doc]
                for other_doc in user_docs
                if other_doc in similarity_matrix.columns
            ) / len(user_docs)
            recommendations[doc] = score
    return sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:top_n]

user_docs = ["Dok 1", "Dok 5", "Dok 8"]
recommendations = recommend_for_user(user_docs, similarity_matrix, top_n=3)

print("\n\n\nРекомендации для пользователя:")
for doc, score in recommendations:
    print(f"{doc}: {score:.2f}")

input('')