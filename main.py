import os
import random
import hashlib
from flask import Flask, jsonify, request

app = Flask(__name__)

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


def get_tier(pct):
    for tier in TIERS:
        if pct <= tier["max"]:
            return tier
    return TIERS[-1]


def hash_name(name, salt):
    digest = hashlib.sha256((salt + name.strip().lower()).encode("utf-8")).hexdigest()
    return int(digest, 16)


def spin_for_name(name):
    pct = (hash_name(name, "pct:") % 100) + 1
    story = None
    if pct > 95:
        story = STORIES[hash_name(name, "story:") % len(STORIES)]
    return pct, story


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
  --bg-soft: #12151a;
  --line: rgba(255,255,255,0.09);
  --line-soft: rgba(255,255,255,0.05);
  --brass: #b99a5b;
  --brass-dim: rgba(185,154,91,0.5);
  --text: #e7e4dd;
  --text-dim: #8a8578;
  --crimson: #a84040;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html, body {
  cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='28' height='28' viewBox='0 0 28 28'><path d='M3 25 L5 23 C3.5 16 7 7 17 3 C22 1.2 26 2 26 2 C26 2 25 6 21.5 10.5 C16.5 17 10.5 21 6 22 L4 26 Z' fill='%23d6d3ca' stroke='%23555248' stroke-width='1'/><path d='M4 26 L7.5 22.5 L9 24 L5.5 27.5 Z' fill='%23b99a5b'/></svg>") 2 26, auto;
  background: var(--bg);
}

button, input {
  cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='28' height='28' viewBox='0 0 28 28'><path d='M3 25 L5 23 C3.5 16 7 7 17 3 C22 1.2 26 2 26 2 C26 2 25 6 21.5 10.5 C16.5 17 10.5 21 6 22 L4 26 Z' fill='%23b99a5b' stroke='%23555248' stroke-width='1'/><path d='M4 26 L7.5 22.5 L9 24 L5.5 27.5 Z' fill='%23d6d3ca'/></svg>") 2 26, pointer;
}

body {
  min-height: 100vh;
  font-family: 'Inter', system-ui, sans-serif;
  color: var(--text);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem 1.25rem;
  background:
    radial-gradient(1000px 500px at 50% -20%, rgba(185,154,91,0.05), transparent 65%),
    var(--bg);
}

.frame {
  width: 100%;
  max-width: 420px;
  text-align: center;
}

.eyebrow {
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.35em;
  text-transform: uppercase;
  color: var(--brass);
  margin-bottom: 1.1rem;
}

h1 {
  font-family: 'Cormorant Garamond', serif;
  font-weight: 500;
  font-size: 44px;
  line-height: 1.08;
  letter-spacing: 0.01em;
  margin-bottom: 0.8rem;
}

.lede {
  font-size: 14px;
  line-height: 1.6;
  color: var(--text-dim);
  margin-bottom: 2.5rem;
}

.lede em {
  font-style: normal;
  color: var(--text);
}

.rule {
  width: 42px;
  height: 1px;
  background: var(--brass-dim);
  margin: 0 auto 2.5rem;
}

.name-input {
  width: 100%;
  font-family: inherit;
  font-size: 15px;
  text-align: center;
  color: var(--text);
  background: transparent;
  border: none;
  border-bottom: 1px solid var(--line);
  padding: 10px 4px 12px;
  margin-bottom: 2.75rem;
  outline: none;
  transition: border-color 0.25s;
}

.name-input::placeholder { color: var(--text-dim); opacity: 0.7; }
.name-input:focus { border-color: var(--brass); }

.dial-wrap { position: relative; width: 210px; height: 210px; margin: 0 auto 2rem; }
.dial-wrap svg { transform: rotate(-90deg); display: block; }

.dial-track { fill: none; stroke: var(--line-soft); stroke-width: 1.5; }
.dial-fill {
  fill: none;
  stroke: var(--brass);
  stroke-width: 1.5;
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
  font-weight: 400;
  font-size: 64px;
  line-height: 1;
  font-variant-numeric: lining-nums;
}

.pct sup { font-size: 26px; color: var(--text-dim); }

.tier-label {
  font-family: 'Cormorant Garamond', serif;
  font-size: 26px;
  font-weight: 500;
  min-height: 32px;
  margin-bottom: 0.3rem;
}

.tier-sub {
  font-size: 13px;
  color: var(--text-dim);
  min-height: 18px;
  margin-bottom: 2.25rem;
}

.spin-btn {
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--brass);
  background: transparent;
  border: 1px solid var(--brass-dim);
  padding: 15px 44px;
  transition: background 0.25s, color 0.25s, border-color 0.25s;
}

.spin-btn:hover { background: var(--brass); color: var(--bg); border-color: var(--brass); }
.spin-btn:active { transform: translateY(1px); }
.spin-btn:disabled { opacity: 0.4; pointer-events: none; }

.hint {
  font-size: 12px;
  color: var(--text-dim);
  opacity: 0.75;
  margin-top: 1.1rem;
}

.story-box {
  margin-top: 2.5rem;
  padding: 1.6rem 1.5rem;
  border: 1px solid var(--line);
  border-top: 1px solid var(--brass-dim);
  text-align: left;
  animation: rise 0.5s ease;
}

