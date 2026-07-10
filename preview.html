import os
import random
import hashlib
from flask import Flask, jsonify, request, send_file

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKGROUND_PATH = os.path.join(BASE_DIR, "background.png")

TIERS = [
    {"max": 20, "label": "Landlubber", "sub": "Scared of a rowboat"},
    {"max": 40, "label": "Deckhand", "sub": "Swabs when told"},
    {"max": 60, "label": "Buccaneer", "sub": "Knows the ropes"},
    {"max": 80, "label": "First Mate", "sub": "Would take a cannonball for the crew"},
    {"max": 95, "label": "True Pirate", "sub": "Loyalty runs deep as the sea"},
    {"max": 100, "label": "Savage", "sub": "The crew answers to you now"},
]

STORIES = [
    "You were stranded on a desert island with only a coconut and regret. "
    "Savage sailed by, saw you waving, and said 'not today, landlubber' - "
    "then turned the ship around anyway, because leaving you looked bad on "
    "the crew's reputation.",

    "The kraken had you by the ankle. Savage didn't fight it. Savage just "
    "stared at the kraken until it let go out of pure secondhand embarrassment.",

    "You lost a bet and were tied to the mast during a storm. Savage untied "
    "you - but only after finishing a sandwich first, because priorities.",

    "Mutineers threw you overboard. Savage jumped in after you, realized "
    "the water was cold, and dragged you both back up complaining the whole time.",

    "You were locked in the brig for stealing the last biscuit. Savage "
    "picked the lock with a fork, ate the evidence, and blamed the parrot.",
]

TRIBUTE_MIN = 2
TRIBUTE_MAX = 100


def get_tier(pct):
    for tier in TIERS:
        if pct <= tier["max"]:
            return tier
    return TIERS[-1]


def hash_name(name, salt):
    digest = hashlib.sha256((salt + name.strip().lower()).encode("utf-8")).hexdigest()
    return int(digest, 16)


def tribute_boost(tribute):
    """
    $2 buys a +10 boost. Each dollar above that buys a little more,
    scaling linearly so that $100 lands a +95 boost - which, added to
    even the unluckiest base roll of 1, guarantees at least 96% (Savage).
    """
    tribute = max(TRIBUTE_MIN, min(TRIBUTE_MAX, tribute))
    return round(10 + (tribute - TRIBUTE_MIN) * (85 / (TRIBUTE_MAX - TRIBUTE_MIN)))


def spin_for_name(name, tribute=0):
    base = (hash_name(name, "pct:") % 100) + 1
    boost = tribute_boost(tribute) if tribute >= TRIBUTE_MIN else 0
    pct = min(100, base + boost)
    story = None
    if pct > 95:
        story = STORIES[hash_name(name, "story:") % len(STORIES)]
    return pct, base, boost, story


PAGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Loyalty Test</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {
  --bg: #0c0e11;
  --line: rgba(255,255,255,0.09);
  --line-soft: rgba(255,255,255,0.05);
  --brass: #b99a5b;
  --brass-dim: rgba(185,154,91,0.5);
  --brass-faint: rgba(185,154,91,0.18);
  --text: #e7e4dd;
  --text-dim: #8a8578;
  --crimson: #a84040;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html, body {
  width: 100%;
  min-height: 100%;
  cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='28' height='28' viewBox='0 0 28 28'><path d='M3 25 L5 23 C3.5 16 7 7 17 3 C22 1.2 26 2 26 2 C26 2 25 6 21.5 10.5 C16.5 17 10.5 21 6 22 L4 26 Z' fill='%23d6d3ca' stroke='%23555248' stroke-width='1'/><path d='M4 26 L7.5 22.5 L9 24 L5.5 27.5 Z' fill='%23b99a5b'/></svg>") 2 26, auto;
  background: var(--bg);
}

