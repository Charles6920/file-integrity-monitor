# File Integrity Monitor

A Python security tool that detects unauthorized file modifications.

## What It Does

✅ **Create Baseline** - Take a snapshot of your files
✅ **Monitor Files** - Check for any changes
✅ **Detect Modifications** - Alert when files change
✅ **Log Changes** - Record all modifications

## How It Works

1. Program calculates a unique "fingerprint" (SHA256 hash) of your files
2. Saves that fingerprint in `baseline.json`
3. Later, it calculates the fingerprint again
4. If fingerprints match = File is safe ✅
5. If different = File was modified! ⚠️

## Installation

```bash
python file_monitor.py
```

## How to Use
1.Create baseline for your file
2.Save baseline
3.Load baseline
4.Check files regularly
5.Get alerts if anything changes

## Example
Choose: 1
File path: myfile.txt
✅ Baseline created: myfile.txt
Choose: 2
✅ Baseline saved
Choose: 5
✅ myfile.txt - No changes
[Someone modifies myfile.txt]
Choose: 5
⚠️ myfile.txt - MODIFIED!

## Security Concepts

- SHA256 Hashing
- File Integrity Verification
- Change Detection
- Baseline Comparison

## Technologies Used

- Python 3
- Hashlib (for hashing)
- JSON (for storage)

## Author

Charles Alliu - SIWES Student

## License

MIT
