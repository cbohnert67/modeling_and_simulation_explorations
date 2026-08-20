# 🗳️ Quand la démocratie tourne en rond : le paradoxe de Condorcet expliqué simplement

Imaginez une réunion de famille pour choisir le menu du dimanche. Trois propositions sont sur la table : **Pizza** (Option A), **Burgers** (Option B) et **Sushi** (Option C). 

Chacun vote en toute logique, sans mauvaise foi. Pourtant, à la fin des débats, impossible de trancher. Pire encore : si on compare les plats deux à deux, une majorité préfère la pizza au burger, le burger au sushi... et le sushi à la pizza ! 

Vous venez de tomber dans le **paradoxe de Condorcet**. Ce n'est ni un bug, ni de l'entêtement : c'est un phénomène mathématique fascinant où la logique individuelle se dissout dans le choix collectif.

---

## 👤 Mais qui était ce Condorcet ?

**Nicolas de Condorcet** (1743–1794) était un brillant mathématicien, philosophe et homme politique français du siècle des Lumières. Convaincu que la science et la logique pouvaient améliorer la société et la démocratie, il publie en 1785 un traité révolutionnaire. 

C'est dans cet écrit qu'il démontre que la règle de la majorité simple par duels (comparer les options deux à deux) peut aboutir à des préférences collectives circulaires. En pleine naissance des démocraties modernes, Condorcet jette un pavé dans la mare : **le vote majoritaire peut être fondamentalement instable**.

---

## 🏕️ Le paradoxe en action : l'histoire des vacances entre amis

Pour comprendre comment le groupe devient "fou" alors que chaque individu est cohérent, prenons un cas simple avec 3 amis — Alice, Bob et Charlie — qui choisissent leur destination de vacances :

*   **Alice** préfère la **Mer** 🌊 (1), puis la **Montagne** ⛰️ (2), et enfin la **Ville** 🏛️ (3).
    *   *Sa logique :* $\text{Mer} \succ \text{Montagne} \succ \text{Ville}$
*   **Bob** préfère la **Montagne** ⛰️ (1), puis la **Ville** 🏛️ (2), et enfin la **Mer** 🌊 (3).
    *   *Sa logique :* $\text{Montagne} \succ \text{Ville} \succ \text{Mer}$
*   **Charlie** préfère la **Ville** 🏛️ (1), puis la **Mer** 🌊 (2), et enfin la **Montagne** ⛰️ (3).
    *   *Sa logique :* $\text{Ville} \succ \text{Mer} \succ \text{Montagne}$

Chaque ami a une préférence parfaitement transitive (si Alice préfère la Mer à la Montagne, et la Montagne à la Ville, elle préfère logiquement la Mer à la Ville).

### Faisons les duels !

Pour être le plus équitable possible, comparons les destinations deux à deux :

1.  **Mer contre Montagne :**
    *   Alice vote Mer.
    *   Charlie préfère la Ville, mais entre Mer et Montagne, il choisit la **Mer**.
    *   Bob vote Montagne.
    *   **Résultat :** 2 voix contre 1 pour la **Mer** ! (La majorité préfère la Mer à la Montagne).
2.  **Montagne contre Ville :**
    *   Alice et Bob votent **Montagne**.
    *   Charlie vote Ville.
    *   **Résultat :** 2 voix contre 1 pour la **Montagne** !
3.  **Ville contre Mer :**
    *   Bob et Charlie préfèrent la **Ville** à la Mer.
    *   Alice vote Mer.
    *   **Résultat :** 2 voix contre 1 pour la **Ville** !

### La boucle est bouclée 🔄

Si nous résumons les choix du groupe :
$$\text{Mer} \succ \text{Montagne} \succ \text{Ville} \succ \text{Mer}$$

Le groupe préfère la Mer à la Montagne, la Montagne à la Ville... et la Ville à la Mer ! Le choix collectif tourne en rond. Il n'existe aucun vainqueur incontestable.

---

## 🏛️ Des conséquences bien réelles : politique, entreprise et manipulation

Ce paradoxe n'est pas qu'un jeu de l'esprit. Il se manifeste régulièrement à toutes les échelles.

### 🇬🇧 Le casse-tête historique du Brexit (2018–2019)
Après le référendum de 2016, le Parlement britannique s'est retrouvé complètement paralysé. Trois options s'opposaient :
*   **A** : Annuler le Brexit et rester dans l'UE (*Remain*).
*   **B** : Sortir avec l'accord de Theresa May (*Soft Brexit*).
*   **C** : Partir sans aucun accord (*Hard Brexit / No Deal*).

Les députés étaient divisés en trois blocs irréconciliables. En théorie, l'accord négocié (**B**) battait les autres options en duel individuel. Pourtant, lors des votes réels au Parlement, chaque camp votait stratégiquement contre les options intermédiaires pour faire gagner sa propre vision. Résultat : **le Parlement a rejeté successivement toutes les options**, illustrant la paralysie typique d'un cycle de Condorcet.

