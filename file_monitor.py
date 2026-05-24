#!/usr/bin/env python3
import hashlib
import os
import json
from datetime import datetime

class FileIntegrityMonitor:
    """Monitor files for unauthorized changes"""
    
    def __init__(self):
        self.baseline = {}
        self.baseline_file = "baseline.json"
        self.log_file = "integrity_log.txt"
    
    def calculate_hash(self, filepath):
        """Calculate SHA256 hash of a file"""
        sha256 = hashlib.sha256()
        
        try:
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def create_baseline(self, filepath):
        """Create baseline hash for a file"""
        hash_value = self.calculate_hash(filepath)
        
        if hash_value:
            self.baseline[filepath] = {
                'hash': hash_value,
                'timestamp': datetime.now().isoformat()
            }
            print(f"✅ Baseline created: {filepath}")
            return True
        return False
    
    def save_baseline(self):
        """Save baseline to JSON file"""
        try:
            with open(self.baseline_file, 'w') as f:
                json.dump(self.baseline, f, indent=2)
            print(f"✅ Baseline saved to {self.baseline_file}")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def load_baseline(self):
        """Load baseline from JSON file"""
        try:
            if os.path.exists(self.baseline_file):
                with open(self.baseline_file, 'r') as f:
                    self.baseline = json.load(f)
                print(f"✅ Baseline loaded")
                return True
            else:
                print("❌ Baseline file not found!")
                return False
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def check_file(self, filepath):
        """Check if file has been modified"""
        if filepath not in self.baseline:
            print(f"❌ File not in baseline: {filepath}")
            return None
        
        current_hash = self.calculate_hash(filepath)
        baseline_hash = self.baseline[filepath]['hash']
        
        if current_hash == baseline_hash:
            return {
                'status': 'OK',
                'message': f"✅ {filepath} - No changes"
            }
        else:
            return {
                'status': 'MODIFIED',
                'message': f"⚠️ {filepath} - MODIFIED!",
                'previous': baseline_hash,
                'current': current_hash
            }
    
    def check_all_files(self):
        """Check all files in baseline"""
        print("\n" + "="*50)
        print("CHECKING ALL FILES...")
        print("="*50 + "\n")
        
        changes = []
        
        for filepath in self.baseline:
            result = self.check_file(filepath)
            
            if result['status'] == 'MODIFIED':
                print(result['message'])
                changes.append(result)
            else:
                print(result['message'])
        
        print("\n" + "="*50)
        if changes:
            print(f"⚠️ {len(changes)} file(s) modified!")
        else:
            print("✅ All files intact!")
        print("="*50 + "\n")

def main():
    monitor = FileIntegrityMonitor()
    
    print("\n" + "="*50)
    print("FILE INTEGRITY MONITOR v1.0")
    print("="*50 + "\n")
    
    while True:
        print("MENU:")
        print("1. Create baseline")
        print("2. Save baseline")
        print("3. Load baseline")
        print("4. Check file")
        print("5. Check all files")
        print("6. Exit")
        
        choice = input("\nChoose (1-6): ").strip()
        
        if choice == '1':
            filepath = input("File path: ").strip()
            if os.path.exists(filepath):
                monitor.create_baseline(filepath)
            else:
                print("❌ File not found!\n")
        
        elif choice == '2':
            monitor.save_baseline()
        
        elif choice == '3':
            monitor.load_baseline()
        
        elif choice == '4':
            filepath = input("File path: ").strip()
            result = monitor.check_file(filepath)
            if result:
                print(f"\n{result['message']}\n")
        
        elif choice == '5':
            monitor.check_all_files()
        
        elif choice == '6':
            print("\nStay safe! 🔐\n")
            break
        
        else:
            print("❌ Invalid choice!\n")

if __name__ == "__main__":
    main()