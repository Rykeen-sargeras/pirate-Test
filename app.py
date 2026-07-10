<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>How Much of a Pirate Are You?</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Pirata+One&family=Merriweather:wght@400;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
  <div class="ocean"></div>

  <main class="ship-card">
    <h1 class="title">How much of a pirate<br>are ye?</h1>
    <p class="subtitle">Spin the wheel and find yer true loyalty to <strong>Savage</strong></p>

    <input id="nameInput" class="name-input" type="text" placeholder="Enter yer pirate name" maxlength="40">

    <div class="wheel-frame">
      <div id="pct" class="pct">0%</div>
    </div>

    <div id="tier" class="tier">press spin to find yer pirate soul</div>

    <button id="spinBtn" class="spin-btn">Spin the Wheel</button>
    <p class="hint">Same name, same fate every time - it's a hash, not luck.</p>

    <div id="story" class="story-box hidden">
      <p class="story-label">True loyalty to Savage</p>
      <p id="storyText" class="story-text"></p>
    </div>
  </main>

  <footer class="footer">Yarrr &mdash; built for the crew</footer>

  <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
