# Random Decision App

A simple Flask web app that answers questions with weighted randomness, plus a couple of sarcastic bonus endpoints for roasting and motivation.

## Requirements

- Python 3
- `pip`

## Setup

1. Create and activate a virtual environment if you want:
   - Windows PowerShell:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Run the app:
   ```powershell
   python app.py
   ```
4. Open your browser and visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Project Structure

```text
app.py
decisions.py
templates/
  index.html
static/
  style.css
  script.js
requirements.txt
README.md
```

## API Endpoints

### `GET /`

Renders the main UI.

### `GET /decide?question=<text>`

Returns a JSON response like:

```json
{
  "question": "Should I go outside?",
  "answer": "Maybe",
  "confidence": 0.58
}
```

Behavior:
- Daytime favors more direct answers like `Yes` and `No`
- Late night (10 PM to 4 AM) increases the odds of more chaotic answers

### `GET /random-insult`

Returns a harmless sarcastic roast:

```json
{
  "message": "You overanalyze so hard even your to-do list needs emotional support."
}
```

### `GET /motivation`

Returns a sarcastic motivation message:

```json
{
  "message": "Go make progress. Perfection is just procrastination wearing nicer shoes."
}
```

## Example Usage

Open the app in the browser, type a question, and click `Decide`. You can also use:

- `Roast Me` to fetch a funny insult
- `Motivate Me` to fetch a sarcastic encouragement

You can also call the API directly:

```powershell
Invoke-RestMethod "http://127.0.0.1:5000/decide?question=Should%20I%20order%20pizza%3F"
```
