from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN")
DB = env.str("DB")
UPLOADS = env.str("UPLOADS")