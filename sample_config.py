HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ

    Bot_token = environ["Bot_Token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    Bot_token = "Insert Bot_Token Here"
    ARQ_API_KEY = "Get this from @ARQRobot"
