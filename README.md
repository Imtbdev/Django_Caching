# Django_Caching

This project demonstrates the use of various caching backends in Django, including Memcached, file-based cache, local memory cache, and database cache.

## Requirements

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/) for dependency management
- Memcached running on port **11211**

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. Install dependencies with Poetry:

    ```bash
    poetry install
    ```

3. Activate the virtual environment:

    ```bash
    poetry shell
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Memcached

Make sure Memcached is running and listening on port **11211** before starting the Django server.

You can check if Memcached is running by using:

```bash
netstat -ano | findstr :11211
```

If Memcached is not running, start it manually on port 11211.

Without Memcached, some caching features might fall back to alternative cache backends and may work slower.

## Caching in the Project

The project uses multiple cache backends configured in Django:

- **Memcached** (`default`)
- **File-Based Cache** (`filesystem`)
- **Local Memory Cache** (`localmemory`)
- **Database Cache** (`database`)
- **Dummy Cache** (`dummy`)

Switching between cache backends happens at the view level.

---