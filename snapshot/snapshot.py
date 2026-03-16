"""
Make snapshot

{"Tasks": {"total": 440, "running": 1, "sleeping": 354, "stopped": 1, "zombie": 0},
"%CPU": {"user": 14.4, "system": 2.2, "idle": 82.7},
"KiB Mem": {"total": 16280636, "free": 335140, "used": 11621308},
"KiB Swap": {"total": 16280636, "free": 335140, "used": 11621308},
"Timestamp": 1624400255}
"""
import argparse
import psutil
import time
import json
import subprocess
import pprint


def main():
    """Snapshot tool."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Interval between snapshots in seconds", type=int, default=5)
    parser.add_argument("-f", help="Output file name", default="snapshot.json")
    parser.add_argument("-n", help="Quantity of snapshot to output", type=int, default=20)
    args = parser.parse_args()
    interval = args.i
    file_name = args.f
    snapshot_n = args.n

    for _ in range(snapshot_n):
        tasks = count_tasks()
        cpu_st = cpuStats(psutil.cpu_times())
        mem_st = memory_stats()
        sw_mem_st = swap_memory_stats()
        time_stamp = int(time.time())
        snapshot = {"Tasks": tasks,
                    "%CPU": cpu_st.out(),
                    "KiB Mem": mem_st,
                    "KiB Swap": sw_mem_st,
                    "Timestamp": time_stamp}

        with open(file_name, 'a') as f:
            json.dump(snapshot, f, indent=2)
            f.write('\n')
            f.write('\n')

        subprocess.run(['clear'])
        pprint.pprint(snapshot, width=120, sort_dicts=False)
        time.sleep(interval)


def count_tasks():
    running = 0
    sleeping = 0
    stopped = 0
    zombie = 0

    for proc in psutil.process_iter(['status']):
        match proc.info['status']:
            case "running":
                running += 1
            case "sleeping":
                sleeping += 1
            case "stopped":
                stopped += 1
            case "zombie":
                zombie += 1

    total = running + sleeping + stopped + zombie
    procs = {"total": total, "running": running, "sleeping": sleeping, "stopped": stopped,
             "zombie": zombie}
    return procs


class cpuStats:
    def __init__(self, cpu):
        self.user = cpu.user
        self.system = cpu.system
        self.idle = cpu.idle

    def out(self):
        cpu_out = {"user": self.user, "system": self.system, "idle": self.idle}
        return cpu_out


def cpu_stats():
    cpu_t = psutil.cpu_times()
    user = cpu_t.user
    system = cpu_t.system
    idle = cpu_t.idle
    cpu_stat_out = {"user": user, "system": system, "idle": idle}
    return cpu_stat_out


def memory_stats():
    mem_st = psutil.virtual_memory()
    total = mem_st.total
    free = mem_st.free
    used = mem_st.used
    mem_st_out = {"total": total, "free": free, "used": used}
    return mem_st_out


def swap_memory_stats():
    sw_mem_st = psutil.swap_memory()
    total = sw_mem_st.total
    free = sw_mem_st.free
    used = sw_mem_st.used
    sw_mem_out = {"total": total, "free": free, "used": used}
    return sw_mem_out


if __name__ == "__main__":
    main()
