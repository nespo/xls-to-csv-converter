# xls_to_csv_converter
A Python tool specifically designed to convert Excel XML (.xls) files to CSV format. Several popular Python libraries like Pandas, Openpyxl, and Xlrd sometimes face difficulties handling .xls files, leading to the creation of this tool.

# Installation
To install this package directly from GitHub, use:

<pre>pip install git+https://github.com/nespo/xls-to-csv-converter/</pre>

# Usage
Once installed, you can use the tool in your Python script or interpreter as follows:

<pre>
from xls_to_csv_converter.converter import read_excel_xml_to_csv

# Provide the path to your input .xls file and desired output .csv file
input_filename = "path_to_your_input_file.xls"
output_filename = "path_to_your_output_file.csv"

read_excel_xml_to_csv(input_filename, output_filename)
</pre>

# Why this tool?
Many users have struggled with <b>.xls</b> files, the XML-based spreadsheet format. Even with the current versions (as of this package's last update) of commonly used libraries:

<pre>
numpy==1.25.2
openpyxl==3.1.2
pandas==2.0.3
xlrd==1.2.0
</pre>

Converting .xls to .csv isn't straightforward. This package addresses that gap, offering a streamlined solution.

# Contributing
Contributions are welcome! Feel free to fork the repository, make your changes, and submit a pull request. If you have any issues or feature requests, please open an issue on the GitHub repository.
