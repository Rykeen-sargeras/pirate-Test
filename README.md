:root {
  --wood-dark: #2b1a0f;
  --wood-mid: #4a2f1c;
  --wood-light: #6b4226;
  --parchment: #f1e2c1;
  --parchment-dark: #d8c090;
  --gold: #d4a441;
  --gold-bright: #f2c14e;
  --ink: #2b1a0f;
  --sea-deep: #0b2e3a;
  --sea-mid: #14495c;
  --danger: #7a1f1f;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  min-height: 100vh;
  font-family: 'Merriweather', serif;
  color: var(--parchment);
  background: linear-gradient(180deg, var(--sea-deep) 0%, var(--sea-mid) 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem 1rem;
  position: relative;
  overflow-x: hidden;
}

.ocean {
  position: fixed;
  inset: 0;
  background:
    radial-gradient(circle at 20% 30%, rgba(242, 193, 78, 0.06), transparent 40%),
    repeating-linear-gradient(45deg, rgba(255,255,255,0.02) 0px, rgba(255,255,255,0.02) 2px, transparent 2px, transparent 20px);
  z-index: 0;
}

.ship-card {
  position: relative;
  z-index: 1;
  background: var(--wood-mid);
  border: 6px solid var(--wood-dark);
  border-radius: 16px;
  box-shadow: 0 0 0 3px var(--gold), 0 20px 40px rgba(0,0,0,0.5);
  max-width: 480px;
  width: 100%;
  padding: 2rem 1.75rem;
  text-align: center;
}

.title {
  font-family: 'Pirata One', cursive;
  font-size: 42px;
  line-height: 1.1;
  color: var(--gold-bright);
  margin: 0 0 0.5rem;
  text-shadow: 2px 2px 0 var(--ink);
}

.subtitle {
  font-size: 15px;
  color: var(--parchment-dark);
  margin: 0 0 1.5rem;
}

.subtitle strong {
  color: var(--gold-bright);
}

.name-input {
  width: 100%;
  font-family: 'Merriweather', serif;
  font-size: 15px;
  color: var(--ink);
  background: var(--parchment);
  border: 3px solid var(--gold);
  border-radius: 8px;
  padding: 10px 14px;
  margin-bottom: 1.25rem;
}

.name-input::placeholder {
  color: var(--wood-light);
  opacity: 0.7;
}

.wheel-frame {
  background: var(--parchment);
  color: var(--ink);
  border: 4px dashed var(--gold);
  border-radius: 50%;
  width: 160px;
  height: 160px;
  margin: 0 auto 1.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.pct {
  font-family: 'Pirata One', cursive;
  font-size: 44px;
}

.tier {
  min-height: 24px;
  font-size: 16px;
  color: var(--gold-bright);
  margin-bottom: 1.5rem;
  font-weight: 700;
}

.spin-btn {
  font-family: 'Pirata One', cursive;
  font-size: 20px;
  letter-spacing: 1px;
  background: var(--gold);
  color: var(--ink);
  border: 3px solid var(--wood-dark);
  border-radius: 10px;
  padding: 12px 28px;
  cursor: pointer;
  transition: transform 0.1s ease, background 0.2s ease;
}

.spin-btn:hover {
  background: var(--gold-bright);
}

.spin-btn:active {
  transform: scale(0.96);
}

.spin-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.hint {
  font-size: 12px;
  color: var(--parchment-dark);
  margin: 10px 0 0;
  opacity: 0.8;
}

.story-box {
  margin-top: 1.5rem;
  background: var(--parchment);
  color: var(--ink);
  border: 3px solid var(--gold);
  border-radius: 10px;
  padding: 1rem 1.25rem;
  text-align: left;
}

.story-box.hidden {
  display: none;
}

.story-label {
  font-family: 'Pirata One', cursive;
  font-size: 18px;
  color: var(--danger);
  margin: 0 0 6px;
}

.story-text {
  font-size: 14px;
  line-height: 1.6;
  margin: 0;
}

.footer {
  position: relative;
  z-index: 1;
  margin-top: 2rem;
  font-size: 12px;
  color: var(--parchment-dark);
  opacity: 0.7;
}
