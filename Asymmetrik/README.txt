README file for Asymmetrik Business Card OCR challenge
*Please note: this solution works under the assumption that the OCR outputs the text of the business card into a text file.

Before running the code, ensure that Python is downloaded on your computer. Python 64-bit is recommended.
After python is installed-
open the command line and run "pip install regex"
run the command "pip install -U spacy"
run the command "pip install -U spacy-lookups-data"
run the command "python -m spacy download en_core_web_sm"
These libraries will enable the code to run properly

To run the code in windows command line/powershell:
Navigate to the code using cd and user directories.
	Typically, this will look like "cd desktop" -> "cd Asymmetrik"
Then type python followed by the file name:
	"python Asymmetrik.py"
This will run the code
After the code runs, it will prompt you for a test number
This will be a number 1-5 and will call the corresponding test.txt file
The txt files can be opened to compare output.

To run the code on 