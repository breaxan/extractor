# extractor

This is a simple Python command-line program to recursively extract files in a source directory to a destination directory. A few notes about its behaviour:
- Run the program like this:
  ```console
  foo@bar:~$ python3 extractor.py [src_dir] [dest_dir]
  ```
  src_dir and dest_dir are added to the Current Working Directory to produce the corresponding paths. **You shouldn't provide a full path.**
- **A non-empty folder should not be used as the destination directory if it is being used for the first time**, since most of the checks take place during the extraction process.
- Only filenames with an accepted file extension are extracted. The accepted file extensions can be changed through the ACCEPTED_EXTENSIONS global variable.
- The program also includes a function to rename files in a standard manner.

Execution should look like this:
1. Create an empty destination directory.
2. Extract the files in a source directory to the destination directory.
3. Repeat 2. as much as you want.
