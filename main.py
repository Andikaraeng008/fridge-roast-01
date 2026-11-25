"""Fridge Roast entry: write the one-line roast to output/entry.txt.

One concrete scene (the fridge rating my milk in front of guests) plus a
final-phrase twist that reverses who needs replacing.
"""
import os

LINE = "My smart fridge rated my milk 'past its prime' in front of my guests, then suggested I replace it \u2014 it meant me, not the milk."

def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
