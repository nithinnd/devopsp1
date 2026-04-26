import random
from datetime import datetime


LOGICAL_ANSWERS = [
    ("Yes", 0.34),
    ("No", 0.31),
    ("Maybe", 0.2),
    ("You already know the answer", 0.1),
    ("Stop overthinking", 0.05),
]

CHAOTIC_ANSWERS = [
    ("Yes", 0.18),
    ("No", 0.16),
    ("Maybe", 0.24),
    ("You already know the answer", 0.2),
    ("Stop overthinking", 0.22),
]

INSULTS = [
    "You have the confidence of a loading bar stuck at 3 percent.",
    "You are not a mess, but your decision-making is definitely freelancing.",
    "Your brain treats simple choices like a season finale cliffhanger.",
    "You overanalyze so hard even your to-do list needs emotional support.",
    "If hesitation were cardio, you'd be an elite athlete.",
]

MOTIVATIONS = [
    "Believe in yourself. Someone has to, and your browser is doing its best.",
    "You have survived every bad idea so far. Statistically, that's impressive.",
    "Go make progress. Perfection is just procrastination wearing nicer shoes.",
    "You can do hard things, even if you do complain stylishly first.",
    "One small step is still movement, and movement beats dramatic staring.",
]


def _current_hour():
    return datetime.now().hour


def _is_late_night(hour):
    return hour >= 22 or hour < 4


def _pick_weighted_answer():
    answers = CHAOTIC_ANSWERS if _is_late_night(_current_hour()) else LOGICAL_ANSWERS
    choices = [answer for answer, _ in answers]
    weights = [weight for _, weight in answers]
    return random.choices(choices, weights=weights, k=1)[0]


def _build_confidence(answer):
    confidence_ranges = {
        "Yes": (0.7, 0.96),
        "No": (0.68, 0.95),
        "Maybe": (0.35, 0.64),
        "You already know the answer": (0.75, 0.99),
        "Stop overthinking": (0.8, 1.0),
    }
    low, high = confidence_ranges[answer]
    return round(random.uniform(low, high), 2)


def get_decision(question):
    answer = _pick_weighted_answer()
    return {
        "question": question,
        "answer": answer,
        "confidence": _build_confidence(answer),
    }


def get_random_insult():
    return random.choice(INSULTS)


def get_motivation():
    return random.choice(MOTIVATIONS)
