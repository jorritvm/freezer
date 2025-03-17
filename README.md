# freezer
Freezer content tracker using reflex frontend and fastapi/sqlalchemy backend.


# Developer instructions
install the dependencies using poetry
```
poetry install --no-root
```
run the app
```
reflex run
```
or run in debug mode
```
reflex run --loglevel debug
```

# configuration
FRONTEND_PORT=3001 sets the http port

## database
- the database url is set up in `rxconfig.py` 
- the database models are defined in `models.py`
- the database is created by running `reflex db init`
- when changes to the models are made reflex uses alembic to create a migration script: `reflex db makemigrations --message "something changed"`
- after checking the migration script you can execute it using `reflex db migrate`
- populate with default data: `python freezer\models.py`