button, input {
  cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='28' height='28' viewBox='0 0 28 28'><path d='M3 25 L5 23 C3.5 16 7 7 17 3 C22 1.2 26 2 26 2 C26 2 25 6 21.5 10.5 C16.5 17 10.5 21 6 22 L4 26 Z' fill='%23b99a5b' stroke='%23555248' stroke-width='1'/><path d='M4 26 L7.5 22.5 L9 24 L5.5 27.5 Z' fill='%23d6d3ca'/></svg>") 2 26, pointer;
}

body {
  min-height: 100vh;
  min-height: 100svh;
  font-family: 'Inter', system-ui, sans-serif;
  color: var(--text);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(0.75rem, 2.5vh, 2rem) clamp(0.75rem, 2.5vw, 2rem);
  position: relative;
  overflow-x: hidden;
  background:
    linear-gradient(rgba(3, 8, 18, 0.16), rgba(5, 10, 20, 0.42)),
    url('/background.png') center center / cover no-repeat fixed;
}

/* ---- Pirate scenery ---- */

.scenery { display: none; }

.ship {
  position: absolute;
  bottom: 24px;
  right: 4%;
  width: 220px;
  opacity: 0.5;
  animation: bob 7s ease-in-out infinite;
}

@keyframes bob {
  0%, 100% { transform: translateY(0) rotate(-0.6deg); }
  50% { transform: translateY(-8px) rotate(0.8deg); }
}

.cannon-l, .cannon-r {
  position: absolute;
  bottom: 26px;
  width: 120px;
  opacity: 0.35;
}

.cannon-l { left: 3%; }

.sea-line {
  position: absolute;
  bottom: 70px;
  left: 0;
  width: 200%;
  height: 30px;
  background: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 30' preserveAspectRatio='none'><path d='M0 15 Q75 5 150 15 T300 15 T450 15 T600 15' fill='none' stroke='rgba(185,154,91,0.16)' stroke-width='1'/></svg>") repeat-x;
  background-size: 50% 100%;
  animation: drift 26s linear infinite;
}

.sea-line.two { bottom: 52px; opacity: 0.55; animation-duration: 34s; animation-direction: reverse; }

@keyframes drift { from { transform: translateX(0); } to { transform: translateX(-50%); } }

/* ---- Layout ---- */

.frame-shell {
  width: min(60vw, 1200px);
  min-width: min(60vw, calc(100vw - 2rem));
  max-width: calc(100vw - 2rem);
  position: relative;
  z-index: 1;
}

.frame {
  width: 100%;
  max-width: 100%;
  text-align: center;
  position: relative;
  z-index: 1;
  padding: clamp(1.6rem, 2.9vw, 2.75rem);
  border: 1px solid rgba(255,255,255,0.11);
  background: linear-gradient(180deg, rgba(8,14,30,0.48), rgba(16,11,29,0.58));
  box-shadow: 0 18px 60px rgba(0,0,0,0.34), inset 0 0 40px rgba(95, 73, 160, 0.08);
  -webkit-backdrop-filter: blur(10px) saturate(1.12);
  backdrop-filter: blur(10px) saturate(1.12);
  transform-origin: top center;
}

.jolly { width: 74px; margin: 0 auto 1.2rem; display: block; opacity: 0.9; }

.eyebrow {
  font-size: 11px; font-weight: 500;
  letter-spacing: 0.35em; text-transform: uppercase;
  color: var(--brass); margin-bottom: 1rem;
}

h1 {
  font-family: 'Cormorant Garamond', serif;
  font-weight: 500; font-size: 44px; line-height: 1.08;
  margin-bottom: 0.8rem;
}

.lede { font-size: 14px; line-height: 1.6; color: var(--text-dim); margin-bottom: 2rem; }
.lede em { font-style: normal; color: var(--text); }

.rope {
  width: 190px; height: 12px; margin: 0 auto 2.2rem; display: block; opacity: 0.6;
}

.name-input {
  width: 100%; font-family: inherit; font-size: 15px; text-align: center;
  color: var(--text); background: transparent; border: none;
  border-bottom: 1px solid var(--line);
  padding: 10px 4px 12px; margin-bottom: 2.2rem;
  outline: none; transition: border-color 0.25s;
}
.name-input::placeholder { color: var(--text-dim); opacity: 0.7; }
.name-input:focus { border-color: var(--brass); }

