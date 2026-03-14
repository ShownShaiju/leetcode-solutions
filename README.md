# LeetCode Practice

This repository contains Python solutions for LeetCode problems, organized by topic folders.

## Folder Structure

- `arrays/242_valid_anagram.py` - Solution for LeetCode **242. Valid Anagram**

## Current Problem Included

### 242. Valid Anagram

- **Difficulty:** Easy
- **Topic:** HashMap / Frequency Counting
- **LeetCode Link:** https://leetcode.com/problems/valid-anagram/
- **Approach Used:** `collections.Counter` comparison

## Prerequisites

- Python 3.8 or newer installed

Check your Python version:

```bash
python --version
```

## How to Run the Code Locally

The file is written in LeetCode class format (`class Solution`) and does not print output by default.

### Option 1: Quick local test in terminal

Run this command from the repository root:

```bash
python -c "import importlib.util; spec=importlib.util.spec_from_file_location('sol','arrays/242_valid_anagram.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); s=m.Solution(); print(s.isAnagram('anagram','nagaram')); print(s.isAnagram('rat','car'))"
```

Expected output:

```text
True
False
```

### Option 2: Run inside LeetCode

1. Open the problem page: https://leetcode.com/problems/valid-anagram/
2. Copy the `Solution` class from `arrays/242_valid_anagram.py`
3. Paste into LeetCode editor and run/submit

## Time and Space Complexity

For the current solution using `Counter`:

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

Where `n` is the length of the strings.

## Notes

- File names follow this pattern: `<problem_number>_<problem_name>.py`
- As you add more files, update this README with a short index of solved problems.

## License

This project is licensed under the MIT License.
See the `LICENSE` file for full details.
