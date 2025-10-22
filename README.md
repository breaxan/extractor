# extractor

This is a simple Python program to recursively extract files in a source directory to a destination directory. A few notes about its behaviour:
- **A non-empty folder should not be used as the destination directory if it is being used for the first time**, since most of the checks take place during the extraction process.
- Only filenames with an accepted file extension are extracted. The accepted file extensions can be changed through the ACCEPTED_EXTENSIONS global variable.
- The program also includes a function to rename files in a standard manner. Currently this is done with the PADDING global variable, although this is a lazy solution and it should be changed.

Execution should look like this:
1. Create an empty destination directory.
2. Extract the files in a source directory to the destination directory.
3. Repeat 2. as much as you want .
