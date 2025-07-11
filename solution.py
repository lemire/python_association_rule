import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Créer un ensemble de données d'exemple (transactions d'achats)
data = {
    'Transaction': ['T1', 'T2', 'T3', 'T4', 'T5'],
    'Items': [
        ['Lait', 'Pain', 'Beurre'],
        ['Lait', 'Pain'],
        ['Lait', 'Beurre', 'Œufs'],
        ['Pain', 'Beurre'],
        ['Lait', 'Pain', 'Beurre', 'Œufs']
    ]
}

# Convertir en DataFrame
df = pd.DataFrame(data)

# Transformer les données en format one-hot encoding
# Créer une liste de tous les items uniques
all_items = sorted(set(item for sublist in df['Items'] for item in sublist))
# Initialiser une matrice binaire
one_hot = pd.DataFrame(0, index=df['Transaction'], columns=all_items)
for idx, items in zip(df['Transaction'], df['Items']):
    for item in items:
        one_hot.loc[idx, item] = 1

# Convertir la matrice binaire en types booléens
one_hot = one_hot.astype(bool)

# Appliquer l'algorithme Apriori pour trouver les itemsets fréquents
frequent_itemsets = apriori(one_hot, min_support=0.4, use_colnames=True)

# Générer les règles d'association
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

# Afficher les résultats
print("Itemsets fréquents :")
print(frequent_itemsets)
print("\nRègles d'association :")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])