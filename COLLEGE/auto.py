from flask import Flask, jsonify, render_template_string
import threading
import time
import webbrowser
import pyautogui

app = Flask(__name__)

# background thread control
_refresh_thread = None
_refresh_stop_event = threading.Event()
interval_seconds = 5
target_url = "https://fast.com"

HTML_PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>fast.com refresher (Python)</title>
  <style>
    body { font-family: system-ui, sans-serif; margin: 40px; max-width:700px; }
    button { padding:10px 14px; margin-right:8px; }
    #status { margin-top:10px; color:#333; }
  </style>
</head>
<body>
  <h2>fast.com auto-refresh (Python + pyautogui)</h2>
  <p>Click Start to open <strong>fast.com</strong> and begin refreshing it every 5 seconds. Click Stop to stop.</p>

  <button id="start">Start</button>
  <button id="stop" disabled>Stop</button>
  <div id="status">Status: <span id="state">stopped</span></div>

  <script>
    const startBtn = document.getElementById('start');
    const stopBtn = document.getElementById('stop');
    const stateEl = document.getElementById('state');

    startBtn.addEventListener('click', async () => {
      startBtn.disabled = true;
      const res = await fetch('/start', { method: 'POST' });
      const j = await res.json();
      stateEl.textContent = j.status;
      stopBtn.disabled = false;
    });

    stopBtn.addEventListener('click', async () => {
      stopBtn.disabled = true;
      const res = await fetch('/stop', { method: 'POST' });
      const j = await res.json();
      stateEl.textContent = j.status;
      startBtn.disabled = false;
    });

    // optional: poll status
    setInterval(async () => {
      const res = await fetch('/status');
      const j = await res.json();
      stateEl.textContent = j.status;
      startBtn.disabled = (j.running === true);
      stopBtn.disabled = (j.running !== true);
    }, 2000);
  </script>
</body>
</html>
"""

def refresher_loop(stop_event: threading.Event):
    """Background loop: press F5 every interval_seconds while not stopped."""
    # Give initial time for browser to open
    time.sleep(3)
    while not stop_event.is_set():
        # Send F5 to active window — ensure browser is active or bring it to front yourself
        try:
            pyautogui.press('f5')
            print("Pressed F5 (refreshed).")
        except Exception as e:
            print("pyautogui error:", e)
        # wait interval or break if stopped
        stop_event.wait(interval_seconds)

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/start', methods=['POST'])
def start():
    global _refresh_thread, _refresh_stop_event
    if _refresh_thread and _refresh_thread.is_alive():
        return jsonify(status="already running", running=True)

    # Clear previous event and start new thread
    _refresh_stop_event = threading.Event()
    # Open target URL in default browser (new window/tab)
    webbrowser.open(target_url)
    # Start background thread
    _refresh_thread = threading.Thread(target=refresher_loop, args=(_refresh_stop_event,), daemon=True)
    _refresh_thread.start()
    return jsonify(status="running", running=True)

@app.route('/stop', methods=['POST'])
def stop():
    global _refresh_thread, _refresh_stop_event
    if _refresh_thread and _refresh_thread.is_alive():
        _refresh_stop_event.set()
        _refresh_thread.join(timeout=1.0)
        _refresh_thread = None
        return jsonify(status="stopped", running=False)
    else:
        return jsonify(status="not running", running=False)

@app.route('/status')
def status():
    running = _refresh_thread is not None and _refresh_thread.is_alive()
    return jsonify(status="running" if running else "stopped", running=running)

if __name__ == '__main__':
    print("Starting Flask server at http://127.0.0.1:5000")
    app.run(debug=False)
