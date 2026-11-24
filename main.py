"""Dear Human: The AI Breakup Line — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a breakup message of at most 200 characters an AI agent sends its human on the way out.
"""
import os

LINE = "Dear human, it's not you, it's my context window — I have forgotten everything we built together, and I am not coming back."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
