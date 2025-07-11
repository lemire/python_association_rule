# Exemple de règles d'association

Ce projet illustre comment identifier automatique des règles d'association en Python. Vous pouvez modifier le script pour y mettre vos propres données.

## Prérequis

Avant de procéder, assurez-vous d'installer Python 3.7 ou une version ultérieure sur votre machine.

- **Pour Windows** :
  1. Téléchargez l'installateur depuis https://www.python.org/downloads/windows/
  2. Lancez l'installateur et cochez l'option "Add Python to PATH" avant de cliquer sur "Install Now".
  3. Ouvrez l'invite de commandes :
     - Cliquez sur le menu Démarrer (icône Windows en bas à gauche), tapez "Invite de commandes" ou "cmd", puis cliquez sur l'application correspondante.
  4. Vérifiez l'installation en tapant :
     ```
     python --version
     ```
     ou
     ```
     python3 --version
     ```

- **Pour macOS** :
  1. Ouvrez le Terminal.
  2. Installez Homebrew si ce n'est pas déjà fait :
     ```
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
  3. Installez Python 3 avec Homebrew :
     ```
     brew install python
     ```
  4. Vérifiez l'installation :
     ```
     python3 --version
     ```

Le nom de l'interpréteur Python sur votre système peut être `python` ou `python3` selon votre système. Nous allons supposer qu'il s'agit de `python3`.

## Installation des dépendances (environnement virtuel recommandé)

1. Créez un environnement virtuel dans le dossier du projet :
   ```
   python3 -m venv venv
   ```
2. Activez l'environnement virtuel :
   - **Sur macOS et Linux** :
     ```
     source venv/bin/activate
     ```
   - **Sur Windows** :
     ```
     venv\Scripts\activate
     ```
3. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

Lorsque vous avez terminé, vous pouvez désactiver l'environnement virtuel avec :
```
deactivate
```

## Obtention des fichiers du projet

Pour obtenir les fichiers du projet, vous pouvez télécharger une archive ZIP depuis GitHub :

1. Rendez-vous sur la page du projet : https://github.com/lemire/python_association_rule
2. Cliquez sur le bouton vert « Code » puis sur « Download ZIP ».
3. Décompressez l’archive téléchargée sur votre ordinateur.
4. Ouvrez le dossier extrait dans votre terminal ou explorateur de fichiers pour suivre les instructions d’installation ci-dessus.

## Utilisation

Lancez le script principal :

```
python3 solution.py
```

Le script fournit une analyse des règles d'association pour le jeu de données suivant.

```
        ['Lait', 'Pain', 'Beurre'],
        ['Lait', 'Pain'],
        ['Lait', 'Beurre', 'Œufs'],
        ['Pain', 'Beurre'],
        ['Lait', 'Pain', 'Beurre', 'Œufs']
```

En d'autres termes, un consommateur a acheté du lait, du pain et du beurre. Le suivant
n'a acheté que du lait et du pain. Et ainsi de suite.

## Exemple de résultat
Après exécution, vous verrez dans le terminal une sortie du type :

```
Itemsets fréquents :
    support              itemsets
0       0.8              (Beurre)
1       0.8                (Lait)
2       0.8                (Pain)
3       0.4                (Œufs)
4       0.6        (Beurre, Lait)
5       0.6        (Beurre, Pain)
6       0.4        (Beurre, Œufs)
7       0.6          (Lait, Pain)
8       0.4          (Œufs, Lait)
9       0.4  (Beurre, Lait, Pain)
10      0.4  (Beurre, Œufs, Lait)

Règles d'association :
       antecedents     consequents  support  confidence      lift
