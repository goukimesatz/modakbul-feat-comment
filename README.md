# Campfire API 🔥

A RESTful API built with FastAPI that simulates an ephemeral discussion board.

In this system, topics act as "campfires." They have a limited Time-To-Live (TTL). Users can keep the campfire burning by adding comments (fuel). If a topic goes cold and the TTL expires, a background process permanently sweeps away the topic and all associated comments.

## Tech Stack
* **Framework:** FastAPI (Python)
* **Server:** Uvicorn
* **Data Store:** In-memory Python dictionaries (simulated database)
* **Security:** bcrypt (Password hashing)

## Core Mechanics
1. **Creation:** When a new Topic is created, it is given a TTL of exactly 1 hour.
2. **Fueling the Fire:** Every new Comment added to a Topic extends its TTL by 1 minute.
3. **Sweeping the Ashes:** A background task runs every 60 seconds to check for expired Topics. If `Current Time > TTL`, the Topic and its Comments are permanently deleted.

## How to Run Locally

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn bcrypt
   ```
3. Start the development server:
   ```bash
   uvicorn main:app --reload
   ```
4. Access the interactive API documentation at: `http://127.0.0.1:8000/docs`

## API Endpoints

### Users
* `POST /users/register`: Create a new account (hashes password).
* `POST /users/login`: Authenticate and retrieve User ID.

### Topics
* `POST /topics`: Start a new campfire (requires `owner_id` query param).
* `GET /topics`: List all active, unexpired campfires.

### Comments
* `POST /topics/{topic_id}/comments`: Add a comment to extend the topic's TTL.
* `GET /topics/{topic_id}/comments`: Retrieve all comments for a specific topic.