@keyframes rise {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.story-box.hidden { display: none; }

.story-label {
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--brass);
  margin-bottom: 0.8rem;
}

.story-text {
  font-family: 'Cormorant Garamond', serif;
  font-size: 19px;
  line-height: 1.55;
  color: var(--text);
}

.sound-bar {
  margin-top: 3.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  opacity: 0.85;
}

.sound-toggle {
  font-family: 'Inter', sans-serif;
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--text-dim);
  background: transparent;
  border: 1px solid var(--line);
  padding: 9px 18px;
  transition: color 0.25s, border-color 0.25s;
}

.sound-toggle:hover { color: var(--text); border-color: var(--line); }
.sound-toggle.on { color: var(--brass); border-color: var(--brass-dim); }

.volume {
  width: 130px;
  -webkit-appearance: none;
  appearance: none;
  height: 1px;
  background: var(--line);
  outline: none;
  transition: opacity 0.3s;
}

.volume:disabled { opacity: 0.25; }

.volume::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 11px; height: 11px;
  border-radius: 50%;
  background: var(--brass);
  border: none;
}

.volume::-moz-range-thumb {
  width: 11px; height: 11px;
  border-radius: 50%;
  background: var(--brass);
  border: none;
}

.footer {
  margin-top: 2.25rem;
  font-size: 10px;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--text-dim);
  opacity: 0.5;
}

@media (max-width: 460px) {
  h1 { font-size: 36px; }
  .pct { font-size: 54px; }
}
</style>
</head>
<body>

<main class="frame">
  <div class="eyebrow">The loyalty test</div>
  <h1>How much of a<br>pirate are you?</h1>
  <p class="lede">Enter your name. The wheel does not deal in luck &mdash;<br>it deals in fate. Your loyalty to <em>Savage</em> awaits.</p>
  <div class="rule"></div>

  <input id="nameInput" class="name-input" type="text" placeholder="Your name" maxlength="40" autocomplete="off">

  <div class="dial-wrap">
    <svg width="210" height="210" viewBox="0 0 210 210">
      <circle class="dial-track" cx="105" cy="105" r="96"></circle>
      <circle id="dialFill" class="dial-fill" cx="105" cy="105" r="96"
              stroke-dasharray="603.2" stroke-dashoffset="603.2"></circle>
    </svg>
    <div class="dial-center">
      <div class="pct"><span id="pctNum">0</span><sup>%</sup></div>
    </div>
  </div>

  <div id="tierLabel" class="tier-label">&nbsp;</div>
  <div id="tierSub" class="tier-sub">Consult the wheel</div>

  <button id="spinBtn" class="spin-btn">Consult the wheel</button>
  <p class="hint">The same name always meets the same fate.</p>

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

<script>
const spinBtn = document.getElementById('spinBtn');
const pctNum = document.getElementById('pctNum');
const tierLabel = document.getElementById('tierLabel');
const tierSub = document.getElementById('tierSub');
const storyBox = document.getElementById('story');
const storyText = document.getElementById('storyText');
const nameInput = document.getElementById('nameInput');
const dialFill = document.getElementById('dialFill');
const soundToggle = document.getElementById('soundToggle');
const volumeSlider = document.getElementById('volume');

const CIRC = 603.2;

function setDial(pct, savage) {
  dialFill.style.strokeDashoffset = CIRC - (CIRC * pct) / 100;
  dialFill.classList.toggle('savage', !!savage);
}

spinBtn.addEventListener('click', async () => {
  spinBtn.disabled = true;
  storyBox.classList.add('hidden');
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
  const url = name ? `/api/spin?name=${encodeURIComponent(name)}` : '/api/spin';

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

    if (data.story) {
      storyText.textContent = data.story;
      storyBox.classList.remove('hidden');
    }

    spinBtn.disabled = false;
  }, maxTicks * 80);
});

/* ---- Ambience: quiet ocean air, OFF by default ----
   Generated with the Web Audio API: filtered noise swells like distant
   surf, plus a very low, slow drone. No files, no copyright, no melody
   to get stuck in your head. */

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
  lp.type = 'lowpass';
  lp.frequency.value = 420;
  lp.Q.value = 0.4;

  const swell = ctx.createGain();
  swell.gain.value = 0.25;

  const lfo = ctx.createOscillator();
  lfo.frequency.value = 0.07;
  const lfoGain = ctx.createGain();
  lfoGain.gain.value = 0.15;
  lfo.connect(lfoGain);
  lfoGain.connect(swell.gain);

  noise.connect(lp); lp.connect(swell); swell.connect(master);

  const drone = ctx.createOscillator();
  drone.type = 'sine';
  drone.frequency.value = 55;
  const droneGain = ctx.createGain();
  droneGain.gain.value = 0.05;
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


@app.route("/api/spin")
def spin():
    name = request.args.get("name", "").strip()
    if name:
        pct, story = spin_for_name(name)
    else:
        pct = random.randint(1, 100)
        story = random.choice(STORIES) if pct > 95 else None
    tier = get_tier(pct)
    result = {"percent": pct, "tier": tier["label"], "sub": tier["sub"]}
    if story:
        result["story"] = story
    return jsonify(result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
