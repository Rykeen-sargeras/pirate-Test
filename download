<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>How Much of a Pirate Are You?</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Pirata+One&family=Inter:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
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

  <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
