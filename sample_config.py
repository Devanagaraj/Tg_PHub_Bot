HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ

    TOKEN = environ["TOKEN"]
    ARQ_KEY = environ["ARQ_API_KEY"]

# NOTE Fill this if you are not deploying on heroku.
else:
    TOKEN = "Insert Bot_Token Here"
    ARQ_KEY = "Get this from @ARQRobot"
