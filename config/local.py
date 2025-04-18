# DB_HOST = "localhost"
# DB_NAME = "locallink_db"
# # SQLALCHEMY_DATABASE_URI = "sqlite:///local.db"

# SQLALCHEMY_DATABASE_URI = (
#     "postgresql://LocalLink_user:password123@localhost:5000/LocalLink_db"
# )


DB_PASSWORD = "3BW6aIwPf9BGnZLW"
DB_NAME = "postgres"
DB_HOST = "aws-0-us-east-2.pooler.supabase.com"
DB_USERNAME = "postgres.pmvkzxhyjawfclueeocx"
DB_PORT = 5432
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Add SECRET_KEY for Flask and JWT
SECRET_KEY = "supersecretkey1234567890"
