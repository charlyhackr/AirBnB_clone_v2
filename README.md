# HBNB AirBnB Clone V2

This is the console/command interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON file. We manage the database with the MySQLdb module, we make actions towards it to find and filter specific data we desire. In this project we make a transition between the FileStorage database and the DBstorage.

### Supported classes:
* BaseModel
* State
* User
* City
* Amenity
* Place
* Review

### Commands:
* create - creates an object
* show - shows an object (based on id)
* destroy - destroys an object
* all - shows all objects, of one type or all types
* quit/EOF - quits the console
* help - sees descriptions of commands

To start, navigate to the project folder and enter this command, `./console.py` in the shell.

#### Create
`create <class name>`

Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`

Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`

Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`

Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`