- Create a Python virtual environment.

    python3 -m venv ./env (or use virtualenv)

- Activate the env
		
		source ./env/bin/activate

- Upgrade packaging tools (not sure if necessary).

    pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    pip install -e ".[testing]"

- Configure the database.

    initialize_labela_proef_db development.ini

- Run the project.

    pserve development.ini


Next steps:
-add authentication for users/admins (add admin as user or seperate entity), I like JWT bearer token.
-add authorization for user/admin routes
-implement product, user and order update/delete etc.
-improve request validation and error messages
-tax handling