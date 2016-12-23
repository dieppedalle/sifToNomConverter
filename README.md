# sifToNomeConverter
## Script to convert .sif files to .nom format.

### Running the script
The code was written using Python 2.7. No external libraries are needed.

To run the script enter the following command:
```
python main.py inputFile outputFile
```
The above command will read inputFile as a .sif file and produce outputFile as a .nom file. The inputFile must be placed in the input folder and the outputFile will be placed in the output folder when the script is run. 

The user can also specify a True flag as a fourth parameter as followed:
```
python main.py inputFile outputFile True
```
### Convert triangle faces to square faces
This True flag will merge the triangle faces into square faces whenever it is possible (as a result less faces will be created).

For example, with the True flag the following faces:
```
face f0 (0 32 31) endface
face f1 (0 63 32) endface
```
would become
```
face f0 (0 32 31 63) endface
```
### Example
The files in the output folder were generated using:
```
python main.py Borromean Borromean True
python main.py input input True
python main.py zero zero True
```

