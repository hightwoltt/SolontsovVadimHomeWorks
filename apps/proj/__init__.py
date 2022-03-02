# import os

# os.environ['venv_pr']

# def get_env_variable(env_variable: str) -> str:
#     try:
#         return os.environ['venv_pr']
#     except KeyError:
#         raise ImproperlyConfigured(
#             f'Set {venv_pr} environment variable'
#         )


# SECRET_KEY = get_env_variable('SECRET_KEY')