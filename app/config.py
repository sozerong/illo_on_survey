import os

PG_HOST     = os.environ.get("PG_HOST",     "localhost")
PG_PORT     = os.environ.get("PG_PORT",     "5432")
PG_USER     = os.environ.get("PG_USER",     "postgres")
PG_PASSWORD = os.environ.get("PG_PASSWORD", "postgres")
PG_DB       = os.environ.get("PG_DB",       "postgres")

USER_DB_URL = f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
