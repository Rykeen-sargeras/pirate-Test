import os
import random
import hashlib
from flask import Flask, jsonify, request

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


def get_tier(pct):
    for tier in TIERS:
        if pct <= tier["max"]:
            return tier["label"]
    return TIERS[-1]["label"]


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
  <title>How Much of a Pirate Are You?</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Pirata+One&family=Inter:wght@400;600&display=swap" rel="stylesheet">
  <style>
:root {
  --bg-0: #0a1220;
  --bg-1: #101c30;
  --card: rgba(255, 255, 255, 0.04);
  --card-border: rgba(255, 255, 255, 0.08);
  --gold: #e8b64c;
  --gold-soft: rgba(232, 182, 76, 0.15);
  --text: #eef2f7;
  --text-dim: #93a1b5;
  --teal: #35d0ba;
  --red: #ff5d5d;
  --radius: 20px;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html,
body {
  cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'><path d='M4 28 L6 26 C4 18 8 8 20 3 C26 1 30 2 30 2 C30 2 29 7 25 12 C19 20 12 24 7 25 L5 29 Z' fill='%23c8cfd8' stroke='%232b3240' stroke-width='1.5'/><path d='M5 29 L9 25 L11 27 L7 31 Z' fill='%23e8b64c' stroke='%238a6a20' stroke-width='1'/></svg>") 2 30, auto;
}

body {
  min-height: 100vh;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  color: var(--text);
  background:
    radial-gradient(1200px 600px at 80% -10%, rgba(53, 208, 186, 0.08), transparent 60%),
    radial-gradient(900px 500px at 10% 110%, rgba(232, 182, 76, 0.07), transparent 60%),
    linear-gradient(180deg, var(--bg-0), var(--bg-1));
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem 1rem;
  overflow-x: hidden;
}

button,
input,
a {
  cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'><path d='M4 28 L6 26 C4 18 8 8 20 3 C26 1 30 2 30 2 C30 2 29 7 25 12 C19 20 12 24 7 25 L5 29 Z' fill='%23e8b64c' stroke='%238a6a20' stroke-width='1.5'/><path d='M5 29 L9 25 L11 27 L7 31 Z' fill='%23c8cfd8' stroke='%232b3240' stroke-width='1'/></svg>") 2 30, pointer;
}

.waves {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 200%;
  height: 90px;
  background: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 90' preserveAspectRatio='none'><path d='M0 45 Q150 10 300 45 T600 45 T900 45 T1200 45 V90 H0 Z' fill='rgba(53,208,186,0.06)'/></svg>") repeat-x;
  background-size: 50% 100%;
  animation: drift 14s linear infinite;
  pointer-events: none;
}

@keyframes drift {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}

.card {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 440px;
  background: var(--card);
  border: 1px solid var(--card-border);
  border-radius: var(--radius);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  padding: 2.25rem 2rem;
  text-align: center;
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.35);
}

.flag {
  font-size: 34px;
  line-height: 1;
  margin-bottom: 0.75rem;
}

h1 {
  font-family: 'Pirata One', cursive;
  font-weight: 400;
  font-size: 40px;
  line-height: 1.05;
  letter-spacing: 0.5px;
  color: var(--text);
  margin-bottom: 0.4rem;
}

h1 span {
  color: var(--gold);
}

.subtitle {
  font-size: 14px;
  color: var(--text-dim);
  margin-bottom: 1.75rem;
}

.subtitle strong {
  color: var(--gold);
  font-weight: 600;
}

.name-input {
  width: 100%;
  font-family: inherit;
  font-size: 15px;
  color: var(--text);
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--card-border);
  border-radius: 12px;
  padding: 13px 16px;
  margin-bottom: 1.5rem;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.name-input::placeholder {
  color: var(--text-dim);
}

.name-input:focus {
  border-color: var(--gold);
  box-shadow: 0 0 0 3px var(--gold-soft);
}

.dial-wrap {
  position: relative;
  width: 190px;
  height: 190px;
  margin: 0 auto 1.25rem;
}

.dial-wrap svg {
  transform: rotate(-90deg);
}

.dial-track {
  fill: none;
  stroke: rgba(255, 255, 255, 0.07);
  stroke-width: 10;
}

.dial-fill {
  fill: none;
  stroke: var(--gold);
  stroke-width: 10;
  stroke-linecap: round;
  transition: stroke-dashoffset 0.35s ease, stroke 0.35s ease;
}

.dial-fill.savage {
  stroke: var(--red);
}

.dial-center {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.pct {
  font-family: 'Pirata One', cursive;
  font-size: 46px;
  color: var(--text);
}

.pct-label {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--text-dim);
}

.tier {
  min-height: 22px;
  font-size: 15px;
  font-weight: 600;
  color: var(--gold);
  margin-bottom: 1.5rem;
}