### 🏢 Le piège des élections classiques en entreprise
Imaginez une start-up devant choisir sa future ville d'implantation entre **Paris** (A), **Lyon** (B) et **Marseille** (C) :
*   Les commerciaux (42 % de l'équipe) veulent absolument **Paris**.
*   Les développeurs (38 %) veulent **Marseille** pour le cadre de vie.
*   Les financiers (20 %) préfèrent **Lyon** pour le compromis coût/accessibilité.

Si on organise un vote uninominal classique à un tour ("chacun vote pour sa ville préférée") :
1.  Paris obtient 42 % des voix.
2.  Marseille obtient 38 % des voix.
3.  **Lyon** est éliminé d'office avec seulement 20 %.

Pourtant, si on avait fait des duels, **Lyon** aurait écrasé Paris (58 % contre 42 %) et Marseille (62 % contre 38 %). Notre système de vote habituel a éliminé le seul candidat qui mettait tout le monde d'accord !

### 🎛️ Le pouvoir de celui qui fixe l'ordre du jour (Agenda Setting)
Quand il y a un cycle de Condorcet, celui qui décide de l'ordre des votes (le président de séance, le manager...) détient un pouvoir immense : **il peut choisir le vainqueur sans tricher**.

Reprenons nos 3 amis et leurs vacances. Charlie veut à tout prix aller à la **Ville** (C). Il lui suffit d'organiser le vote ainsi :
1.  "On vote d'abord entre la **Mer** (A) et la **Montagne** (B)." (La Mer gagne).
2.  "Maintenant, on vote entre le vainqueur, la **Mer** (A), et la **Ville** (C)." (La Ville gagne !).

Si Alice avait organisé le vote, elle aurait opposé la Montagne et la Ville d'abord, pour faire gagner la Mer à la fin. **Contrôler l'ordre du jour, c'est contrôler le résultat.**

---

## 📊 Que dit la science des données ? (Simulations de Monte-Carlo)

Pour savoir si ce paradoxe est fréquent ou rare, nous avons codé des simulations informatiques. En générant des millions de profils de vote aléatoires (le modèle de la *Culture Impartiale*, où chaque votant choisit ses préférences au hasard), nous avons mesuré la probabilité qu'un cycle apparaisse.

Voici les résultats frappants pour un électorat de taille moyenne (21 votants) :

| Nombre de candidats ($M$) | Risque de tomber sur un cycle (Paradoxe) |
| :---: | :---: |
| **3 candidats** | **~8,8 %** (soit environ 1 vote sur 11) |
| **5 candidats** | **~25,1 %** (soit 1 vote sur 4 !) |
| **7 candidats** | **~36,9 %** (plus d'un tiers du temps) |
| **10 candidats** | **~48,9 %** (presque une chance sur deux) |

> [!IMPORTANT]
> **La leçon des chiffres :** 
> Plus il y a d'options sur la table, plus le risque de paralysie ou de décision incohérente explose. C'est pourquoi il est crucial de limiter le nombre de choix lors d'un vote important.

---

## 🛠️ Comment s'en sortir ? Les alternatives électorales

Puisqu'aucun système de classement traditionnel n'est parfait (un fait prouvé mathématiquement par le **Théorème d'impossibilité d'Arrow**), comment faire pour prendre de bonnes décisions ?

### 1. La méthode Borda (Le système des points)
Comme à l'Eurovision, chaque électeur distribue des points. Si on a 3 candidats, le premier reçoit 3 points, le deuxième 2 points, et le dernier 1 point. On fait la somme.
*   *Avantage :* Fini les cycles, on a toujours un vainqueur clair.
*   *Inconvénient :* Facilement manipulable si on ajoute un candidat "fantôme" uniquement pour piquer des points à un adversaire.

### 2. Le vote alternatif (Instant-Runoff Voting)
Utilisé en Australie, les électeurs classent les candidats. Si personne n'a la majorité absolue au premier tour, on élimine le dernier et on redistribue ses voix à ses deuxièmes choix. On recommence jusqu'à avoir un vainqueur.
*   *Avantage :* Évite d'élire un candidat rejeté par une majorité.
*   *Inconvénient :* Peut quand même éliminer un candidat de consensus très tôt.

### 3. Le Jugement Majoritaire (L'évaluation absolue)
Développé en 2007 par des chercheurs français du CNRS, ce système change tout. **On ne classe plus, on évalue.**
Chaque votant attribue de manière indépendante une mention à chaque candidat : *Excellent, Très Bien, Bien, Passable, Insuffisant, À Rejeter*. Le gagnant est celui qui obtient la meilleure **mention médiane** (celle validée par au moins 50 % des votants).

*   *Avantage :* **Échappe totalement au paradoxe de Condorcet !** En évaluant chaque option par rapport à une échelle absolue plutôt que de les comparer directement, on évite les boucles. C'est sans doute le système le plus robuste et le plus moderne à ce jour.

---

## 💡 Ce qu'il faut retenir pour vos décisions

1.  **L'intransitivité n'est pas une anomalie humaine :** Si votre équipe ne parvient pas à se décider entre trois projets, ce n'est pas parce qu'ils sont difficiles, mais parce que l'agrégation de choix différents est mathématiquement complexe.
2.  **Méfiez-vous du scrutin classique à un tour :** Il favorise les candidats polarisants et élimine souvent les meilleurs compromis.
3.  **Limitez les options :** Plus vous proposez de choix lors d'un vote, plus vous risquez de créer de l'instabilité et de laisser la porte ouverte à la manipulation de l'ordre du jour.
4.  **Explorez de nouveaux formats :** Pour les choix importants en équipe, l'évaluation par mentions (Jugement Majoritaire) ou la distribution de points (Borda) sont bien plus représentatives du consensus réel que le simple vote "Oui/Non".
