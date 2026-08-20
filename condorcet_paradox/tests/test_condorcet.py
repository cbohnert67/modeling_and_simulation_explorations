import pytest
from src.condorcet import Candidate, Voter, PairwiseDuel, Tournament, CondorcetSimulation


def test_candidate_equality_and_hashing():
    c1 = Candidate("A")
    c2 = Candidate("A")
    c3 = Candidate("B")

    assert c1 == c2
    assert c1 != c3
    assert hash(c1) == hash(c2)
    assert str(c1) == "A"


def test_voter_preferences():
    a, b, c = Candidate("A"), Candidate("B"), Candidate("C")
    voter = Voter(1, [a, b, c])

    assert voter.prefers(a, b) is True
    assert voter.prefers(b, c) is True
    assert voter.prefers(a, c) is True
    assert voter.prefers(c, a) is False


def test_pairwise_duel_evaluation():
    a, b = Candidate("A"), Candidate("B")
    voters = [
        Voter(1, [a, b]),
        Voter(2, [a, b]),
        Voter(3, [b, a])
    ]

    duel = PairwiseDuel(a, b)
    duel.evaluate_voters(voters)

    assert duel.votes_a == 2
    assert duel.votes_b == 1
    assert duel.get_winner() == a


def test_tournament_classic_condorcet_cycle():
    a, b, c = Candidate("A"), Candidate("B"), Candidate("C")
    candidates = [a, b, c]

    # Profil du paradoxe : A > B > C > A
    voters = [
        Voter(1, [a, b, c]),
        Voter(2, [b, c, a]),
        Voter(3, [c, a, b])
    ]

    tournament = Tournament(candidates, voters)

    assert tournament.has_cycle() is True
    assert tournament.get_condorcet_winner() is None


def test_tournament_clear_condorcet_winner():
    a, b, c = Candidate("A"), Candidate("B"), Candidate("C")
    candidates = [a, b, c]

    voters = [
        Voter(1, [a, b, c]),
        Voter(2, [a, c, b]),
        Voter(3, [b, a, c])
    ]

    tournament = Tournament(candidates, voters)

    assert tournament.has_cycle() is False
    assert tournament.get_condorcet_winner() == a


def test_borda_scores_calculation():
    a, b, c = Candidate("A"), Candidate("B"), Candidate("C")
    candidates = [a, b, c]

    # V1: A(2), B(1), C(0)
    # V2: B(2), C(1), A(0)
    # V3: C(2), A(1), B(0)
    # Totaux : A=3, B=3, C=3
    voters = [
        Voter(1, [a, b, c]),
        Voter(2, [b, c, a]),
        Voter(3, [c, a, b])
    ]

    tournament = Tournament(candidates, voters)
    scores = tournament.get_borda_scores()

    assert scores[a] == 3
    assert scores[b] == 3
    assert scores[c] == 3


def test_condorcet_simulation_execution():
    sim = CondorcetSimulation(num_candidates=3, num_voters=21)
    results = sim.run_simulation(iterations=100)

    assert results["iterations"] == 100
    assert results["num_candidates"] == 3
    assert results["num_voters"] == 21
    assert 0.0 <= results["cycle_probability"] <= 100.0
    assert 0.0 <= results["condorcet_winner_probability"] <= 100.0