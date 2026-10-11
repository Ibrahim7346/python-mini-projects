import os
import hashlib

# mock database of known malware signatures (MD5 Hashes)
MALWARE_DATABASE = {
    "44d88612fea8a8f36de82e1278abb02f": "EICAR Test Virus Standard Pattern",
    "5f4dcc3b5aa765d61d8327deb882cf99": "Trojan.Win32.Generic",
    "b74056157053e18cf085b39bfdb01358": "Ransomeware.Locky.Variant"
}

def calculate_md5(file_path):
    """Calculates the MD5 hash signature of a file."""
    md5_hash = hashlib.md5()
    try:
        # read the file in binary mode in small chunks to handle large files efficiently
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                md5_hash.update(byte_block)
        return md5_hash.hexdigest()
    except (PermissionError, FileNotFoundError):
        return None

def scan_directory(directory_path):
    """Scans a directory and checks all files against the signature database."""
    print(f"[*] Starting signature scan in: {directory_path}\n" + "-"*50)

    if not os.path.exists(directory_path):
        print(f"[!] Error: The path '{directory_path}' does not exist.")
        return
    
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_md5(file_path)

            if file_hash is None:
                continue # skip files that cant be read

            # check if the calculated signature exists in our malware database
            if file_hash in MALWARE_DATABASE:
                print(f"[ALERT] MALWARE DETECTED!")
                print(f"        File: {file_path}")
                print(f"        Signature Match: {file_hash}")
                print(f"        Threat Name: {MALWARE_DATABASE[file_hash]}\n")
            else:
                print(f"[CLEAN] {file_path}")


if __name__ == "__main__":
            # put the exact path to your real folder inside the quotes:
            target_folder = "C:/Users/ibron/OneDrive/Documents"
            # run the scanner on your folder
            scan_directory(target_folder)                     