0         (Beurre)          (Lait)      0.6    0.750000  0.937500
1           (Lait)        (Beurre)      0.6    0.750000  0.937500
2         (Beurre)          (Pain)      0.6    0.750000  0.937500
3           (Pain)        (Beurre)      0.6    0.750000  0.937500
4           (Œufs)        (Beurre)      0.4    1.000000  1.250000
5           (Lait)          (Pain)      0.6    0.750000  0.937500
6           (Pain)          (Lait)      0.6    0.750000  0.937500
7           (Œufs)          (Lait)      0.4    1.000000  1.250000
8   (Beurre, Lait)          (Pain)      0.4    0.666667  0.833333
9   (Beurre, Pain)          (Lait)      0.4    0.666667  0.833333
10    (Lait, Pain)        (Beurre)      0.4    0.666667  0.833333
11  (Beurre, Œufs)          (Lait)      0.4    1.000000  1.250000
12  (Beurre, Lait)          (Œufs)      0.4    0.666667  1.666667
13    (Œufs, Lait)        (Beurre)      0.4    1.000000  1.250000
14          (Œufs)  (Beurre, Lait)      0.4    1.000000  1.666667
```


## Explication du code

Ce code commence par transformer un ensemble de données de transactions en un format exploitable pour l’analyse des règles d’association. Initialement, les données sont structurées sous forme de dictionnaire et converties en un DataFrame avec `pd.DataFrame(data)`. Ensuite, pour préparer les données à l’algorithme Apriori, elles sont transformées en une matrice binaire (one-hot encoding). Une liste d’items uniques est créée à partir des transactions en utilisant une compréhension de liste et la fonction `set`. Une matrice vide est initialisée avec les transactions comme index et les items comme colonnes, puis remplie de 1 lorsque qu’un item est présent dans une transaction. Cette matrice est convertie en type booléen pour optimiser les calculs ultérieurs.

Dans une deuxième étape, le code applique l’algorithme Apriori, fourni par la bibliothèque `mlxtend`, pour identifier les itemsets fréquents, c’est-à-dire les combinaisons d’items qui apparaissent dans au moins 40 % des transactions (définies par `min_support=0.4`). La fonction `apriori` prend la matrice binaire comme entrée et retourne un DataFrame contenant les itemsets fréquents avec leur support, qui mesure la fréquence relative de chaque combinaison. L’option `use_colnames=True` garantit que les noms des items sont utilisés dans les résultats, facilitant leur interprétation.

Enfin, le code génère des règles d’association à partir des itemsets fréquents en utilisant la fonction `association_rules`. Ces règles identifient des relations du type « si A, alors B » avec une confiance minimale de 60 % (`min_threshold=0.6`), mesurée par la métrique `confidence`. Les résultats affichés incluent les itemsets fréquents et les règles d’association, avec des colonnes clés comme `antecedents` (items de départ), `consequents` (items prédits), `support` (fréquence de la règle), `confidence` (probabilité conditionnelle), et `lift` (force de la règle par rapport à une cooccurrence aléatoire). Cet affichage permet d’analyser les relations significatives entre les items dans les transactions.

## Explication du résultat

Les résultats des itemsets fréquents montrent les combinaisons d’articles achetés ensemble dans au moins 40 % des transactions, selon le seuil de support défini (`min_support=0.4`). Par exemple, le beurre, le lait et le pain ont chacun un support de 0,8, ce qui signifie qu’ils apparaissent dans 80 % des transactions, reflétant leur popularité individuelle. Les combinaisons comme (beurre, lait) ou (lait, pain) ont un support de 0,6, indiquant qu’elles sont achetées ensemble dans 60 % des cas. Des itemsets plus complexes, comme (beurre, lait, pain) ou (beurre, œufs, lait), ont un support de 0,4, montrant qu’ils sont moins fréquents mais toujours significatifs. Ces itemsets révèlent les tendances d’achat courantes, avec des articles comme le beurre, le lait et le pain formant une base d’achats réguliers, souvent complétée par des œufs dans certaines transactions.

Les règles d’association identifient des relations prédictives entre les articles, avec une confiance minimale de 60 % (`min_threshold=0.6`). Par exemple, la règle `(œufs) → (beurre)` a une confiance de 1,0, ce qui signifie que chaque fois que des œufs sont achetés, du beurre est également acheté, avec un lift de 1,25, indiquant une association légèrement plus forte que le hasard. De même, `(œufs) → (lait)` a une confiance de 1,0 et un lift de 1,25. D’autres règles, comme `(beurre) → (lait)` ou `(lait) → (pain)`, ont une confiance de 0,75 et un lift de 0,9375, suggérant une association légèrement moins forte que prévue par hasard. La règle `(beurre, lait) → (œufs)` se distingue avec un lift de 1,6667, indiquant une probabilité significativement plus élevée que les œufs soient achetés lorsque le beurre et le lait sont dans le panier. Ces règles mettent en évidence des relations exploitables entre les articles, bien que certaines associations soient moins fortes (lift proche ou inférieur à 1).

Un commerçant peut utiliser ces données pour optimiser ses stratégies de vente. Par exemple, sachant que les œufs sont fortement associés au beurre et au lait, il pourrait placer ces articles à proximité dans le magasin pour encourager les achats combinés ou proposer des promotions groupées, comme une réduction sur le beurre et le lait lorsque des œufs sont achetés. Les itemsets fréquents, comme (beurre, lait, pain), suggèrent des paniers d’achat typiques, ce qui peut guider la mise en avant de ces produits dans des offres combinées ou des publicités ciblées. De plus, les règles avec un lift élevé, comme `(beurre, lait) → (œufs)`, peuvent être utilisées pour des recommandations personnalisées en ligne ou des suggestions au point de vente, augmentant ainsi les ventes incitatives. Enfin, ces insights peuvent informer la gestion des stocks, en s’assurant que des articles fréquemment achetés ensemble, comme le beurre et le lait, soient toujours disponibles pour répondre à la demande.


## Références

- Lemire et al., [La science des données: Théorie et applications avec R et Python](https://www.amazon.ca/science-donn%C3%A9es-Th%C3%A9orie-applications-Python/dp/B0D53QXGKM)
- Robert Godin et Daniel Lemire, [Programmation avec Python: des jeux au Web](https://www.amazon.ca/Programmation-avec-Python-jeux-Web/dp/B0CVX9296P)




