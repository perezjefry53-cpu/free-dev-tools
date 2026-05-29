#!/usr/bin/env python3
"""
🔍 Duplicate File Finder Pro - $5
Find and manage duplicate files
"""
import os
import hashlib
from collections import defaultdict

def hash_file(filepath, chunk_size=8192):
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(chunk_size), b''):
                hasher.update(chunk)
        return hasher.hexdigest()
    except:
        return None

def find_duplicates(directory, min_size=1):
    size_map = defaultdict(list)
    
    print("📊 Analyzing files by size...")
    for root, dirs, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            try:
                size = os.path.getsize(path)
                if size >= min_size * 1024:
                    size_map[size].append(path)
            except:
                continue
    
    # Only check files with same size
    hash_map = defaultdict(list)
    print("🔍 Comparing file contents...")
    checked = 0
    total = sum(len(files) for files in size_map.values() if len(files) > 1)
    
    for size, paths in size_map.items():
        if len(paths) < 2:
            continue
        for path in paths:
            file_hash = hash_file(path)
            if file_hash:
                hash_map[file_hash].append(path)
                checked += 1
    
    # Find duplicates
    duplicates = {h: paths for h, paths in hash_map.items() if len(paths) > 1}
    
    return duplicates

def main():
    print("🔍 Duplicate File Finder Pro")
    print("=" * 35)
    
    directory = input("Directory to scan (default: current): ") or "."
    
    if not os.path.isdir(directory):
        print(f"❌ Directory not found: {directory}")
        return
    
    min_kb = input("Min file size in KB (default: 1): ") or "1"
    
    print(f"\nScanning '{directory}'...")
    duplicates = find_duplicates(directory, int(min_kb))
    
    if not duplicates:
        print("\n✅ No duplicates found!")
        return
    
    total_size = 0
    print(f"\n📋 Found {len(duplicates)} duplicate groups:")
    for i, (file_hash, paths) in enumerate(duplicates.items(), 1):
        size = os.path.getsize(paths[0]) / 1024
        total_size += size * (len(paths) - 1)
        print(f"\n  Group {i} ({size:.1f} KB):")
        for path in paths:
            print(f"    📄 {path}")
    
    print(f"\n💾 Potential space saved: {total_size:.1f} KB ({total_size/1024:.2f} MB)")

if __name__ == '__main__':
    main()
