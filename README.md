# CraftMap

CraftMap is a simple Flask application that allows you to load and display Minecraft maps from your save folder.

## Installation

## Requirements:

1. Install Python and Pip.
2. Open a Terminal or Command Prompt and change into your .minecraft saves folder.

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
python pymclevel.setup.py install
pip install -r requirements.txt
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
