import colorama as clr
clr.init(autoreset=True)

import os, shutil, math, hashlib

ACCEPTED_EXTENSIONS = ['.jpg', '.jpeg', '.png']

### Rename files in directory path. mode must be either "numerical" or "md5"
def rename_files(dirpath, mode="numerical"):
    root = os.getcwd()
    os.chdir(dirpath)
    # Rename files numerically
    if mode == "numerical":
        # Calculate necessary padding
        digits = int(math.log10(len(os.listdir()))) + 1
        for i, filename in enumerate(os.listdir()):
            ext = get_extension(filename)
            filepath = f"{dirpath}/{filename}"
            if mode == "numerical":
                os.rename(filepath, f"{dirpath}/image{pad(i + 1, digits)}{ext}")
    # Rename files hashlike
    elif mode == "md5":
        for filename in os.listdir():
            ext = get_extension(filename)
            filepath = f"{dirpath}/{filename}"
            md5 = get_md5(filepath)
            os.rename(filepath, f"{dirpath}/{md5}{ext}")
    else:
        raise ValueError(clr.Fore.RED + "### mode must be either \"numerical\" or \"md5\"")
    os.chdir(root)

### Extract files from src_dir to dest_dir. Only files with accepted extensions are extracted. After extraction files are renamed to
### their MD5 hash and their extension is lowercased
def extract_files(src_dir, dest_dir):
    global ACCEPTED_EXTENSIONS
    count = 0
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
            count += 1

### Get file's MD5 hash
def get_md5(filepath):
    with open(filepath, "rb") as f:
        digest = hashlib.file_digest(f, "md5")
    return digest.hexdigest()

### Get file extension
def get_extension(filename):
    try:
        ind = len(filename) - 1 - filename[::-1].index('.')
        return filename[ind:]
    except ValueError:
        return ValueError

### Convert integer n to string with padding of zeros. digits specifies the number of digits of the string
def pad(n, digits):
    p = int(math.log10(n)) + 1
    return (digits-p)*'0' + str(n)


if __name__ == "__main__":
    root = os.getcwd()
    src_path = 
    dest_path = 
    extract_files(src_path, dest_path)
    rename_files(dest_path, "numerical")