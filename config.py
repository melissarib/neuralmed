from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    basic_auth_username: str = "admin"
    basic_auth_password: str = "Admin123"
    integration_url: str = "localhost/openmrs/ws/rest/v1"

    class Config:
        env_file = ".env"

settings = Settings()
