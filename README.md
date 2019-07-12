# 0x00. AirBnB clone - The console

First step in the creation of an AirBnB clone: a command line interpreter to manage objects.
The building of this console  includes:
* A base data model
* A command line interpreter
* A storage engine (file storage)

### Usage
To execute our console
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
And in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) $

```
### The command line interpreter (The Console)
To use the following comands first execute the console by typing `./console` . Then type any of the commands bellow:

| Command                                                      | Description                                  |
|:------------------------------------------------------------ |:---------------------------------------                       
| `quit`                                                       | Quits the console                            |
| `help` or `help <cmd>`                                       | shows documentation for any existing command |
| `create <class>`                                             | creates an intannce, saves and prints its id |
| `all` or `all <class>`                                       | shows all instances or specific ones         |
| `show <class> <id>` or `<class>.show(<id>)`                  | show a specified object                      |
| `destroy <class> <id>` or `<class>.destroy(<id>)`            | removes an object or instance                |
| `update <class> <id> <attribute name> "<attribute value>"`   | updates an attribute with a new valu         |

### The Base Model
To see the file cd to models/base_model.py
Defines all common methods and attributes of future classes and objects.
Public instance attributes:
- id: string: Generates a unique uuid when a BaseModel instance is created.
- created_at: Contains date and time information of an instance when it is first created.
- updated_at: Contains date and time information of an instance when it is updated.
Methods:
- __str__: prints: [<class name>] (<self.id>) <self.__dict__>
Public instance methods:
- save(self): updates the public instance attribute updated_at with the current datetime
- to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance

### File Storage
Class that inherits from BaseModel class: to see file cd to models/engines/file_storage.py.
The storage engine type used for this project is file storage with the use of serializatiton and deserialization processes to store objects. Implemented in: `file_storage.py`
Data flow of the serialization to desearialization process:
`<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>`
Private class attributes:
- __file_path: string path to the JSON file (ex: file.json)
- __objects: dictionary will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
Public instance methods:
- all(self): returns the dictionary __objects
- new(self, obj): sets in __objects the obj with key <obj class name>.id
- save(self): serializes __objects to the JSON file (path: __file_path)
- reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)
 
### More Classes
Additional classes that inherit from BaseModel:

Class Name | Attributes
-- | --
`User` | email, password, first_name, last_name
`Amenity` | Name
`Review` | place_id, user_id, text
`State`  | Name
`City` | state_id, name
`Place` | city_id, user_id, name, description, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids

### About
Created on Ubuntu 14.04 LTS. Using python3 version 3.4.3.

### Authors
* **Sofia Cheung** - [Svcg17](https://github.com/Svcg17)
* **Kenneth Mensah** - [Ken-Mens](https://github.com/Ken-Mens)
