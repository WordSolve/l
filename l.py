#!/usr/bin/env python3
"""
l - The minimalist letter utility
A simple tool for exploring words containing the letter 'l'
"""

import sys
import random


WORDS = [
    "love", "light", "life", "loyal", "learn", "legend",
    "liberty", "lovely", "laughter", "luminous", "limitless",
    "brilliant", "elegant", "simple", "essential", "beautiful",
    "powerful", "peaceful", "playful", "colorful", "meaningful",
    "gentle", "grateful", "helpful", "wonderful", "delightful",
    "celestial", "elemental", "ethereal", "magical", "lyrical",
    "crystal", "pearl", "violet", "coral", "olive",
    "parallel", "level", "spiral", "itual", "avel",
    "liberal", "literal", "ological", "lateral", "plural"
]


def list_words():
    """Display all words in the collection."""
    print(f"\n📝 {len(WORDS)} words containing 'l':\n")
    for i, word in enumerate(WORDS, 1):
        print(f"  {i:2d}. {word}")
    print()


def search_words(pattern):
    """Search for words containing the given pattern."""
    pattern = pattern.lower()
    matches = [w for w in WORDS if pattern in w.lower()]
    
    if matches:
        print(f"\n🔍 Found {len(matches)} word(s) matching '{pattern}':\n")
        for word in matches:
            print(f"  • {word}")
        print()
    else:
        print(f"\n❌ No words found matching '{pattern}'\n")


def random_word():
    """Display a random word from the collection."""
    word = random.choice(WORDS)
    print(f"\n🎲 Random word: {word}\n")


def count_words():
    """Display the count of words."""
    print(f"\n📊 Total words: {len(WORDS)}\n")


def show_help():
    """Display usage information."""
    print("""
╔══════════════════════════════════════╗
║  l - The minimalist letter utility   ║
╚══════════════════════════════════════╝

Usage:
  python3 l.py <command> [arguments]

Commands:
  list          List all words
  search TEXT   Search for words containing TEXT
  random        Display a random word
  count         Show word count
  help          Show this help message

Examples:
  python3 l.py list
  python3 l.py search love
  python3 l.py random

Philosophy:
  One letter. One purpose. Pure minimalism.
""")


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == "list":
        list_words()
    elif command == "search":
        if len(sys.argv) < 3:
            print("\n❌ Error: search requires a pattern\n")
            print("Usage: python3 l.py search <pattern>\n")
        else:
            search_words(sys.argv[2])
    elif command == "random":
        random_word()
    elif command == "count":
        count_words()
    elif command == "help":
        show_help()
    else:
        print(f"\n❌ Unknown command: {command}\n")
        show_help()


if __name__ == "__main__":
    main()
