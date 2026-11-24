import os

# Funniest time machine warning entry
ENTRY_TEXT = "WARNING: Do not kill your grandfather. Paperwork for paradoxes takes 6–8 business eternities."

def main():
    # Write the entry to /output/entry.txt
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")

if __name__ == "__main__":
    main()
