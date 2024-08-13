from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from app.models import User, Inference 

from alembic import context
from app.databases import SQLALCHEMY_DATABASE_URL, Base

# Đọc cấu hình Alembic
config = context.config
fileConfig(config.config_file_name)

# Thiết lập đối tượng Base để tự động tìm kiếm các mô hình ORM của bạn
target_metadata = Base.metadata

# Thiết lập URL kết nối cho Alembic
config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)

def run_migrations_offline():
    """Chạy di trú trong chế độ ngoại tuyến."""
    context.configure(
        url=SQLALCHEMY_DATABASE_URL, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Chạy di trú trong chế độ trực tuyến."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()