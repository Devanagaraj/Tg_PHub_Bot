HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ

    TOKEN = environ["TOKEN"]
    ARQ_KEY = environ["ARQ_KEY"]
    API_ID = int(os.environ.get('API_ID'))
    API_HASH = os.environ.get('API_HASH')

# NOTE Fill this if you are not deploying on heroku.
else:
    TOKEN = "Insert Bot-token Here | @Botfather"
    ARQ_KEY = "Get this from @ARQRobot"
    API_ID = 0
    API_HASH = "abcd568990jjj"
