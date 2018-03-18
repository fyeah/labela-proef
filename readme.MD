## Setup and run steps
### Database
Create a new user inside psql.  
`CREATE USER lba WITH password 'a';`

And create a new database.  
`CREATE DATABASE lbaproef;`

And grant priviliges.  
`GRANT ALL PRIVILEGES ON DATABASE lbaproef to lba;`

The backend expects postgresql to run on the default localhost port 5432.

### Python API

Clone this repository.

Create a Python virtual environment inside it.  
`python3 -m venv ./env` (I used virtualenv).

Activate the env.  
`source ./env/bin/activate`

Upgrade packaging tools (not sure if necessary).  
`pip install --upgrade pip setuptools`

Install the project in editable mode with its testing requirements.  
`pip install -e ".[testing]`

Configure the database.  
`initialize_labela_proef_db development.ini`

Run the project.  
`pserve development.ini`

## JSON data to test the endpoints
/product POST:  
`{
	"name": "autoband",
	"description": "Is lekker snel",
	"price": 38.99
}`

/user POST:  
`{
	"email": "yorin@hotmail.com",
	"password": "testen33",
	"first_name": "Yorin",
	"last_name": "Osinga",
	"street": "Duinweg",
	"house_nr": "125D",
	"postcode": "1871AH",
	"city": "Schoorl",
	"country": "The Netherlands"
}`

## Next steps 
-finish basic /order routes (create, getAll, getById)  
-add authentication for users/admins (add admin as user or seperate entity), I like JWT bearer token.  
-add authorization for user/admin routes.  
-implement product, user and order update/delete etc.  
-improve request validation and error messages.  
-tax handling.  
