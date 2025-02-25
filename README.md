# txtrndr
Made for a visual arts assignment on chance and randomness

## Installation
This project requires the following dependencies:
- pillow
- argparse

To install the dependencies, run the following command:
```
python -m pip install -r requirements.txt
```

## Usage
```
usage: txtrndr.py [-h] [--dest DEST] [--charset CHARSET] src

Generate a new image with text using a charset

positional arguments:
  src                Source image

options:
  -h, --help         show this help message and exit
  --dest DEST        Destination image
  --charset CHARSET  Charset
```

## Example
```
python txtrndr.py --dest output.png ./example/earth_publicdomain.jpg  
```
![](https://github.com/atparsec/txtrndr/blob/main/example/earth_publicdomain_xcnvs.jpg)

## Charsets
View the `charsets` directory for some example charsets, and for instructions on how to create your own.
