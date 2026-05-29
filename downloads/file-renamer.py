#!/usr/bin/env python3
"""
📂 Batch File Renamer Pro - $5
Rename multiple files at once with patterns
"""
import os
import re
import sys

def preview_rename(directory, pattern, replace_with, dry_run=True):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    renamed = 0
    
    for f in files:
        new_name = f.replace(pattern, replace_with)
        if new_name != f:
            old_path = os.path.join(directory, f)
            new_path = os.path.join(directory, new_name)
            if dry_run:
                print(f"  📄 {f} → {new_name}")
            else:
                os.rename(old_path, new_path)
                print(f"  ✅ {f} → {new_name}")
            renamed += 1
    
    return renamed

def main():
    print("📂 Batch File Renamer Pro")
    print("=" * 35)
    
    directory = input("Directory path (default: current): ") or "."
    
    if not os.path.isdir(directory):
        print(f"❌ Directory not found: {directory}")
        return
    
    print(f"\nFiles in '{directory}':")
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for i, f in enumerate(files[:10], 1):
        print(f"  {i}. {f}")
    if len(files) > 10:
        print(f"  ... and {len(files)-10} more")
    
    pattern = input("\nText to replace: ")
    if not pattern:
        print("❌ No pattern specified")
        return
    
    replace_with = input(f"Replace '{pattern}' with: ")
    
    print("\n📋 Preview of changes:")
    count = preview_rename(directory, pattern, replace_with, dry_run=True)
    
    if count == 0:
        print("\nNo files matched the pattern.")
        return
    
    confirm = input(f"\nRename {count} files? (y/N): ").lower()
    if confirm == 'y':
        preview_rename(directory, pattern, replace_with, dry_run=False)
        print(f"\n✅ {count} files renamed successfully!")
    else:
        print("\nCancelled")

if __name__ == '__main__':
    main()
