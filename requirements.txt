import os
import random
import hashlib
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

TIERS = [
    {"max": 20, "label": "Landlubber - scared of a rowboat"},
    {"max": 40, "label": "Deckhand - swabs when told"},
    {"max": 60, "label": "Buccaneer - knows the ropes"},
    {"max": 80, "label": "First Mate - would take a cannonball for the crew"},
    {"max": 95, "label": "True Pirate - loyalty runs deep as the sea"},
    {"max": 100, "label": "SAVAGE - the crew answers to you now"},
]

STORIES = [
    "You were stranded on a desert island with only a coconut and regret. "
    "Savage sailed by, saw you waving, and said 'not today, landlubber' - "
    "then turned the ship around anyway because leaving you looked bad on "
    "the crew's reputation.",

    "The kraken had you by the ankle. Savage didn't fight it. Savage just "
    "stared at the kraken until it let go out of pure secondhand embarrassment.",

    "You lost a bet and were tied to the mast during a storm. Savage untied "
    "you, but only after finishing a sandwich first, because priorities.",

    "Mutineers threw you overboard. Savage jumped in after you, realized "
    "the water was cold, and dragged you both back up complaining the whole time.",

    "You were locked in the brig for stealing the last biscuit. Savage "
    "picked the lock with a fork, ate the evidence, and blamed the parrot.",
]


def get_tier(pct: int) -> str:
    for tier in TIERS:
        if pct <= tier["max"]:
            return tier["label"]
    return TIERS[-1]["label"]


def hash_name(name: str, salt: str) -> int:
    """Turn a name (plus a salt) into a stable, well-spread integer."""
    digest = hashlib.sha256((salt + name.strip().lower()).encode("utf-8")).hexdigest()
    return int(digest, 16)


def spin_for_name(name: str):
    """
    Same name always produces the same percentage and tier - it's a hash,
    not true randomness. Separate salts keep the percentage and story
    choices independent of each other.
    """
    pct = (hash_name(name, "pct:") % 100) + 1
    story = None
    if pct > 95:
        story = STORIES[hash_name(name, "story:") % len(STORIES)]
    return pct, story


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/spin")
def spin():
    name = request.args.get("name", "").strip()

    if name:
        pct, story = spin_for_name(name)
    else:
        pct = random.randint(1, 100)
        story = random.choice(STORIES) if pct > 95 else None

    result = {"percent": pct, "tier": get_tier(pct)}
    if story:
        result["story"] = story
    return jsonify(result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
