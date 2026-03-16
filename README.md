# snapshot

A CLI tool for periodic system snapshots: tracks tasks, CPU, memory, and swap, logging each to a JSON file.

## Installation

```bash
git clone git@github.com:lukantozi/snapshot-tool.git
python -m venv .venv
source .venv/bin/activate
cd snapshot-tool
pip install -U ./snapshot-tool
```

## Usage

```bash
snapshot [-i INTERVAL] [-f FILE] [-n COUNT]
```

| Flag | Description | Default |
|------|-------------|---------|
| `-i` | Interval between snapshots (seconds) | `5` |
| `-f` | Output file name | `snapshot.json` |
| `-n` | Number of snapshots to take | `20` |

## Output

Each snapshot is appended to the output file as a JSON object:

```json
{
  "Tasks": { "total": 440, "running": 1, "sleeping": 354, "stopped": 1, "zombie": 0 },
  "%CPU": { "user": 14.4, "system": 2.2, "idle": 82.7 },
  "KiB Mem": { "total": 16280636, "free": 335140, "used": 11621308 },
  "KiB Swap": { "total": 16280636, "free": 335140, "used": 11621308 },
  "Timestamp": 1624400255
}
```

## Requirements

- `psutil==7.2.2`
- `packaging==26.0`
- `setuptools==82.0.1`
