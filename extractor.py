import colorama as clr
clr.init(autoreset=True)

import os, shutil, math, hashlib

PADDING = 1
ACCEPTED_EXTENSIONS = ['.jpg', '.jpeg', '.png']

### Rename files in directory path
def rename_files(dirpath, mode="numerical"):
    global PADDING
    root = os.getcwd()
    os.chdir(dirpath)
    i = 1
    for filename in os.listdir():
        ext = get_extension(filename)
        filepath = f"{dirpath}/{filename}"
        if mode == "numerical":
            os.rename(filepath, f"{dirpath}/image{add_zeros(i, PADDING)}{ext}")
            i += 1
        elif mode == "md5":
            md5 = get_md5(filepath)
            os.rename(filepath, f"{dirpath}/{md5}{ext}")
        else:
            raise ValueError(clr.Fore.RED + "### mode must be either \"numerical\" or \"md5\"")
    os.chdir(root)

### Extract files from src_dir to dest_dir. Only files with accepted extensions are extracted. After extraction files are renamed to
### their MD5 hash and their extension is lowercased
def extract_files(src_dir, dest_dir):
    global ACCEPTED_EXTENSIONS
    for root, dirnames, filenames in os.walk(src_dir):
        print("### Extracting " + root)
        for filename in filenames:
            filepath = f"{root}/{filename}"
            ext = get_extension(filename)
            md5 = get_md5(filepath)
            new_filename = md5 + ext.lower()
            # Check if extension is unacceptable
            if ext.lower() not in ACCEPTED_EXTENSIONS:
                print(clr.Fore.YELLOW + f"### {filename} ignored due to unaccepted extension")
                continue
            # Check if filename already exists in dest_dir
            if new_filename in os.listdir(dest_dir):
                print(clr.Fore.YELLOW + f"### {filename} already in destination as {new_filename}")
                continue
            shutil.copy(filepath, f"{dest_dir}/{new_filename}")
            print(clr.Fore.GREEN + f"### Copied {filename} as {new_filename}")

### Get file's MD5 hash
def get_md5(filepath):
    with open(filepath, "rb") as f:
        digest = hashlib.file_digest(f, "md5")
    return digest.hexdigest()

### Get file extension
def get_extension(filename):
    try:
        ind = filename.index('.')
        return filename[ind:]
    except ValueError:
        print(clr.Fore.RED + f"### {filename} is missing an extension")

### Convert integer i to string with padding of zeros. Useful for file naming
def add_zeros(i, n):
    p = int(math.log10(i))
    return (n-p-1)*'0' + str(i)

root = os.getcwd()
#extract_files(root + "/src", root + "/dest")
rename_files(root + "/dest", "numerical")