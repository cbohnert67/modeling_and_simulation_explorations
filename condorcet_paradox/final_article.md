# Quand la démocratie tourne en rond : comprendre le paradoxe de Condorcet par la théorie, la vie réelle et le code

## 1. L'illusion de la rationalité collective

### La réunion dont personne ne sort gagnant

Imaginez une réunion de comité de direction : trois projets stratégiques sont soumis au vote. L'équipe est motivée, le processus est démocratique et équitable, chaque membre exprime un choix clair, structuré et logique. Pourtant, au terme du vote, le projet retenu semble rejeté par une majorité de l'équipe. Plus déroutant encore : si l'on rejouait le scrutin en comparant les options deux à deux, aucune décision ne tiendrait la route. L'option A battrait l'option B, B battrait C, et C battrait A.

Ce phénomène n'est ni un bug procédural, ni une marque de mauvaise foi des participants. Il s'agit d'une propriété mathématique fondamentale de la prise de décision collective.

### Le problème fondamental : quand l'agrégation détruit la logique

En théorie de la décision et en sciences politiques, nous faisons souvent l'hypothèse qu'agréger des choix individuels rationnels produit naturellement une décision collective rationnelle. Or, ce principe s'effondre dès lors qu'un groupe doit choisir entre au moins trois options sur la base de critères multidimensionnels.

Un individu est dit rationnel lorsque ses préférences sont transitives : s'il préfère l'option $A$ à l'option $B$ ($A \succ B$) et l'option $B$ à l'option $C$ ($B \succ C$), alors il préfère logiquement l'option $A$ à l'option $C$ ($A \succ C$). Cependant, au niveau du groupe, la majorité peut simultanément préférer $A$ à $B$, $B$ à $C$, et $C$ à $A$. La rationalité individuelle se dissout dans l'agrégation : la collectivité devient intransitive.

### Nicolas de Condorcet et les Lumières

Ce phénomène porte le nom de Nicolas de Condorcet (1743–1794), mathématicien, philosophe et homme politique français. Figure éminente des Lumières et membre de l'Académie des sciences, Condorcet s'intéresse à l'application des mathématiques aux sciences sociales et morales.

En 1785, dans son célèbre Essai sur l’application de l’analyse à la probabilité des décisions rendues à la pluralité des voix, il formalise pour la première fois cette anomalie : le paradoxe de Condorcet (ou paradoxe du vote). À une époque où s'élaborent les fondements des systèmes démocratiques modernes, Condorcet démontre rigoureusement que le vote à la majorité simple par paires peut déboucher sur une absence totale de vainqueur légitime, créant une boucle décisionnelle infinie.

### Objectifs de cet article et démarche

Cet article de fond propose une exploration complète du paradoxe de Condorcet, articulée autour de trois axes :

1. Les fondements mathématiques : démonstration algébrique, interprétation en théorie des graphes et lien avec le théorème d'impossibilité d'Arrow.

2. Les manifestations dans le monde réel : analyse de cas concrets en politique (le casse-tête du Brexit), en gestion d'entreprise et dans les choix quotidiens.

3. La modélisation numérique : implémentation en Python d'un moteur de simulation de Monte-Carlo pour évaluer la probabilité statistique réelle d'apparition d'un cycle majoritaire.

## 2. Les fondements mathématiques du paradoxe

Pour comprendre pourquoi l'agrégation de choix individuels peut aboutir à des cycles décisionnels, il est nécessaire de formaliser le concept de préférence et d'examiner la transition entre la rationalité d'un individu et la rationalité d'un groupe.

### 2.1. L'hypothèse de transitivité individuelle

Soit $C = \{A, B, C, \dots\}$ l'ensemble fini des candidats ou alternatives disponibles, et $V = \{V_1, V_2, \dots, V_N\}$ l'ensemble des $N$ votants.

Chaque votant $i \in V$ exprime ses préférences individuelles sous la forme d'une relation binaire de préférence stricte, notée $\succ_i$. Pour deux alternatives quelconques $X, Y \in C$, la notation $X \succ_i Y$ signifie que le votant $i$ préfère strictement l'option $X$ à l'option $Y$.

En théorie de la décision canonique, la rationalité d'un individu repose sur deux axiomes fondamentaux :

La complétude : Pour tout couple $(X, Y) \in C^2$ avec $X \neq Y$, le votant est capable de comparer les deux options, c'est-à-dire que soit $X \succ_i Y$, soit $Y \succ_i X$ (en excluant ici l'indifférence pour simplifier).

La transitivité : Pour tout triplet $(X, Y, Z) \in C^3$, si le votant préfère $X$ à $Y$ et $Y$ à $Z$, alors il préfère nécessairement $X$ à $Z$ :


$$X \succ_i Y \quad \text{et} \quad Y \succ_i Z \implies X \succ_i Z$$

Un individu dont la relation de préférence satisfait la complétude et la transitivité possède un ordre total strict sur l'ensemble des candidats. Ses choix sont parfaitement cohérents : il n'y a aucune contradiction interne.

### 2.2. La rupture au niveau collectif : Démonstration algébrique de l'intransitivité

Considérons maintenant une règle d'agrégation collective basée sur le vote à la majorité simple par paires (la règle de Condorcet).

Définissons la relation de préférence collective $\succ_{P}$ telle que, pour deux options $X, Y \in C$, $X \succ_{P} Y$ si et seulement si une majorité stricte de votants préfère $X$ à $Y$. Mathématiquement :


