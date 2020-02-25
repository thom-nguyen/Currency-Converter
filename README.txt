How to use currency_convert.exe:

0) If input and/or output .csv files are desired, make sure they are located in the same folder as currency_convert.exe
1) Open and run currency_convert.exe
2) Enter required input fields (no leading/trailing whitespaces)
	currency_convert
		Field Name: <field name>
		Multiplier: <multiplier>
		Input File: <input file/"none" if no input file desired>
		Output File: <output file/"None" if no output file desired

	2a) If no input and/or output file specified, program will use stdin and stdout respectively.
	2b) If no input file specified, enter data line-by-line by typing in values separated using commas (no leading/trailing whitespaces).
	    Input "DONE" when no more rows are to be added.

3) Enter conversion type
	'0' for USD to EUR
	'1' for EUR to USD
4) Output will either be written in specified output .csv file, or printed to the terminal.
