#!/usr/bin/env python3
"""
Sample Python Application
A simple program to demonstrate git workflow operations
"""

def greet(name="World"):
    """Return a greeting message"""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Add two numbers and return the result"""
    return a + b

def main():
    """Main function"""
    print(greet())
    print(greet("GitHub"))
    print(f"2 + 3 = {add_numbers(2, 3)}")
    print("\nThis is a sample project to demonstrate git operations:")
    print("  - Committing code")
    print("  - Pushing changes")
    print("  - Creating branches")
    print("  - And more!")

if __name__ == "__main__":
    main()