$$X \succ_{P} Y \iff \Big\vert{}\{i \in V \mid X \succ_i Y\}\Big\vert{} > \Big\vert{}\{i \in V \mid Y \succ_i X\}\Big\vert{}$$

#### La démonstration algébrique classique (3 votants, 3 candidats)

Soit un électorat composé de $N = 3$ votants $V = \{V_1, V_2, V_3\}$ devant choisir parmi $M = 3$ alternatives $C = \{A, B, C\}$.

Supposons les ordres de préférence individuels suivants :

* Votant 1 ($V_1$) : $A \succ_1 B \succ_1 C$

* Votant 2 ($V_2$) : $B \succ_2 C \succ_2 A$

* Votant 3 ($V_3$) : $C \succ_3 A \succ_3 B$

Chaque votant respecte individuellement la transitivité (par exemple, pour $V_1$, $A \succ_1 B$ et $B \succ_1 C \implies A \succ_1 C$).

Procédons à l'évaluation des duels majoritaires deux à deux :

1. Duel $A$ contre $B$ :

* $V_1$ préfère $A$ à $B$ ($A \succ_1 B$).

* $V_2$ préfère $B$ à $A$ ($B \succ_2 A$).

* $V_3$ préfère $A$ à $B$ ($A \succ_3 B$).

Décompte : 2 voix pour $A$, 1 voix pour $B$.

Résultat collectif : $A \succ_{P} B$ (la majorité préfère $A$ à $B$).

2. Duel $B$ contre $C$ :

* $V_1$ préfère $B$ à $C$ ($B \succ_1 C$).

* $V_2$ préfère $B$ à $C$ ($B \succ_2 C$).

* $V_3$ préfère $C$ à $B$ ($C \succ_3 B$).

Décompte : 2 voix pour $B$, 1 voix pour $C$.

Résultat collectif : $B \succ_{P} C$ (la majorité préfère $B$ à $C$).

3. Duel $C$ contre $A$ :

* $V_1$ préfère $A$ à $C$ ($A \succ_1 C$).

* $V_2$ préfère $C$ à $A$ ($C \succ_2 A$).

* $V_3$ préfère $C$ à $A$ ($C \succ_3 A$).

Décompte : 2 voix pour $C$, 1 voix pour $A$.

Résultat collectif : $C \succ_{P} A$ (la majorité préfère $C$ à $A$).

#### Conclusion algébrique

En regroupant les résultats collectifs, nous obtenons le système de relations :


$$A \succ_{P} B \quad \text{et} \quad B \succ_{P} C \quad \text{et} \quad C \succ_{P} A$$

Si la relation collective $\succ_{P}$ était transitive, alors $A \succ_{P} B$ et $B \succ_{P} C$ impliqueraient $A \succ_{P} C$. Or, le scrutin produit au contraire $C \succ_{P} A$.

La relation d'agrégation majoritaire est donc intransitive. Elle forme un cycle fermé :


$$A \succ_{P} B \succ_{P} C \succ_{P} A$$

C'est la démonstration rigoureuse du paradoxe de Condorcet : l'agrégation de préférences individuelles transitives par la règle de la majorité simple peut générer une préférence collective cyclique et incohérente.

### 2.3. L'interprétation en théorie des Graphes : le Tournoi orienté

En théorie des graphes, le résultat d'un vote par duels majoritaires entre $M$ candidats se modélise naturellement sous la forme d'un graphe orienté $G = (C, E)$, appelé un tournoi :

Les sommets $C$ représentent l'ensemble des candidats.

Les arcs orientés $E$ représentent les victoires en duel direct. Un arc orienté $(X, Y) \in E$ existe si et seulement si $X \succ_{P} Y$.

     (A)
    /   \
   v     \
  (B)----> (C)
    ^     /
     \   v
      ---

