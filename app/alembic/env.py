from logging.config import fileConfig
import os
import sys

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from core.db.models import Base
from alembic import context

CONTAINER_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if CONTAINER_ROOT not in sys.path:
    sys.path.append(CONTAINER_ROOT)

config = context.config
fileConfig(config.config_file_name)

USER = os.getenv("POSTGRES_USER", "postgres")
PASS = os.getenv("POSTGRES_PASSWORD", "postgres")
DB = os.getenv("POSTGRES_DB", "postgres")
DB_HOST = "localhost"
DB_PORT = os.getenv("POSTGRES_PORT", 5432)
CONFIG_SECTION = "sqlalchemy.url"
db_connection = f"postgresql://{USER}:{PASS}@{DB_HOST}:{DB_PORT}/{DB}"

config.set_main_option(CONFIG_SECTION, db_connection)

target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option(CONFIG_SECTION)
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            version_table_schema=target_metadata.schema,
            include_schemas=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