/* ---- Tribute ---- */

.tribute {
  border: 1px solid var(--line);
  padding: 1.3rem 1.4rem 1.5rem;
  margin-bottom: 2.4rem;
  position: relative;
}

.tribute-corner {
  position: absolute; width: 14px; height: 14px;
  border-color: var(--brass-dim); border-style: solid;
}
.tribute-corner.tl { top: -1px; left: -1px; border-width: 1px 0 0 1px; }
.tribute-corner.tr { top: -1px; right: -1px; border-width: 1px 1px 0 0; }
.tribute-corner.bl { bottom: -1px; left: -1px; border-width: 0 0 1px 1px; }
.tribute-corner.br { bottom: -1px; right: -1px; border-width: 0 1px 1px 0; }

.tribute-head {
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 0.4rem;
}

.tribute-label {
  font-size: 10px; font-weight: 500;
  letter-spacing: 0.3em; text-transform: uppercase;
  color: var(--brass);
}

.tribute-amount {
  font-family: 'Cormorant Garamond', serif;
  font-size: 26px; color: var(--text);
  min-width: 64px; text-align: right;
}

.tribute-sub {
  font-size: 12px; color: var(--text-dim);
  text-align: left; margin-bottom: 1.1rem; min-height: 16px;
}

.tribute-row { display: flex; align-items: center; gap: 14px; }

.coin { width: 22px; height: 22px; flex: 0 0 auto; opacity: 0.9; }

.tribute-entry {
  flex: 1;
  display: flex;
  align-items: center;
  border: 1px solid var(--line);
  background: rgba(0,0,0,0.2);
  transition: border-color 0.25s, box-shadow 0.25s;
}
.tribute-entry:focus-within {
  border-color: var(--brass);
  box-shadow: 0 0 0 3px var(--brass-faint);
}
.tribute-currency {
  padding-left: 13px;
  color: var(--brass);
  font-family: 'Cormorant Garamond', serif;
  font-size: 22px;
}
.tribute-input {
  width: 100%;
  min-width: 0;
  border: 0;
  outline: 0;
  color: var(--text);
  background: transparent;
  font: 500 15px 'Inter', sans-serif;
  padding: 12px 13px 12px 7px;
}
.tribute-input::placeholder { color: var(--text-dim); opacity: 0.72; }
.tribute-input::-webkit-outer-spin-button,
.tribute-input::-webkit-inner-spin-button { -webkit-appearance: none; margin: 0; }
.tribute-input[type=number] { -moz-appearance: textfield; }

.tribute-off {
  margin-top: 0.9rem;
  font-size: 10px; letter-spacing: 0.2em; text-transform: uppercase;
  color: var(--text-dim); background: none; border: none;
  border-bottom: 1px solid transparent;
  padding: 2px 0; transition: color 0.2s;
}
.tribute-off:hover { color: var(--text); }
.tribute-off.active { color: var(--brass); }

/* ---- Dial ---- */

.dial-wrap { position: relative; width: 210px; height: 210px; margin: 0 auto 1.8rem; }
.dial-wrap svg.ring { transform: rotate(-90deg); display: block; }

.compass {
  position: absolute; inset: 14px;
  opacity: 0.13; pointer-events: none;
}

.dial-track { fill: none; stroke: var(--line-soft); stroke-width: 1.5; }
.dial-fill {
  fill: none; stroke: var(--brass); stroke-width: 1.5;
  transition: stroke-dashoffset 0.4s ease, stroke 0.4s ease;
}
.dial-fill.savage { stroke: var(--crimson); }

.dial-center {
  position: absolute; inset: 0;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
}

.pct {
  font-family: 'Cormorant Garamond', serif;
  font-weight: 400; font-size: 62px; line-height: 1;
}
.pct sup { font-size: 26px; color: var(--text-dim); }

