import hashlib
import time

SUPPORTED_ALGORITHM = ("md5", "sha1", "sha256", "sha512")

def hash_word(word: str, algorithm: str) -> str:
    """Hash a single word using the chosen algorithm."""
    hasher = hashlib.new(algorithm)
    hasher.update(word.encode("utf-8"))
    return hasher.hexdigest()

def load_wordlist(path: str) -> list[str]:
    """Read a wordlist file into a list of stripped words."""
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f if line.strip()]
    
def crack_hash(target_hash: str, algorithm: str, wordlist_path: str):
    """
    Try every word in the wordlist against the target hash.
    Retuns the matching word if found, otherwise None.
    """
    target_hash = target_hash.lower().strip()
    words = load_wordlist(wordlist_path)

    print(f"Loaded {len(words)} words from '{wordlist_path}'")
    print(f"Cracking {algorithm.upper()} hash: {target_hash}\n")

    start_time = time.time()

    for index, word in enumerate(words, start=1):
        attempt_hash = hash_word(word, algorithm)

        if attempt_hash == target_hash:
            elapsed = time.time() - start_time
            print(f"\nMatch found after {index} attempts ({elapsed:.2f}s)")
            return word
        # progress feedback every 10,000 attempts
        if index % 10000 == 0:
            print(f"  ...tried {index} words")

    elapsed = time.time() - start_time
    print(f"\nNo match found after {len(words)} attempts ({elapsed:.2f}s)")
    return None

def get_algorithm_choice():
    """Ask the user which hashing algorithm to use."""
    print("Supported algorithms:" ", ".join(SUPPORTED_ALGORITHM))
    choice = input("Algorithm: ").strip().lower()

    while choice not in SUPPORTED_ALGORITHM:
        print("Invalid input choice.")
        choice = input("Algorithm: ").strip().lower()

    return choice

def main():
    print("== Dictionary Attack Password Cracker ==\n")

    target_hash = input("Target hash: ").strip()
    algorithm = get_algorithm_choice()
    wordlist_path = input("Path to wordlist file: ").strip()

    try:
        result = crack_hash(target_hash, algorithm, wordlist_path)
    except FileNotFoundError:
        print(f"Error: wordlist file '{wordlist_path}' not found.")
        return
    except ValueError:
        print(f"Error: '{algorithm}' is not a valid haahlib algorithm.")
        return

    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found in wordlist.")

if __name__ == "__main__":
    main()

               




