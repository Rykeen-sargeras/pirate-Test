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
