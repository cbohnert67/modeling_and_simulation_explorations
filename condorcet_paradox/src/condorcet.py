import random
from collections import defaultdict
from typing import List, Dict, Optional, Tuple


class Candidate:
    """Représente un candidat ou une option lors d'un scrutin."""

    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"Candidate('{self.name}')"

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Candidate):
            return self.name == other.name
        return False

    def __hash__(self) -> int:
        return hash(self.name)


class Voter:
    """Représente un électeur détenant une relation de préférence stricte et transitive."""

    def __init__(self, voter_id: int, preferences: List[Candidate]):
        self.voter_id = voter_id
        self.preferences = preferences

    def prefers(self, candidate_a: Candidate, candidate_b: Candidate) -> bool:
        """Retourne True si l'électeur préfère candidate_a à candidate_b."""
        idx_a = self.preferences.index(candidate_a)
        idx_b = self.preferences.index(candidate_b)
        return idx_a < idx_b

    def __repr__(self) -> str:
        prefs_str = " > ".join(c.name for c in self.preferences)
        return f"Voter({self.voter_id}: [{prefs_str}])"


class PairwiseDuel:
    """Représente un duel direct (1 contre 1) entre deux candidats."""

    def __init__(self, candidate_a: Candidate, candidate_b: Candidate):
        self.candidate_a = candidate_a
        self.candidate_b = candidate_b
        self.votes_a = 0
        self.votes_b = 0

    def evaluate_voters(self, voters: List[Voter]) -> None:
        """Décompte les voix pour chaque candidat du duel sur l'ensemble de l'électorat."""
        self.votes_a = 0
        self.votes_b = 0
        for voter in voters:
            if voter.prefers(self.candidate_a, self.candidate_b):
                self.votes_a += 1
            else:
                self.votes_b += 1

    def get_winner(self) -> Optional[Candidate]:
        """Retourne le vainqueur du duel direct ou None en cas d'égalité parfaite."""
        if self.votes_a > self.votes_b:
            return self.candidate_a
        elif self.votes_b > self.votes_a:
            return self.candidate_b
        return None


class Tournament:
    """Organise les duels par paires, construit le tournoi orienté et détecte les cycles."""

    def __init__(self, candidates: List[Candidate], voters: List[Voter]):
        self.candidates = candidates
        self.voters = voters
        self.duels: List[PairwiseDuel] = []
        self.adjacency_list: Dict[Candidate, List[Candidate]] = defaultdict(list)
        self._evaluate_tournament()

    def _evaluate_tournament(self) -> None:
        """Exécute tous les duels par paires et construit le graphe des victoires."""
        num_candidates = len(self.candidates)
        for i in range(num_candidates):
            for j in range(i + 1, num_candidates):
                duel = PairwiseDuel(self.candidates[i], self.candidates[j])
                duel.evaluate_voters(self.voters)
                self.duels.append(duel)

                winner = duel.get_winner()
                if winner == duel.candidate_a:
                    self.adjacency_list[duel.candidate_a].append(duel.candidate_b)
                elif winner == duel.candidate_b:
                    self.adjacency_list[duel.candidate_b].append(duel.candidate_a)

    def get_condorcet_winner(self) -> Optional[Candidate]:
        """Retourne le Vainqueur de Condorcet s'il existe (bat tous les autres candidats en duel)."""
        required_wins = len(self.candidates) - 1
        for candidate in self.candidates:
            if len(self.adjacency_list[candidate]) == required_wins:
                return candidate
        return None

    def has_cycle(self) -> bool:
        """Détecte la présence d'au moins un cycle d'intransitivité par un parcours DFS à 3 couleurs."""
        visited: Dict[Candidate, int] = {c: 0 for c in self.candidates}

        def dfs(node: Candidate) -> bool:
            visited[node] = 1  # Gris : en cours de visite
            for neighbor in self.adjacency_list[node]:
                if visited[neighbor] == 1:
                    return True  # Arc arrière trouvé -> Cycle !
                if visited[neighbor] == 0 and dfs(neighbor):
                    return True
            visited[node] = 2  # Noir : terminé
            return False

        for candidate in self.candidates:
            if visited[candidate] == 0:
                if dfs(candidate):
                    return True
        return False

    def get_borda_scores(self) -> Dict[Candidate, int]:
        """Calcule les points accumulés par chaque candidat selon la méthode de Borda."""
        scores: Dict[Candidate, int] = {c: 0 for c in self.candidates}
        num_candidates = len(self.candidates)
        for voter in self.voters:
            for rank, candidate in enumerate(voter.preferences):
                scores[candidate] += (num_candidates - 1 - rank)
        return scores

    def get_borda_winner(self) -> Candidate:
        """Retourne le candidat ayant obtenu le plus grand nombre de points de Borda."""
        scores = self.get_borda_scores()
        return max(scores, key=lambda c: scores[c])


class CondorcetSimulation:
    """Moteur de simulation Monte-Carlo pour l'estimation probabiliste du paradoxe de Condorcet."""

    def __init__(self, num_candidates: int, num_voters: int):
        self.num_candidates = num_candidates
        self.num_voters = num_voters
        self.candidates = [Candidate(chr(65 + i)) for i in range(num_candidates)]

    def generate_random_voters(self) -> List[Voter]:
        """Génère un profil de vote aléatoire uniforme (modèle Impartial Culture)."""
        voters = []
        for i in range(1, self.num_voters + 1):
            prefs = self.candidates.copy()
            random.shuffle(prefs)
            voters.append(Voter(i, prefs))
        return voters

    def run_simulation(self, iterations: int) -> Dict[str, float]:
        """Exécute N itérations Monte-Carlo et retourne les probabilités mesurées."""
        cycle_count = 0
        condorcet_winner_count = 0

        for _ in range(iterations):
            voters = self.generate_random_voters()
            tournament = Tournament(self.candidates, voters)

            if tournament.has_cycle():
                cycle_count += 1
            if tournament.get_condorcet_winner() is not None:
                condorcet_winner_count += 1

        return {
            "iterations": iterations,
            "num_candidates": self.num_candidates,
            "num_voters": self.num_voters,
            "cycle_probability": (cycle_count / iterations) * 100.0,
            "condorcet_winner_probability": (condorcet_winner_count / iterations) * 100.0
        }