.spin-btn {
  width: 100%;
  font-family: 'Pirata One', cursive;
  font-size: 22px;
  letter-spacing: 1px;
  color: #171207;
  background: linear-gradient(135deg, var(--gold), #f5d47a);
  border: none;
  border-radius: 14px;
  padding: 14px 0;
  transition: transform 0.12s ease, filter 0.2s ease;
}

.spin-btn:hover {
  filter: brightness(1.08);
}

.spin-btn:active {
  transform: scale(0.97);
}

.spin-btn:disabled {
  opacity: 0.55;
}

.hint {
  font-size: 12px;
  color: var(--text-dim);
  margin-top: 0.9rem;
}

.story-box {
  margin-top: 1.5rem;
  background: var(--gold-soft);
  border: 1px solid rgba(232, 182, 76, 0.35);
  border-radius: 14px;
  padding: 1.1rem 1.25rem;
  text-align: left;
  animation: rise 0.4s ease;
}

@keyframes rise {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

.story-box.hidden {
  display: none;
}

.story-label {
  font-family: 'Pirata One', cursive;
  font-size: 17px;
  color: var(--gold);
  margin-bottom: 5px;
}

.story-text {
  font-size: 13.5px;
  line-height: 1.65;
  color: var(--text);
}

.music-bar {
  position: relative;
  z-index: 1;
  margin-top: 1.25rem;
  width: 100%;
  max-width: 440px;
  display: flex;
  align-items: center;
  gap: 14px;
  background: var(--card);
  border: 1px solid var(--card-border);
  border-radius: 999px;
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  padding: 10px 18px;
}

.mute-btn {
  flex: 0 0 auto;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  border: 1px solid var(--card-border);
  background: rgba(255, 255, 255, 0.05);
  color: var(--gold);
  font-size: 17px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}

.mute-btn:hover {
  background: rgba(255, 255, 255, 0.1);
}

.music-label {
  font-size: 12px;
  color: var(--text-dim);
  white-space: nowrap;
}

.volume {
  flex: 1;
  -webkit-appearance: none;
  appearance: none;
  height: 5px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.12);
  outline: none;
}

.volume::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--gold);
  border: 2px solid #171207;
}

.volume::-moz-range-thumb {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--gold);
  border: 2px solid #171207;
}

.footer {
  position: relative;
  z-index: 1;
  margin-top: 1.5rem;
  font-size: 12px;
  color: var(--text-dim);
  opacity: 0.7;
}

@media (max-width: 480px) {
  h1 { font-size: 33px; }
  .card { padding: 1.75rem 1.25rem; }
}

</style>
</head>
<body>
  <div class="waves"></div>

  <main class="card">
    <div class="flag">&#127988;&#8205;&#9760;&#65039;</div>
    <h1>How much of a <span>pirate</span> are ye?</h1>
    <p class="subtitle">Spin the wheel and find yer true loyalty to <strong>Savage</strong></p>

    <input id="nameInput" class="name-input" type="text" placeholder="Enter yer pirate name" maxlength="40">

    <div class="dial-wrap">
      <svg width="190" height="190" viewBox="0 0 190 190">
        <circle class="dial-track" cx="95" cy="95" r="84"></circle>
        <circle id="dialFill" class="dial-fill" cx="95" cy="95" r="84"
                stroke-dasharray="527.8" stroke-dashoffset="527.8"></circle>
      </svg>
      <div class="dial-center">
        <div id="pct" class="pct">0%</div>
        <div class="pct-label">pirate blood</div>
      </div>
    </div>

    <div id="tier" class="tier">press spin to find yer pirate soul</div>

    <button id="spinBtn" class="spin-btn">Spin the Wheel</button>
    <p class="hint">Same name, same fate every time &mdash; it's a hash, not luck.</p>

    <div id="story" class="story-box hidden">
      <p class="story-label">True loyalty to Savage</p>
      <p id="storyText" class="story-text"></p>
    </div>
  </main>

  <div class="music-bar">
    <button id="muteBtn" class="mute-btn" aria-label="Toggle music">&#9835;</button>
    <span class="music-label">Shanty</span>
    <input id="volume" class="volume" type="range" min="0" max="100" step="1" value="35" aria-label="Music volume">
  </div>

  <footer class="footer">Yarrr &mdash; built for the crew</footer>

  <script>
const spinBtn = document.getElementById('spinBtn');
const pctEl = document.getElementById('pct');
const tierEl = document.getElementById('tier');
const storyBox = document.getElementById('story');
const storyText = document.getElementById('storyText');
const nameInput = document.getElementById('nameInput');
const dialFill = document.getElementById('dialFill');
const muteBtn = document.getElementById('muteBtn');
const volumeSlider = document.getElementById('volume');

const CIRCUMFERENCE = 527.8;

function setDial(pct, savage) {
  dialFill.style.strokeDashoffset = CIRCUMFERENCE - (CIRCUMFERENCE * pct) / 100;
  dialFill.classList.toggle('savage', !!savage);
}

/* ---------------- Spin ---------------- */