.boost-note {
  font-size: 11px; color: var(--brass);
  min-height: 15px; margin-top: 2px; letter-spacing: 0.05em;
}

.tier-label {
  font-family: 'Cormorant Garamond', serif;
  font-size: 26px; font-weight: 500;
  min-height: 32px; margin-bottom: 0.3rem;
}

.tier-sub { font-size: 13px; color: var(--text-dim); min-height: 18px; margin-bottom: 2rem; }

.spin-btn {
  font-family: 'Inter', sans-serif;
  font-size: 12px; font-weight: 500;
  letter-spacing: 0.3em; text-transform: uppercase;
  color: var(--brass); background: transparent;
  border: 1px solid var(--brass-dim);
  padding: 15px 44px;
  transition: background 0.25s, color 0.25s, border-color 0.25s;
}
.spin-btn:hover { background: var(--brass); color: var(--bg); border-color: var(--brass); }
.spin-btn:active { transform: translateY(1px); }
.spin-btn:disabled { opacity: 0.4; pointer-events: none; }

.hint { font-size: 12px; color: var(--text-dim); opacity: 0.75; margin-top: 1rem; }

.story-box {
  margin-top: 2.4rem; padding: 1.6rem 1.5rem;
  border: 1px solid var(--line); border-top: 1px solid var(--brass-dim);
  text-align: left; animation: rise 0.5s ease;
}
@keyframes rise { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
.story-box.hidden { display: none; }

.story-label {
  font-size: 10px; font-weight: 500;
  letter-spacing: 0.3em; text-transform: uppercase;
  color: var(--brass); margin-bottom: 0.8rem;
}

.story-text { font-family: 'Cormorant Garamond', serif; font-size: 19px; line-height: 1.55; }

.sound-bar {
  margin-top: 3rem; display: flex; align-items: center;
  justify-content: center; gap: 16px; opacity: 0.85;
}

.sound-toggle {
  font-family: 'Inter', sans-serif;
  font-size: 10px; font-weight: 500;
  letter-spacing: 0.25em; text-transform: uppercase;
  color: var(--text-dim); background: transparent;
  border: 1px solid var(--line); padding: 9px 18px;
  transition: color 0.25s, border-color 0.25s;
}
.sound-toggle:hover { color: var(--text); }
.sound-toggle.on { color: var(--brass); border-color: var(--brass-dim); }

.volume {
  width: 130px; -webkit-appearance: none; appearance: none;
  height: 1px; background: var(--line); outline: none; transition: opacity 0.3s;
}
.volume:disabled { opacity: 0.25; }
.volume::-webkit-slider-thumb {
  -webkit-appearance: none; appearance: none;
  width: 11px; height: 11px; border-radius: 50%;
  background: var(--brass); border: none;
}
.volume::-moz-range-thumb { width: 11px; height: 11px; border-radius: 50%; background: var(--brass); border: none; }

.footer {
  margin-top: 2rem; font-size: 10px; letter-spacing: 0.25em;
  text-transform: uppercase; color: var(--text-dim); opacity: 0.5;
}

@media (max-width: 700px) {
  body {
    align-items: flex-start;
    background-attachment: scroll;
    padding: 0.75rem;
  }
  .frame-shell {
    width: min(430px, calc(100vw - 1.5rem));
    min-width: 0;
    max-width: calc(100vw - 1.5rem);
  }
  .frame { padding: 1.15rem; }
}

@media (max-width: 500px) {
  h1 { font-size: clamp(32px, 10vw, 38px); }
  .lede { font-size: 13px; }
  .dial-wrap { transform: scale(0.9); margin-top: -10px; margin-bottom: 0.7rem; }
  .pct { font-size: 52px; }
  .sound-bar { flex-wrap: wrap; gap: 12px; }
  .volume { width: min(130px, 40vw); }
}

@media (max-width: 360px) {
  .tribute-head { align-items: flex-start; gap: 8px; }
  .tribute-label { letter-spacing: 0.2em; }
  .spin-btn { width: 100%; padding-left: 12px; padding-right: 12px; }
}
</style>
</head>
<body>

<div class="scenery" aria-hidden="true">
  <div class="sea-line"></div>
  <div class="sea-line two"></div>

  <svg class="ship" viewBox="0 0 220 150" fill="none" stroke="#b99a5b" stroke-width="1.4">
    <path d="M25 112 L195 112 L178 138 L48 138 Z" />
    <line x1="110" y1="112" x2="110" y2="18" />
    <path d="M110 22 L110 62 L58 62 Q78 42 110 22 Z" fill="rgba(185,154,91,0.08)"/>
    <path d="M110 30 L110 92 L172 92 Q150 56 110 30 Z" fill="rgba(185,154,91,0.08)"/>
    <line x1="110" y1="18" x2="132" y2="18" />
    <path d="M132 18 L132 26 L122 22 Z" fill="#b99a5b" stroke="none"/>
    <line x1="48" y1="112" x2="110" y2="62" stroke-dasharray="2 4"/>
    <line x1="178" y1="112" x2="110" y2="92" stroke-dasharray="2 4"/>
    <circle cx="70" cy="123" r="3"/><circle cx="110" cy="123" r="3"/><circle cx="150" cy="123" r="3"/>
  </svg>

  <svg class="cannon-l" viewBox="0 0 120 70" fill="none" stroke="#b99a5b" stroke-width="1.4">
    <path d="M14 42 L74 22 Q86 18 90 26 Q94 34 82 38 L22 58 Q12 60 10 52 Q8 46 14 42 Z"/>
    <circle cx="40" cy="56" r="10"/>
    <circle cx="40" cy="56" r="3" fill="rgba(185,154,91,0.25)" stroke="none"/>
    <circle cx="100" cy="22" r="4"/>
    <path d="M104 14 Q110 8 108 2" stroke-dasharray="2 3"/>
  </svg>
</div>

<div id="frameShell" class="frame-shell">
<main id="appFrame" class="frame">
  <svg class="jolly" viewBox="0 0 80 80" fill="none" stroke="#b99a5b" stroke-width="1.6">
    <circle cx="40" cy="32" r="15"/>
    <circle cx="34" cy="30" r="2.6" fill="#b99a5b" stroke="none"/>
    <circle cx="46" cy="30" r="2.6" fill="#b99a5b" stroke="none"/>
    <path d="M37 40 L40 36 L43 40" />
    <path d="M33 44 Q40 48 47 44" />
    <line x1="35" y1="44" x2="35" y2="47"/><line x1="40" y1="46" x2="40" y2="49"/><line x1="45" y1="44" x2="45" y2="47"/>
    <path d="M14 56 L66 74 M66 56 L14 74" stroke-linecap="round"/>
    <circle cx="14" cy="56" r="3.5"/><circle cx="66" cy="56" r="3.5"/>
    <circle cx="14" cy="74" r="3.5"/><circle cx="66" cy="74" r="3.5"/>
  </svg>

  <div class="eyebrow">The loyalty test</div>
  <h1>How much of a<br>pirate are you?</h1>
  <p class="lede">Enter your name. The wheel does not deal in luck &mdash;<br>it deals in fate. Your loyalty to <em>Savage</em> awaits.</p>

  <svg class="rope" viewBox="0 0 190 12" fill="none" stroke="#b99a5b" stroke-width="1">
    <path d="M2 6 Q8 1 14 6 T26 6 T38 6 T50 6 T62 6 T74 6 T86 6 T98 6 T110 6 T122 6 T134 6 T146 6 T158 6 T170 6 T182 6 T188 6"/>
    <path d="M2 6 Q8 11 14 6 T26 6 T38 6 T50 6 T62 6 T74 6 T86 6 T98 6 T110 6 T122 6 T134 6 T146 6 T158 6 T170 6 T182 6 T188 6" opacity="0.5"/>
  </svg>

  <input id="nameInput" class="name-input" type="text" placeholder="Your name" maxlength="40" autocomplete="off">

  <div class="tribute">
    <span class="tribute-corner tl"></span><span class="tribute-corner tr"></span>
    <span class="tribute-corner bl"></span><span class="tribute-corner br"></span>

    <div class="tribute-head">
      <span class="tribute-label">Tribute to Savage</span>
      <span id="tributeAmount" class="tribute-amount">&mdash;</span>
    </div>
    <p id="tributeSub" class="tribute-sub">The wheel is not above bribery.</p>

    <div class="tribute-row">
      <svg class="coin" viewBox="0 0 22 22" fill="none" stroke="#b99a5b" stroke-width="1.3">
        <circle cx="11" cy="11" r="9.5"/>
        <circle cx="11" cy="11" r="6.5" opacity="0.5"/>
        <path d="M11 7.5 V14.5 M8.5 9 Q11 7 13.5 9 M8.5 13 Q11 15 13.5 13"/>
      </svg>
      <label class="tribute-entry" for="tributeInput">
        <span class="tribute-currency">$</span>
        <input id="tributeInput" class="tribute-input" type="number" min="2" max="100" step="1" placeholder="Enter 2 to 100" inputmode="numeric" autocomplete="off">
      </label>
    </div>

    <button id="tributeOff" class="tribute-off active" type="button">Clear tribute &mdash; face fate honestly</button>
  </div>

  <div class="dial-wrap">
    <svg class="compass" viewBox="0 0 180 180" fill="none" stroke="#b99a5b" stroke-width="1">
      <circle cx="90" cy="90" r="70"/>
      <path d="M90 20 L96 84 L90 90 L84 84 Z" fill="rgba(185,154,91,0.4)" stroke="none"/>
      <path d="M90 160 L84 96 L90 90 L96 96 Z"/>
      <path d="M20 90 L84 84 L90 90 L84 96 Z"/>
      <path d="M160 90 L96 96 L90 90 L96 84 Z"/>
      <line x1="90" y1="10" x2="90" y2="22"/><line x1="90" y1="158" x2="90" y2="170"/>
      <line x1="10" y1="90" x2="22" y2="90"/><line x1="158" y1="90" x2="170" y2="90"/>
    </svg>
    <svg class="ring" width="210" height="210" viewBox="0 0 210 210">
      <circle class="dial-track" cx="105" cy="105" r="96"></circle>
      <circle id="dialFill" class="dial-fill" cx="105" cy="105" r="96"
              stroke-dasharray="603.2" stroke-dashoffset="603.2"></circle>
    </svg>
    <div class="dial-center">
      <div class="pct"><span id="pctNum">0</span><sup>%</sup></div>
      <div id="boostNote" class="boost-note"></div>
    </div>
  </div>

  <div id="tierLabel" class="tier-label">&nbsp;</div>
  <div id="tierSub" class="tier-sub">Consult the wheel</div>

  <button id="spinBtn" class="spin-btn">Consult the wheel</button>
  <p class="hint">The same name always meets the same fate. Gold, however, talks.</p>

  <div id="story" class="story-box hidden">
    <p class="story-label">How Savage saved you</p>
    <p id="storyText" class="story-text"></p>
  </div>

  <div class="sound-bar">
    <button id="soundToggle" class="sound-toggle">Sound off</button>
    <input id="volume" class="volume" type="range" min="0" max="100" step="1" value="40" disabled aria-label="Ambience volume">
  </div>

  <div class="footer">For the crew</div>
</main>
</div>

<script>
const spinBtn = document.getElementById('spinBtn');
const pctNum = document.getElementById('pctNum');
const boostNote = document.getElementById('boostNote');
const tierLabel = document.getElementById('tierLabel');
const tierSub = document.getElementById('tierSub');
const storyBox = document.getElementById('story');
const storyText = document.getElementById('storyText');
const nameInput = document.getElementById('nameInput');
const dialFill = document.getElementById('dialFill');
const soundToggle = document.getElementById('soundToggle');
const volumeSlider = document.getElementById('volume');
const tributeInput = document.getElementById('tributeInput');
const tributeAmount = document.getElementById('tributeAmount');
const tributeSub = document.getElementById('tributeSub');
const tributeOff = document.getElementById('tributeOff');
const frameShell = document.getElementById('frameShell');
const appFrame = document.getElementById('appFrame');

const CIRC = 603.2;

function setDial(pct, savage) {
  dialFill.style.strokeDashoffset = CIRC - (CIRC * pct) / 100;
  dialFill.classList.toggle('savage', !!savage);
}

function boostFor(t) { return Math.round(10 + (t - 2) * (85 / 98)); }

function getTribute() {
  const raw = tributeInput.value.trim();
  if (!raw) return 0;
  const amount = Number(raw);
  if (!Number.isFinite(amount)) return 0;
  return Math.round(Math.max(2, Math.min(100, amount)));
}

function updateTributeUI() {
  const t = getTribute();
  if (!t) {
    tributeAmount.innerHTML = '&mdash;';
    tributeSub.textContent = 'Type a tribute from $2 to $100, or leave it blank.';
    tributeOff.classList.add('active');
    return;
  }
  tributeAmount.textContent = '$' + t;
  if (t >= 100) {
    tributeSub.textContent = 'Boost +95 - Savage rank all but guaranteed.';
  } else {
    tributeSub.textContent = 'Boost +' + boostFor(t) + ' to your fate.';
  }
  tributeOff.classList.remove('active');
}

tributeInput.addEventListener('input', updateTributeUI);
tributeInput.addEventListener('blur', () => {
  const t = getTribute();
  tributeInput.value = t ? t : '';
  updateTributeUI();
});
tributeOff.addEventListener('click', () => {
  tributeInput.value = '';
  updateTributeUI();
  tributeInput.focus();
});

spinBtn.addEventListener('click', async () => {
  spinBtn.disabled = true;
  storyBox.classList.add('hidden');
  boostNote.textContent = '';
  tierLabel.innerHTML = '&nbsp;';
  tierSub.textContent = 'The wheel is turning\u2026';

  let ticks = 0;
  const maxTicks = 16;
  const tickInterval = setInterval(() => {
    ticks++;
    const fake = Math.floor(Math.random() * 100) + 1;
    pctNum.textContent = fake;
    setDial(fake, false);
  }, 80);

  const name = nameInput.value.trim();
  const params = new URLSearchParams();
  if (name) params.set('name', name);
  const tribute = getTribute();
  if (tribute) params.set('tribute', tribute);
  const qs = params.toString();
  const url = qs ? '/api/spin?' + qs : '/api/spin';

  let data;
  try {
    const res = await fetch(url);
    data = await res.json();
  } catch (err) {
    clearInterval(tickInterval);
    tierSub.textContent = 'The sea swallowed the answer. Try again.';
    spinBtn.disabled = false;
    return;
  }

  setTimeout(() => {
    clearInterval(tickInterval);
    pctNum.textContent = data.percent;
    setDial(data.percent, data.percent > 95);
    tierLabel.textContent = data.tier;
    tierSub.textContent = data.sub;

    if (data.boost > 0) {
      boostNote.textContent = data.base + ' + ' + data.boost + ' tribute';
    }

    if (data.story) {
      storyText.textContent = data.story;
      storyBox.classList.remove('hidden');
    }

    spinBtn.disabled = false;
    requestAnimationFrame(fitAppToViewport);
  }, maxTicks * 80);
});

/* ---- Keep the full app fitted on shorter desktop screens ---- */

function fitAppToViewport() {
  appFrame.style.transform = 'none';
  frameShell.style.width = '';
  frameShell.style.height = '';

  // Phones and narrow tablets use natural responsive scrolling.
  if (window.innerWidth < 700) return;

  const naturalWidth = appFrame.offsetWidth;
  const naturalHeight = appFrame.offsetHeight;
  const availableWidth = Math.max(320, window.innerWidth - 24);
  const availableHeight = Math.max(480, window.innerHeight - 24);
  const scale = Math.min(1, availableWidth / naturalWidth, availableHeight / naturalHeight);

  if (scale < 0.995) {
    appFrame.style.transform = `scale(${scale})`;
    frameShell.style.width = `${naturalWidth * scale}px`;
    frameShell.style.height = `${naturalHeight * scale}px`;
  }
}

window.addEventListener('resize', fitAppToViewport);
window.addEventListener('orientationchange', fitAppToViewport);
requestAnimationFrame(fitAppToViewport);
if (document.fonts && document.fonts.ready) {
  document.fonts.ready.then(fitAppToViewport);
}
updateTributeUI();

/* ---- Ambience: quiet ocean air, OFF by default ---- */

let ctx = null, master = null, running = false;

function buildAmbience() {
  ctx = new (window.AudioContext || window.webkitAudioContext)();
  master = ctx.createGain();
  master.gain.value = volumeSlider.value / 100 * 0.5;
  master.connect(ctx.destination);

  const len = ctx.sampleRate * 4;
  const buf = ctx.createBuffer(1, len, ctx.sampleRate);
  const d = buf.getChannelData(0);
  let last = 0;
  for (let i = 0; i < len; i++) {
    const white = Math.random() * 2 - 1;
    last = (last + 0.02 * white) / 1.02;
    d[i] = last * 3.5;
  }

  const noise = ctx.createBufferSource();
  noise.buffer = buf;
  noise.loop = true;

  const lp = ctx.createBiquadFilter();
  lp.type = 'lowpass'; lp.frequency.value = 420; lp.Q.value = 0.4;

  const swell = ctx.createGain(); swell.gain.value = 0.25;

  const lfo = ctx.createOscillator(); lfo.frequency.value = 0.07;
  const lfoGain = ctx.createGain(); lfoGain.gain.value = 0.15;
  lfo.connect(lfoGain); lfoGain.connect(swell.gain);

  noise.connect(lp); lp.connect(swell); swell.connect(master);

  const drone = ctx.createOscillator();
  drone.type = 'sine'; drone.frequency.value = 55;
  const droneGain = ctx.createGain(); droneGain.gain.value = 0.05;
  drone.connect(droneGain); droneGain.connect(master);

  noise.start(); lfo.start(); drone.start();
}

soundToggle.addEventListener('click', () => {
  if (!ctx) buildAmbience();
  if (ctx.state === 'suspended') ctx.resume();
  running = !running;
  if (running) {
    master.gain.setTargetAtTime(volumeSlider.value / 100 * 0.5, ctx.currentTime, 0.4);
    soundToggle.textContent = 'Sound on';
    soundToggle.classList.add('on');
    volumeSlider.disabled = false;
  } else {
    master.gain.setTargetAtTime(0, ctx.currentTime, 0.3);
    soundToggle.textContent = 'Sound off';
    soundToggle.classList.remove('on');
    volumeSlider.disabled = true;
  }
});

volumeSlider.addEventListener('input', () => {
  if (ctx && running) {
    master.gain.setTargetAtTime(volumeSlider.value / 100 * 0.5, ctx.currentTime, 0.05);
  }
});
</script>
</body>
</html>"""


@app.route("/")
def index():
    return PAGE


@app.route("/background.png")
def background():
    return send_file(BACKGROUND_PATH, mimetype="image/png", max_age=86400)


@app.route("/api/spin")
def spin():
    name = request.args.get("name", "").strip()
    tribute = request.args.get("tribute", type=int) or 0

    if name:
        pct, base, boost, story = spin_for_name(name, tribute)
    else:
        base = random.randint(1, 100)
        boost = tribute_boost(tribute) if tribute >= TRIBUTE_MIN else 0
        pct = min(100, base + boost)
        story = random.choice(STORIES) if pct > 95 else None

    tier = get_tier(pct)
    result = {
        "percent": pct,
        "base": base,
        "boost": boost,
        "tier": tier["label"],
        "sub": tier["sub"],
    }
    if story:
        result["story"] = story
    return jsonify(result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
