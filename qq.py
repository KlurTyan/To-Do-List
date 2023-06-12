import environ
import os

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(env_file='.env')

print(env('SECRET_KEY'))