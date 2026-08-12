import platform
import psutil


def get_system_info():
    print("\n===== System Information =====")

    print("\nOperating System")
    print("----------------")
    print("System:", platform.system())
    print("Release:", platform.release())
    print("Version:", platform.version())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())

    print("\nCPU Information")
    print("----------------")
    print("CPU Cores:", psutil.cpu_count(logical=False))
    print("Logical CPUs:", psutil.cpu_count(logical=True))
    print("CPU Usage:", psutil.cpu_percent(interval=1), "%")

    memory = psutil.virtual_memory()

    print("\nMemory Information")
    print("------------------")
    print("Total:", round(memory.total / (1024 ** 3), 2), "GB")
    print("Used:", round(memory.used / (1024 ** 3), 2), "GB")
    print("Available:", round(memory.available / (1024 ** 3), 2), "GB")
    print("Usage:", memory.percent, "%")

    disk = psutil.disk_usage("/")

    print("\nDisk Information")
    print("----------------")
    print("Total:", round(disk.total / (1024 ** 3), 2), "GB")
    print("Used:", round(disk.used / (1024 ** 3), 2), "GB")
    print("Free:", round(disk.free / (1024 ** 3), 2), "GB")
    print("Usage:", disk.percent, "%")


get_system_info()
