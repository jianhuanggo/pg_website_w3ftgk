# Developer Portfolio (Flask + SQLite + Docker)

Simple, customizable portfolio website powered by Flask and SQLite, packaged with Docker for one-command local development and easy deployment.

Video tutorial: <a href="https://youtu.be/RZpMevjnLR8">Watch on YouTube</a>

## Features
- Minimal Flask app with a single page in `templates/index.html`
- Content stored in a lightweight SQLite database (`instance/portfolio.db`)
- One-command Docker setup for local development
- Hot-reload while editing Python, HTML, CSS, or JS
- Easy content seeding via `init_db.py`
- Static assets in `static/` with ready-made icons and thumbnails

## Project Structure
```
/Users/jianhuang/anaconda3/envs/pg_website_13/pg_website_13
├── docker-compose.yml
├── init_db.py
├── instance/
│   └── portfolio.db
├── main.py
├── Procfile
├── README.md
├── requirements.txt
├── static/
│   ├── assets/
│   │   ├── icons/...
│   │   └── thumbnails/...
│   ├── script.js
│   └── style.css
└── templates/
    └── index.html
```

## Quick Start
Prerequisites:
- Docker Desktop or Engine

Run locally with Docker (recommended):

```bash
docker compose up
```

Then open `http://localhost` (or `http://localhost:80`).

Stop the stack:

```bash
docker compose down
```

## Local Development (without Docker)
Prerequisites:
- Python 3.12+

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the Flask app:

```bash
export FLASK_APP=main.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
```

Visit `http://localhost:5000`.

## Customization
- Edit site content in `init_db.py` (profile details, links, projects)
- Tweak styles in `static/style.css`
- Add client interactions in `static/script.js`
- Update markup/components in `templates/index.html`

After editing `init_db.py`, re-seed the database:

```bash
python init_db.py
```

If using Docker, run it inside the running container:

```bash
docker compose ps
docker exec -it <web_container_id_or_name> python /app/init_db.py
```

Tip: Assets live under `static/assets/`. Replace icons or thumbnails with your own images while preserving filenames or adjust references in HTML/CSS.

## Docker Tips
Rebuild the image if dependencies change:

```bash
docker compose build --no-cache
docker compose up --force-recreate
```

View logs:

```bash
docker compose logs -f
```

## Production (Gunicorn)
For a simple production container, use a `Dockerfile` like:

```Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:5000", "main:app"]
```

Build and run locally:

```bash
docker build -t my-portfolio .
docker run -p 80:5000 my-portfolio:latest
```

Or update `docker-compose.yml` to use the pre-built image:

```yaml
services:
    web:
        image: my-portfolio:latest
        ports:
            - "80:5000"
        volumes:
            - ./:/app
        deploy:
            restart_policy:
                condition: any

    updater:
        image: my-portfolio:latest
        command: ["tail", "-f", "/dev/null"]
        volumes:
            - ./:/app
        deploy:
            restart_policy:
                condition: any
```

Optionally, use Docker Swarm for remote deployment:

```bash
docker swarm init
docker stack deploy -c docker-compose.yml my-portfolio
```

After your stack is running, update content without downtime:

```bash
docker ps
docker exec <updater_container_id> python3 /app/init_db.py
```

## Database Notes
- SQLite file: `instance/portfolio.db`
- The `init_db.py` script is idempotent and can be re-run safely to refresh content
- To reset your data: stop the app, delete `instance/portfolio.db`, and run `init_db.py` again

## Troubleshooting
- Port already in use: stop other services on port 80 or change the published port in `docker-compose.yml`
- Changes don’t appear: clear browser cache and confirm container logs via `docker compose logs -f`
- Database locked: wait a moment and retry; avoid running multiple write operations simultaneously

## Learning Resources
- Flask basics: `https://youtu.be/6plVs_ytIH8`
- SQLite intro: `https://youtu.be/Ohj-CqALrwk`
- Flask + SQLite advanced: `https://youtu.be/v3CSQkPJtAc`
- Docker intro: `https://youtu.be/-l7YocEQtA0`

Full tutorial for this template: <a href="https://youtu.be/RZpMevjnLR8">YouTube video</a>

## License
This project is released under the MIT License. See `LICENSE` for details.
