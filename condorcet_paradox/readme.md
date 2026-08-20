# 🗳️ Modélisation et Simulation Numérique du Paradoxe de Condorcet

Une analyse théorique, algorithmique et empirique de l'intransitivité des choix collectifs et du paradoxe de Condorcet à l'aide de simulations de Monte-Carlo.

---

## 📌 Présentation du Projet

Théorisé en 1785 par Nicolas de Condorcet, le paradoxe du vote montre que l'agrégation de choix individuels parfaitement rationnels et transitifs ($A \succ B \succ C$) peut générer une préférence collective cyclique ($A \succ B \succ C \succ A$). En l'absence de vainqueur légitime, la décision devient instable et particulièrement vulnérable à la manipulation de l'ordre du jour (*agenda setting*).

Ce projet offre un cadre complet pour étudier ce phénomène :

*   **Un module Python Orienté Objet** ([`src/condorcet.py`](src/condorcet.py)) permettant de représenter des électeurs, d'évaluer des duels par paires, d'exécuter l'algorithme DFS de détection de cycles et de lancer des simulations de Monte-Carlo.
*   **Une suite de tests unitaires** avec Pytest ([`tests/test_condorcet.py`](tests/test_condorcet.py)) garantissant la qualité et la robustesse des algorithmes.
*   **Un Notebook Jupyter interactif** ([`notebooks/condorcet_paradox_exploration.ipynb`](notebooks/condorcet_paradox_exploration.ipynb)) pour expérimenter avec des cas concrets (politique, entreprise) et générer des cartes thermiques/graphiques.
*   **Un article de fond exhaustif** ([`article.md`](article.md)) détaillant la théorie mathématique, le théorème d'impossibilité d'Arrow, les applications réelles et les alternatives électorales (Borda, Jugement Majoritaire, IRV).

---

## 📂 Architecture du Projet

```text
condorcet_paradox/
│
├── article.md                                # Article de fond complet et vulgarisé
├── README.md                                 # Documentation du sous-projet
│
├── src/
│   ├── __init__.py
│   └── condorcet.py                          # Classes POO (Candidate, Voter, Tournament, Simulation)
│
├── tests/
│   ├── __init__.py
│   └── test_condorcet.py                     # Tests unitaires Pytest
│
├── notebooks/
│   └── condorcet_paradox_exploration.ipynb   # Notebook interactif & visualisations
│
└── assets/
    └── condorcet_simulation_results.png     # Visualisations graphiques et heatmaps
```

---

## ⚙️ Installation & Prérequis

### 1. Cloner le dépôt

```bash
git clone https://github.com/cbohnert67/modeling_and_simulation.git
cd modeling_and_simulation/condorcet_paradox
```

### 2. Configurer l'environnement virtuel

Si ce n'est pas déjà fait à la racine du projet :

```bash
python -m venv ../.venv

# Windows (PowerShell)
..\.venv\Scripts\Activate.ps1

# Linux / macOS
source ../.venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install numpy pandas matplotlib seaborn pytest notebook
```

---

## 🚀 Utilisation & Exécution

### Exécuter les tests unitaires

Depuis le répertoire `condorcet_paradox` :

```bash
python -m pytest
```

### Utiliser le module Python en script direct

```bash
python src/condorcet.py
```

### Exemple d'intégration dans votre propre code :

```python
from src.condorcet import Candidate, Voter, Tournament

# Création des alternatives
a, b, c = Candidate("A"), Candidate("B"), Candidate("C")

# Profil de préférences cyclique
voters = [
    Voter(1, [a, b, c]),
    Voter(2, [b, c, a]),
    Voter(3, [c, a, b])
]

# Analyse du tournoi
tournament = Tournament([a, b, c], voters)

print("Vainqueur de Condorcet :", tournament.get_condorcet_winner())  # None
print("Présence d'un cycle :", tournament.has_cycle())               # True
```

### Explorer le Notebook Jupyter

```bash
jupyter notebook notebooks/condorcet_paradox_exploration.ipynb
```

---

## 📊 Principaux Résultats de Simulation

Sous l'hypothèse de l'**Impartial Culture** (où tous les ordres de préférence stricts sont équiprobables), les simulations de Monte-Carlo démontrent que :

*   **Impact majeur du nombre d'alternatives ($M$)** : La probabilité qu'un cycle apparaisse croît de manière spectaculaire avec le nombre de candidats :
    *   $M = 3$ candidats : **~8,7 %**
    *   $M = 5$ candidats : **~25,1 %**
    *   $M = 7$ candidats : **> 80 %**
*   **Stabilité selon la taille de l'électorat ($N$)** : Dès que $N \ge 31$ votants, la probabilité se stabilise autour de la limite théorique asymptotique ($N \to \infty$). Un grand corps électoral ne protège pas contre l'intransitivité collective.

---

## 📄 License

Ce projet est distribué sous licence **MIT**. Libre d'utilisation et de réutilisation pour vos travaux académiques ou personnels.