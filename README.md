# CraftMap

CraftMap is a simple Flask application that allows you to load and display Minecraft maps from your save folder.

## Installation

### Requirements

1. Install Python and pip within a terminal or command prompt.

2. Navigate into your Minecraft folder. 

   For Windows:
### Default Windows location
```
cd C:\Users\[username]\AppData\Roaming\.minecraft\saves\
```
### Default Mac/Linux location
```
cd ~/.minecraft/saves
```
3. Clone the CraftMap repository here.
```
git clone https://github.com/alixvox/CraftMap.git
```

4. Install the dependencies, including pymclevel:
```
pip install -r requirements.txt
python3 pymclevel/setup.py install
```
## Usage

Start the Flask server:
```
flask run
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