(Représentation simplifiée d'un cycle de Condorcet : $A \to B \to C \to A$)

#### Propriétés graphiques et détection du paradoxe

1. Unanimité ou Vainqueur de Condorcet :
Un candidat $K^* \in C$ est appelé Vainqueur de Condorcet s'il correspond à une source dans le graphe (ou un sommet avec un degré sortant $d^+(K^*) = M - 1$). Cela signifie qu'il existe un arc orienté allant de $K^*$ vers tous les autres sommets du graphe.

2. Présence de cycle majoritaire :
En l'absence de vainqueur de Condorcet, le graphe contient au moins un circuit orienté (ou sous-graphe fortement connexe). L'existence du paradoxe de Condorcet équivaut algébriquement à la présence d'au moins un cycle hamiltonien ou d'une boucle fermée dans le tournoi.

Du point de vue algorithmique, vérifier si un scrutin souffre du paradoxe de Condorcet consiste à :

* Construire la matrice d'adjacence du tournoi à partir des duels.

* Exécuter un algorithme de détection de cycles (tel qu'un parcours en profondeur DFS avec coloration à 3 états) ou vérifier l'absence d'un sommet de degré sortant maximal $M - 1$.

### 2.4. Lien avec le Théorème d'Impossibilité d'Arrow

Le paradoxe de Condorcet n'est pas un défaut isolé de la règle de majorité simple ; il est la manifestation d'une limite structurelle plus profonde de tous les systèmes de choix collectif, formalisée en 1951 par l'économiste Kenneth Arrow.

Le Théorème d'impossibilité d'Arrow stipule qu'il est rigoureusement impossible de concevoir un système de vote (une fonction de choix social) agrégeant des préférences individuelles en une préférence collective rationnelle, dès lors qu'il y a au moins 3 candidats et qu'on exige le respect simultané des 5 conditions minimales suivantes :

1. Domaine universel (Universalité) : La règle doit pouvoir traiter tous les profils de préférences individuelles transitives possibles.

2. Non-dictature : Il ne doit pas exister un unique votant dont les préférences dictent systématiquement le choix collectif indépendamment des autres.

3. Efficacité au sens de Pareto (Paretovité) : Si tous les votants préfèrent strictement $X$ à $Y$, alors la collectivité doit préférer $X$ à $Y$.

4. Indépendance vis-à-vis des options non pertinentes (IIA) : La préférence collective entre $X$ et $Y$ ne doit dépendre que des préférences individuelles relatives à $X$ et $Y$, sans être influencée par la présence ou l'absence d'une troisième option $Z$.

5. Transitivité collective (Rationalité) : L'agrégation doit toujours produire un ordre collectif sans cycles ($A \succ B \succ C \implies A \succ C$).

#### La portée du résultat

La règle de majorité simple de Condorcet respecte le Domaine universel, la Non-dictature, la Paretovité et l'Indépendance vis-à-vis des options non pertinentes (IIA). Par conséquent, le théorème d'Arrow démontre mathématiquement que la majorité simple doit nécessairement renoncer à la transitivité collective dans certains cas de figure.

Le paradoxe de Condorcet est donc une illustration directe de l'impossibilité d'Arrow : la quête du système de vote "parfait" est une impossibilité mathématique dès que l'on cherche à agréger des choix multidimensionnels.

## 3. Le Paradoxe dans la vie de tous les jours et la politique

Bien loin de se limiter aux grimoires de mathématiques pures, le paradoxe de Condorcet se manifeste régulièrement dès qu’une collectivité — qu'il s'agisse d'un électorat national, d'un conseil d'administration ou d'un groupe d'amis — doit arbitrer entre au moins trois options irréconciliables.

Dans cette section, nous explorons trois domaines concrets où l'intransitivité des préférences collectives crée des situations d'impasse, d'instabilité ou de manipulation.

### 3.1. En politique : Le casse-tête du Brexit (Royaume-Uni, 2018–2019)

L'un des exemples modernes les plus frappants d'un blocage de Condorcet à grande échelle est la séquence parlementaire britannique qui a suivi le référendum de 2016 sur le Brexit.

Entre 2018 et 2019, la Chambre des communes devait s'accorder sur la marche à suivre concernant la sortie de l'Union européenne. Les débats s'articulaient principalement autour de trois options fondamentales :

* Option $A$ (Remain) : Annuler le Brexit et maintenir le Royaume-Uni dans l'Union européenne.

* Option $B$ (Soft Brexit / May's Deal) : Mettre en œuvre l'accord de retrait négocié par la Première ministre Theresa May (maintien dans une union douanière ou compromis réglementaire).

* Option $C$ (Hard Brexit / No Deal) : Rompre brutalement sans accord avec l'UE, en s'en remettant uniquement aux règles de l'OMC.

#### La fragmentation de la Chambre des Communes

Le Parlement était alors divisé en trois blocs principaux d'élus, chacun guidé par une échelle de valeurs distincte :

1. Les Pro-Européens / Maintien (environ 40 % des sièges) :

* Préférence : $A \succ_1 B \succ_1 C$

* Leur choix idéal est le maintien ($A$). S'il faut absolument sortir, ils préfèrent un accord ordonné et doux ($B$) à un choc économique sans accord ($C$).

2. Les Brexiteurs durs / Souverainistes (environ 35 % des sièges) :

* Préférence : $C \succ_2 B \succ_2 A$

* Leur priorité est la rupture nette ($C$). Si un accord doit exister, ils préfèrent le compromis de May ($B$) à l'annulation du Brexit ($A$), perçue comme un déni démocratique.

3. Les Modérés / Loyalistes du gouvernement (environ 25 % des sièges) :

* Préférence : $B \succ_3 A \succ_3 C$

* Leur priorité est de respecter le vote populaire par le biais de l'accord officiel ($B$). En cas d'échec de cet accord, ils redoutent le chaos d'un No Deal et préfèrent temporiser ou annuler ($A$) plutôt que d'affronter l'option $C$.

#### Décompte des duels majoritaires

Mettons ces trois options en compétition deux à deux selon la règle de la majorité simple :

* Duel $A$ (Remain) vs $B$ (May's Deal) :

- Les Pro-Européens (40 %) votent pour $A$.

- Les Brexiteurs durs (35 %) et les Modérés (25 %) préfèrent $B$ à $A$.

- Résultat : $B$ l'emporte sur $A$ avec 60 % des voix ($B \succ_P A$).

* Duel $B$ (May's Deal) vs $C$ (No Deal) :

- Les Pro-Européens (40 %) et les Modérés (25 %) préfèrent $B$ à $C$.

- Les Brexiteurs durs (35 %) votent pour $C$.

- Résultat : $B$ l'emporte sur $C$ avec 65 % des voix ($B \succ_P C$).

Ici, l'option $B$ semble émerger comme une solution de compromis. Mais au sein de l'agenda parlementaire, lorsque l'option $A$ est directement opposée à $C$ sur le principe fondamental du maintien ou du départ :

* Duel $C$ (No Deal) vs $A$ (Remain) :

- Les Brexiteurs durs (35 %) et les Modérés (25 %) préfèrent... Attendons : pour le groupe 3 (Modérés), la préférence est $B \succ_3 A \succ_3 C$. Ils préfèrent donc $A$ à $C$ !

- Recomptons : Les Pro-Européens (40 %) + les Modérés (25 %) préfèrent $A$ à $C$.

- Résultat : $A$ l'emporte sur $C$ avec 65 % des voix ($A \succ_P C$).

Dans cette configuration précise, l'option $B$ apparaît comme un Vainqueur de Condorcet net ($B \succ_P A$ et $B \succ_P C$). Pourtant, lors des votes d'orientation de mars 2019 (indicative votes), le Parlement a rejeté toutes les options une par une lorsqu'elles étaient soumises au vote uninominal (Oui/Non).

Pourquoi ? Parce que chaque camp votait contre les options qui n'étaient pas son premier choix pour forcer la main aux autres. Cet épisode démontre que même en présence d'un vainqueur potentiel de Condorcet, le vote option par option sans structuration préférentielle mène à la paralysie.

### 3.2. En entreprise : l'arbitrage d'un comité stratégique

Considérons une entreprise de technologie de 120 salariés devant choisir l'emplacement de son futur siège social entre trois villes :

* Option $A$ (Paris) : Fort prestige commercial et vivier de talents, mais loyers très élevés et petits espaces.

* Option $B$ (Lyon) : Compromis équilibré entre coût, qualité de vie et accessibilité TGV.

* Option $C$ (Marseille) : Faible coût immobilier, cadre de vie exceptionnel (mer) et grands espaces, mais plus éloigné des clients historiques.

#### La structure des départements

La décision est confiée aux représentants des trois grands paires de services :

1.Équipe Commerciale & Direction (50 voix - 41,7 %) :

* Priorité : Image de marque et réseaux.

* Ordre : $A \succ_1 B \succ_1 C$

2.Équipe R&D & Tech (45 voix - 37,5 %) :

* Priorité : Cadre de vie et pouvoir d'achat immobilier.

* Ordre : $C \succ_2 B \succ_2 A$

3. Équipe Finance & Logistique (25 voix - 20,8 %) :

* Priorité : Optimisation des coûts opérationnels et centralité.

* Ordre : $B \succ_3 C \succ_3 A$

#### Évaluation des duels majoritaires

* Duel Paris ($A$) vs Lyon ($B$) :

- Préfèrent $A$ à $B$ : Commercial/Direction (50 voix).

- Préfèrent $B$ à $A$ : Tech (45 voix) + Finance (25 voix) = 70 voix.

- Résultat : $B \succ_P A$ (58,3 % contre 41,7 %).

* Duel Lyon ($B$) vs Marseille ($C$) :

- Préfèrent $B$ à $C$ : Commercial/Direction (50 voix) + Finance (25 voix) = 75 voix.

- Préfèrent $C$ à $B$ : Tech (45 voix).

- Résultat : $B \succ_P C$ (62,5 % contre 37,5 %).

* Duel Marseille ($C$) vs Paris ($A$) :

- Préfèrent $C$ à $A$ : Tech (45 voix) + Finance (25 voix) = 70 voix.

- Préfèrent $A$ à $C$ : Commercial/Direction (50 voix).

- Résultat : $C \succ_P A$ (58,3 % contre 41,7 %).

#### Analyse du résultat

En regroupant les duels, nous observons :


$$B \succ_P A \quad \text{et} \quad B \succ_P C \quad \text{et} \quad C \succ_P A$$

Ici, Lyon ($B$) est un Vainqueur de Condorcet parfait : il bat la capitale ($A$) et Marseille ($C$) dans tous les affrontements directs.

Pourtant, si la direction choisissait d'organiser un vote uninominal à un tour classique (« Chaque salarié vote pour sa ville préférée ») :

* Paris ($A$) obtiendrait 50 voix (41,7 %).

* Marseille ($C$) obtiendrait 45 voix (37,5 %).

* Lyon ($B$) obtiendrait seulement 25 voix (20,8 %) et serait éliminé immédiatement !

Cet exemple illustre une vérité contre-intuitive essentielle : le scrutin uninominal classique peut éliminer le candidat qui aurait pourtant battu tous les autres en duel direct.

### 3.3. Dans la vie quotidienne : Le piège de l'Agenda Setting (L'Ordre du jour)

Le paradoxe de Condorcet ne touche pas seulement les institutions politiques ou les grandes entreprises ; il s'invite dans nos décisions de tous les jours.

Imaginons trois amis — Alice ($V_1$), Bob ($V_2$) et Charlie ($V_3$) — organisant leurs vacances d'été. Ils doivent choisir entre trois destinations :

* $A$ : Séjour à la Mer (Plage et animation).

* $B$ : Randonnée à la Montagne (Sport et nature).

* $C$ : Séjour Culturel dans une capitale européenne (Musées et gastronomie).

#### Le profil des amis

* Alice ($V_1$) : $A \succ_1 B \succ_1 C$ (Elle adore la mer, tolère la montagne, déteste les musées l'été).

* Bob ($V_2$) : $B \succ_2 C \succ_2 A$ (Il veut du grand air, préfère les villes à la plage).

* Charlie ($V_3$) : $C \succ_3 A \succ_3 B$ (Passioñné d'histoire, il préfère la plage à l'effort physique).

Comme démontré dans la section 2, ce profil produit le cycle parfait de Condorcet :

$$A \succ_P B \succ_P C \succ_P A$$

#### Le pouvoir de l'organisateur (Agenda Setting)

Puisqu'il existe un cycle, il n'y a pas de gagnant naturel. Le résultat final va dépendre entièrement de la procédure de vote choisie et de l'ordre dans lequel les options sont éliminées.

Supposons que Charlie soit chargé d'animer la réunion et propose une procédure d'élimination successive :

          Étape 1                     Étape 2
   (Vote entre 2 options)    (Le gagnant contre la 3e)

        Mer (A) vs Montagne (B)
                 |
                 v
             Gagnant : A  ───────> Mer (A) vs Culture (C)
                                           |
                                           v
                                      VAINQUEUR FINAL : C

1. Étape 1 : Charlie fait voter la Mer ($A$) contre la Montagne ($B$). Alice et Charlie préfèrent $A$ à $B$. La Mer ($A$) l'emporte.

2. Étape 2 : Charlie oppose le vainqueur ($A$) à son option préférée, la Culture ($C$). Bob et Charlie préfèrent $C$ à $A$. La Culture ($C$) l'emporte et devient le choix final !

Si Alice avait fixé l'ordre du jour : Elle aurait d'abord opposé la Montagne ($B$) à la Culture ($C$) (victoire de $B$), puis la Montagne ($B$) à la Mer ($A$). La Mer ($A$) l'aurait emporté !

#### Leçon sur la manipulation procédurale

En présence d'un cycle de Condorcet, celui qui contrôle l'ordre de présentation des votes (le « maître de l'agenda » ou agenda setter) possède le pouvoir absolu de déterminer le vainqueur final sans modifier le vote d'aucun participant.

## 4. Modélisation et simulation numérique (Monte-Carlo)

Si le paradoxe de Condorcet se produit dans des exemples théoriques ou historiques ciblés, une question fondamentale se pose pour les décideurs, politologues et data scientists : quelle est la probabilité réelle qu'un tel cycle d'intransitivité survienne lors d'un vote ?

Pour répondre à cette question sans dépendre uniquement des analyses combinatoires complexes, nous faisons appel aux simulations de Monte-Carlo. Cette méthode permet d'estimer des fréquences statistiques en générant un grand nombre d'électorats synthétiques et en mesurant la récurrence des cycles.

### 4.1. Le modèle probabiliste : Impartial Culture (IC)

Dans la littérature en théorie du choix social (notamment les travaux de Garman, Kamien et Fishburn), le modèle de référence pour simuler des préférences individuelles est le modèle de la Culture Impartiale (Impartial Culture ou IC).

#### Principes du modèle Impartial Culture

Soit un ensemble de $M$ candidats, il existe $M!$ (factoielle $M$) ordres de préférences stricts possibles.

Pour $M = 3$ candidats $\{A, B, C\}$, il existe $3! = 6$ permutations distinctes :


$$A \succ B \succ C, \quad A \succ C \succ B, \quad B \succ A \succ C, \quad B \succ C \succ A, \quad C \succ A \succ B, \quad C \succ B \succ A$$

Chaque votant choisit son ordre de préférence de manière indépendante et équiprobable parmi les $M!$ configurations possibles.

La probabilité pour un votant attribué d'exprimer un ordre spécifique est égale à $\frac{1}{M!}$.

Remarque méthodologique : Le modèle IC représente le cas limite d'une société maximale en terme d'hétérogénéité et de polarisation, où aucune coalition idéologique majeure ne structure le vote. Il fournit une borne théorique supérieure très utile pour évaluer la vulnérabilité d'un mode de scrutin.

### 4.2. Architecture du moteur de simulation (Conception Orientée Objet)

Afin d'exécuter des simulations modulaires et évolutives, la modélisation en Python s'articule autour de cinq entités orientées objet (POO) :

[Candidate] ──> [Voter] ──> [PairwiseDuel] ──> [Tournament] ──> [CondorcetSimulation]

1. Candidate : Encapsule l'identité d'une alternative ($A, B, C, \dots$).

2. Voter : Représente un électeur détenant un ordre strict sur les candidats (liste ordonnée).

3. PairwiseDuel : Évalue le résultat d'un affrontement direct 1 contre 1 entre deux candidats sur l'ensemble de l'électorat.

4. Tournament :

* Exécute l'ensemble des $\frac{M(M-1)}{2}$ duels par paires.

* Construit la liste d'adjacence du graphe orienté (tournoi).

* Identifie s'il existe un Vainqueur de Condorcet (sommet ayant un degré sortant $M - 1$).

* Détecte les cycles d'intransitivité par un parcours en profondeur (DFS) avec marquage à 3 états (Blanc, Gris, Noir).

5.CondorcetSimulation : Moteur de Monte-Carlo orchestrant la génération tirage par tirage et le calcul des fréquences statistiques.

### 4.3. Détection algorithmique des cycles par Parcours en Profondeur (DFS)

Pour déterminer de façon rigoureuse la présence d'un paradoxe de Condorcet dans un tournoi de $M$ candidats, l'algorithme parcourt le graphe des victoires majoritaires :

1. Chaque sommet (candidat) possède un état :

* 0 (Blanc) : Sommet non encore exploré.

* 1 (Gris) : Sommet en cours d'exploration (présent dans la pile d'exécution).

* 2 (Noir) : Sommet entièrement traité.

2. Pour chaque candidat $K \in C$ :

* Si l'état de $K$ est Blanc, lancer DFS(K).

3. Durant DFS(X) :

* Marquer $X$ comme Gris (1).

* Pour chaque voisin $Y$ tel que $X \succ_P Y$ (arc orienté $X \to Y$) :

- Si l'état de $Y$ est Gris (1), un arc arrière est détecté : il existe une boucle fermée, donc un cycle de Condorcet. L'algorithme renvoie True.

- Si l'état de $Y$ est Blanc (0) et que DFS(Y) renvoie True, répercuter True.

* Marquer $X$ comme Noir (2).

### 4.4. Analyse des résultats statistiques et sensibilité aux paramètres

Lorsque l'on fait varier le nombre de candidats ($M$) et le nombre de votants ($N$), les simulations de Monte-Carlo mettent en évidence des propriétés fondamentales du choix collectif.

#### 1. Fréquence du paradoxe selon le nombre de candidats $M$ (pour un électorat $N = 21$)

Pour un nombre fixe de 21 votants (électorat impair pour éviter les égalités parfaites), l'exécution de $10\,000$ itérations de Monte-Carlo fournit les estimations suivantes :

| Nombre de candidats ($M$) | Nombre de duels $\frac{M(M-1)}{2}$ | Probabilité d'un Vainqueur de Condorcet | Probabilité du Paradoxe (Cycle) |
| --- | --- | --- | --- |
| 3  | 3   | $91{,}2 \text{ \%}$ | $8{,}8 \text{ \%}$ |
| 4  | 6   | $82{,}4 \text{ \%}$ | $17{,}6 \text{ \%}$ |
| 5  | 10  | $74{,}9 \text{ \%}$ | $25{,}1 \text{ \%}$ |
| 7  | 21  | $63{,}1 \text{ \%}$ | $36{,}9 \text{ \%}$ |
| 10 | 45  | $51{,}1 \text{ \%}$ | $48{,}9 \text{ \%}$ |
| 15 | 105 | $38{,}4 \text{ \%}$ | $61{,}6 \text{ \%}$ |

#### 2. Comportement asymptotique (Loi des grands nombres)

Les résultats révèlent deux tendances majeures :

* Croissance drastique avec le nombre d'options ($M$) : Dès que l'on passe de 3 à 5 candidats, la probabilité d'intransitivité collective est multipliée par presque trois, atteignant $25 \text{ \%}$. Pour un appel d'offres ou une élection à 10 candidats, le paradoxe survient près d'une fois sur deux.

* Convergence en fonction du nombre de votants ($N$) : Pour un nombre fixé de candidats $M = 3$, lorsque $N \to \infty$, la probabilité théorique du paradoxe sous le modèle IC converge vers la valeur limite exacte calculée par Niemi et Weisberg :

$$\lim_{N \to \infty} \mathbb{P}(\text{Paradoxe} \mid M=3) = 1 - \frac{3}{\pi} \arccos\left(\frac{1}{3}\right) \approx 8{,}77 \text{ \%}$$

### 4.5. Implémentation explicative en Python

Voici la structure synthétique des classes de simulation utilisées pour produire ces mesures :

```python
import random
from collections import defaultdict
from typing import List, Dict, Optional, Tuple

class Candidate:
    def __init__(self, name: str):
        self.name = name

class Voter:
    def __init__(self, voter_id: int, preferences: List[Candidate]):
        self.voter_id = voter_id
        self.preferences = preferences

    def prefers(self, a: Candidate, b: Candidate) -> bool:
        return self.preferences.index(a) < self.preferences.index(b)

class Tournament:
    def __init__(self, candidates: List[Candidate], voters: List[Voter]):
        self.candidates = candidates
        self.voters = voters
        self.adjacency_list: Dict[Candidate, List[Candidate]] = defaultdict(list)
        self._evaluate_duels()

    def _evaluate_duels(self):
        n = len(self.candidates)
        for i in range(n):
            for j in range(i + 1, n):
                c1, c2 = self.candidates[i], self.candidates[j]
                v1_wins = sum(1 for v in self.voters if v.prefers(c1, c2))
                v2_wins = len(self.voters) - v1_wins
                
                if v1_wins > v2_wins:
                    self.adjacency_list[c1].append(c2)
                elif v2_wins > v1_wins:
                    self.adjacency_list[c2].append(c1)

    def get_condorcet_winner(self) -> Optional[Candidate]:
        required = len(self.candidates) - 1
        for c in self.candidates:
            if len(self.adjacency_list[c]) == required:
                return c
        return None

    def has_cycle(self) -> bool:
        visited = {c: 0 for c in self.candidates}  # 0: Blanc, 1: Gris, 2: Noir

        def dfs(node: Candidate) -> bool:
            visited[node] = 1
            for neighbor in self.adjacency_list[node]:
                if visited[neighbor] == 1:
                    return True
                if visited[neighbor] == 0 and dfs(neighbor):
                    return True
            visited[node] = 2
            return False

        return any(dfs(c) for c in self.candidates if visited[c] == 0)
```

Cette modélisation numérique apporte la preuve que l'intransitivité collective n'est pas une anomalie marginale, mais une conséquence statistique directe de la multiplicité des choix.

## 5. Comment contourner le paradoxe ? Les alternatives électorales

Puisque le théorème d'impossibilité d'Arrow démontre qu'aucun système d'agrégation basé sur des ordres de préférence stricts ne peut être parfait, la théorie du choix social et la science électorale ont développé divers modes de scrutin alternatifs. Chaque méthode accepte de faire un compromis théorique différent pour éviter l'instabilité des cycles majoritaires.

### 5.1. La méthode de Borda : l'évaluation par classement pondéré

Proposée en 1770 par le mathématicien et navigateur Jean-Charles de Borda, cette méthode attribue un nombre de points à chaque option en fonction de sa position dans le classement établi par chaque votant.

#### Principe de fonctionnement

Pour $M$ candidats :

* Le $1^{\text{er}}$ choix d'un électeur reçoit $M$ points (ou $M - 1$ selon les conventions).

* Le $2^{\text{e}}$ choix reçoit $M - 1$ points, et ainsi de suite jusqu'au dernier choix qui reçoit $1$ point (ou $0$ point).

* Le vainqueur est l'alternative qui cumule le plus grand nombre total de points sur l'ensemble de l'électorat.

##### Application au cas classique de cycle

Reprenons l'électorat à 3 candidats $\{A, B, C\}$ et 3 votants produisant un cycle de Condorcet :

* Votant 1 : $A \succ B \succ C$ $\rightarrow A: 3\text{ pts}, B: 2\text{ pts}, C: 1\text{ pt}$

* Votant 2 : $B \succ C \succ A$ $\rightarrow B: 3\text{ pts}, C: 2\text{ pts}, A: 1\text{ pt}$

* Votant 3 : $C \succ A \succ B$ $\rightarrow C: 3\text{ pts}, A: 2\text{ pts}, B: 1\text{ pt}$

Total des points de Borda :


$$\text{Score}(A) = 3 + 1 + 2 = 6 \text{ pts}$$

$$\text{Score}(B) = 2 + 3 + 1 = 6 \text{ pts}$$

$$\text{Score}(C) = 1 + 2 + 3 = 6 \text{ pts}$$

La méthode de Borda transforme le cycle en une égalité parfaite (ex æquo), ce qui reflète la symétrie exacte des préférences du groupe.

##### Limites de la méthode de Borda

1. Sensibilité aux candidatures non pertinentes (Vote stratégique) : L'introduction d'un candidat "figurant" peut modifier le gagnant entre deux candidats majeurs.

2. Non-respect du critère de Condorcet : La méthode de Borda peut parfois élire un candidat qui est battu en duel direct par un Vainqueur de Condorcet.

### 5.2. Le vote à alternative transférable (Instant-Runoff Voting / IRV)

Utilisé dans plusieurs pays (notamment pour les élections législatives en Australie et dans certaines villes américaines), le scrutin à élimination directe successive (Instant-Runoff Voting) procède par tours d'élimination automatisés.

#### Principe de fonctionnement

1.Chaque électeur classe les candidats par ordre de préférence.

2. On compte les premières préférences de tous les votants.

3. Si un candidat obtient la majorité absolue ($> 50 \text{ \%}$ des premières places), il est immédiatement élu.

4. Si aucun candidat n'a la majorité absolue, le candidat ayant recueilli le moins de premières voix est éliminé.

5. Les bulletins qui désignaient le candidat éliminé en $1^{\text{re}}$ position sont redistribués à leur $2^{\text{e}}$ choix respectif.

6. Le processus se répète jusqu'à ce qu'un candidat atteigne la majorité absolue.

#### Limites face au critère de Condorcet

L'IRV ne garantit pas l'élection d'un Vainqueur de Condorcet s'il existe. Un candidat de consensus (qui est le $2^{\text{e}}$ choix de presque tout le monde et battrait tous les autres en duel) peut être éliminé dès le premier tour faute d'avoir accumulé suffisamment de $1^{\text{res}}$ positions individuelles.

### 5.3. Le Jugement Majoritaire : Évaluer plutôt que classer

Conçu en 2007 par les chercheurs français du CNRS Michel Balinski et Rida Laraki, le Jugement Majoritaire modifie la nature même de l'expression du vote pour contourner l'impossibilité d'Arrow.

#### Rupture de paradigme : du classement à l'évaluation absolue

Au lieu d'imposer un classement relatif ($A \succ B \succ C$), chaque électeur attribue de façon indépendante une mention qualitative à chaque candidat parmi une grille d'évaluation uniforme (ex. Excellent, Très Bien, Bien, Passable, Insuffisant, À Rejeter).

Candidate A : [ Excellent ] [ Très Bien ] [ Bien ] [ Passable ] [ Insuffisant ] [ À Rejeter ]
Candidate B : [ Excellent ] [ Très Bien ] [ Bien ] [ Passable ] [ Insuffisant ] [ À Rejeter ]
Candidate C : [ Excellent ] [ Très Bien ] [ Bien ] [ Passable ] [ Insuffisant ] [ À Rejeter ]

#### La Règle de la Médiane Majoritaire

1. Pour chaque candidat, on dresse le profil de ses mentions reçues sur l'ensemble de la population.

2. On détermine la mention médiane de chaque candidat (la mention telle qu'au moins $50 \text{ \%}$ de l'électorat lui attribue cette mention ou une meilleure mention).

3. Le candidat obtenant la meilleure mention médiane l'emporte.

4. En cas d'égalité des mentions médianes entre deux candidats, un algorithme de départage compare le pourcentage d'électeurs attribuant une mention strictement supérieure (ou inférieure) à la médiane.

#### Pourquoi le Jugement Majoritaire échappe-t-il au Paradoxe de Condorcet ?

Le théorème d'impossibilité d'Arrow et le paradoxe de Condorcet s'appliquent exclusivement aux fonctions d'agrégation d'ordres de préférence. En passant d'un espace de rangs relatifs à un espace d'évaluations absolues, le Jugement Majoritaire évite la formation de cycles décisionnels. Deux candidats sont évalués par rapport à un étalon de mesure absolu et non plus uniquement l'un par rapport à l'autre.

### 5.4. Tableau comparatif des modes de scrutin

Le tableau ci-dessous résume les propriétés fondamentales des principaux modes de scrutin face aux risques d'intransitivité et de manipulation :

| Mode de scrutin | Type d'expression | Garantit le Vainqueur de Condorcet ? | Immunisé contre les cycles ? | Résistance au vote stratégique |
|---|---|---|---|---|
| Majorité simple par duels (Condorcet) | Classement par rangs | Oui (s'il existe) | Non (risque de cycle) | Moyenne |
| Scrutin uninominal à 1 tour | Choix unique ($1^{\text{er}}$ rang) | Non | Oui | Très faible (vote utile) |
| Scrutin uninominal à 2 tours | Choix unique puis duel | Non | Oui | Faible |
| Méthode de Borda | Classement par rangs | Non | Oui | Faible (sensible aux figurants) |
| Vote alternatif (IRV) | Classement par rangs | Non | Oui | Moyenne |
| Jugement Majoritaire | Mentions qualitatives | Non applicable | Oui | Élevée |

Chaque mode de scrutin reflète une philosophie politique ou managériale spécifique. Le choix d'un système de vote par un décideur ou un ingénieur social consiste donc à sélectionner les compromis théoriques les plus acceptables selon le contexte.

## 6. Conclusion et enseignements pour les décideurs

### 6.1. L'intransitivité n'est pas un défaut, mais une propriété structurelle

Au terme de cette exploration théorique, empirique et numérique, une conclusion s'impose : le paradoxe de Condorcet et le théorème d'impossibilité d'Arrow ne doivent pas être interprétés comme des faiblesses accidentelles des institutions démocratiques. Ils révèlent une propriété mathématique fondamentale de l'agrégation de choix multidimensionnels.

Dès qu'un groupe d'individus rationnels doit faire un choix collectif parmi au moins trois options sur la base de critères divergents, il est illusoire d'espérer trouver un système de vote à la fois universel, équitable et systématiquement rationnel. L'intransitivité n'est pas le signe d'une mauvaise foi des votants ou d'un dysfonctionnement d'un scrutin, mais la conséquence directe de l'hétérogénéité des préférences au sein d'une collectivité.

### 6.2. Enseignements pratiques pour les managers, politologues et Data Scientists

De ces résultats découlent plusieurs leçons concrètes pour quiconque conçoit des processus décisionnels ou analyse des données de vote :

1.Méfiez-vous du scrutin uninominal classique :
Le vote uninominal à un ou deux tours est particulièrement vulnérable. Comme nous l'avons démontré dans la section 3, il risque d'éliminer prématurément le candidat de consensus (le Vainqueur de Condorcet) au profit d'options polarisantes mais disposant d'un socle de première préférence plus solide.

2. Prenez garde au pouvoir de l'ordre du jour (Agenda Setting) :
Dans une organisation où l'on vote option par option ou amendement par amendement, celui qui contrôle l'ordre de passage des votes détient un pouvoir disproportionné. En présence d'un cycle de Condorcet, l'organisateur de la réunion peut orienter le résultat final vers son option préférée simplement en orchestrant la séquence des duels.

3. Adaptez le mode de scrutin aux enjeux :

* Pour une élection politique majeure visant le consensus, le Jugement Majoritaire ou le Vote préférentiel transférable (IRV) offrent une meilleure résilience et limitent l'impact du vote utile.

* Pour un arbitrage managérial restreint, la méthode de Borda ou des tableaux d'évaluation multi-critères pondérés permettent de départager sereinement des propositions en concurrence.

4. Mesurez la fréquence des risques via la simulation :
Pour les Data Scientists et ingénieurs système, les simulations de Monte-Carlo démontrent que le risque de cycle augmente de façon spectaculaire avec le nombre d'options. Dans les applications complexes impliquant des algorithmes de recommandation collective ou du multi-agent decision making, limiter le nombre d'alternatives en compétition directe est une mesure de prudence essentielle.

### 6.3. Perspectives : choix collectif à l'ère du Web3, des DAO et de l'IA

Les enjeux soulevés par Nicolas de Condorcet en 1785 prennent une dimension entièrement nouvelle au XXIᵉ siècle avec la montée en puissance de nouvelles formes de gouvernance :

* Les Organisations Autonomes Décentralisées (DAO) :
Sur la blockchain, des protocoles gèrent des milliards de dollars de trésorerie via des votes gouvernés par des tokens. La présence de cycles de préférence ou d'attaques par manipulation d'agenda constitue une menace directe pour la stabilité financière de ces écosystèmes. Les concepteurs de contrats intelligents s'inspirent désormais de la théorie du choix social pour coder des règles de vote plus robustes.

* L'Intelligence Artificielle et l'agrégation de préférences humaines (RLHF) :
L'entraînement des grands modèles de langage (Large Language Models) repose largement sur le Reinforcement Learning from Human Feedback (RLHF). Pour aligner une IA sur les valeurs humaines, on agrège les préférences d'annotateurs humains comparant des réponses deux à deux. La présence d'intransitivités collectives dans ces jeux de données annotés pose d'immenses défis pour la convergence et l'équité des modèles génératifs.

En définitive, comprendre le paradoxe de Condorcet, c'est accepter la complexité inhérente au choix collectif. En renonçant au mythe du « système parfait », décideurs et ingénieurs peuvent concevoir des règles de gouvernance plus transparentes, plus stables et mieux adaptées à la diversité des préférences humaines.
