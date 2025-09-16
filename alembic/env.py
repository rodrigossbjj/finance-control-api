import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context
from app.models import Base  # importa seu Base com metadata

# Configuração padrão do Alembic
config = context.config

# Logging do Alembic
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Aponta para o metadata do seu projeto (models)
target_metadata = Base.metadata

# 🔹 Busca a URL do banco na variável de ambiente
DATABASE_URL = os.getenv("DATABASE_URL")
config.set_main_option("sqlalchemy.url", DATABASE_URL)


def run_migrations_offline() -> None:
    """Rodar migrações em modo offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Rodar migrações em modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
