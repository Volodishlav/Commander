# Commander 

A simple Python-based command execution tool designed to repeatedly run shell commands with configurable behavior.

---

### Features

- Execute any shell command in a loop (you can also run multiple commands in order)
- Configurable delay between executions (TTR - Time To Repeat)
- “Slayer Mode” for continuous execution without delay
- Custom working directory
- Scheduled execution by time
- Lightweight and minimal dependencies  

---

### Configuration

```python
# You can edit this line (checks the current time every 1 second):
time.sleep(1)
```

### Usage

```bash
python3 Commander.py
```