spinBtn.addEventListener('click', async () => {
  startMusicIfNeeded();
  spinBtn.disabled = true;
  storyBox.classList.add('hidden');
  tierEl.textContent = 'the wheel be spinnin...';

  let ticks = 0;
  const maxTicks = 18;
  const tickInterval = setInterval(() => {
    ticks++;
    const fake = Math.floor(Math.random() * 100) + 1;
    pctEl.textContent = fake + '%';
    setDial(fake, false);
  }, 70);

  const name = nameInput.value.trim();
  const url = name ? `/api/spin?name=${encodeURIComponent(name)}` : '/api/spin';

  let data;
  try {
    const res = await fetch(url);
    data = await res.json();
  } catch (err) {
    clearInterval(tickInterval);
    tierEl.textContent = 'the ship hit a storm, try again';
    spinBtn.disabled = false;
    return;
  }

  setTimeout(() => {
    clearInterval(tickInterval);
    pctEl.textContent = data.percent + '%';
    setDial(data.percent, data.percent > 95);
    tierEl.textContent = data.tier;

    if (data.story) {
      storyText.textContent = data.story;
      storyBox.classList.remove('hidden');
    }

    spinBtn.disabled = false;
  }, maxTicks * 70);
});

/* ---------------- Music ----------------
   A sea-shanty style loop generated live with the Web Audio API.
   No audio files, no copyright - the notes are synthesized in the browser.
*/

let audioCtx = null;
let masterGain = null;
let shantyTimer = null;
let muted = false;

const NOTES = {
  D3: 146.83, F3: 174.61, G3: 196.0, A3: 220.0, Bb3: 233.08, C4: 261.63,
  D4: 293.66, F4: 349.23, G4: 392.0, A4: 440.0, Bb4: 466.16, C5: 523.25, D5: 587.33,
};

// Melody in D minor, [note, beats] - a jaunty original shanty tune
const MELODY = [
  ['D4', 1], ['F4', 1], ['A4', 1], ['F4', 1],
  ['G4', 1], ['A4', 0.5], ['G4', 0.5], ['F4', 1], ['D4', 1],
  ['C4', 1], ['D4', 1], ['F4', 1], ['G4', 1],
  ['A4', 2], ['G4', 1], ['F4', 1],
  ['D4', 1], ['F4', 1], ['A4', 1], ['C5', 1],
  ['D5', 1.5], ['C5', 0.5], ['A4', 1], ['G4', 1],
  ['F4', 1], ['G4', 1], ['A4', 0.5], ['G4', 0.5], ['F4', 1],
  ['D4', 3], ['D4', 1],
];

// Bass line, one note per bar (4 beats)
const BASS = ['D3', 'G3', 'F3', 'A3', 'D3', 'G3', 'F3', 'D3'];

const BPM = 168;
const BEAT = 60 / BPM;

function playNote(freq, startTime, duration, type, gainLevel) {
  const osc = audioCtx.createOscillator();
  const gain = audioCtx.createGain();
  osc.type = type;
  osc.frequency.value = freq;
  gain.gain.setValueAtTime(0, startTime);
  gain.gain.linearRampToValueAtTime(gainLevel, startTime + 0.02);
  gain.gain.setValueAtTime(gainLevel, startTime + duration * 0.7);
  gain.gain.linearRampToValueAtTime(0.0001, startTime + duration);
  osc.connect(gain);
  gain.connect(masterGain);
  osc.start(startTime);
  osc.stop(startTime + duration + 0.05);
}

function scheduleLoop(startTime) {
  let t = startTime;

  // Melody - square wave gives it a fife/whistle feel
  for (const [note, beats] of MELODY) {
    playNote(NOTES[note], t, beats * BEAT * 0.9, 'square', 0.05);
    t += beats * BEAT;
  }

  // Bass - triangle wave, one note per bar
  let bt = startTime;
  for (const note of BASS) {
    playNote(NOTES[note], bt, 4 * BEAT * 0.95, 'triangle', 0.09);
    bt += 4 * BEAT;
  }

  const loopLength = t - startTime;
  shantyTimer = setTimeout(() => scheduleLoop(audioCtx.currentTime + 0.05), (loopLength - 0.2) * 1000);
}

function startMusicIfNeeded() {
  if (audioCtx) {
    if (audioCtx.state === 'suspended') audioCtx.resume();
    return;
  }
  audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  masterGain = audioCtx.createGain();
  masterGain.gain.value = muted ? 0 : volumeSlider.value / 100;
  masterGain.connect(audioCtx.destination);
  scheduleLoop(audioCtx.currentTime + 0.1);
}

function applyVolume() {
  if (!masterGain) return;
  masterGain.gain.setTargetAtTime(muted ? 0 : volumeSlider.value / 100, audioCtx.currentTime, 0.03);
}

volumeSlider.addEventListener('input', () => {
  if (muted && volumeSlider.value > 0) {
    muted = false;
    muteBtn.innerHTML = '&#9835;';
  }
  startMusicIfNeeded();
  applyVolume();
});

muteBtn.addEventListener('click', () => {
  startMusicIfNeeded();
  muted = !muted;
  muteBtn.innerHTML = muted ? '&#128263;' : '&#9835;';
  applyVolume();
});

</script>
</body>
</html>
"""


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
    result = {"percent": pct, "tier": get_tier(pct)}
    if story:
        result["story"] = story
    return jsonify(result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
