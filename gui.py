
import tkinter as tk
import psutil
import requests

def refresh():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("C:\\").percent

    cpu_label.config(text=f"CPU Usage: {cpu}%")
    memory_label.config(text=f"Memory Usage: {memory}%")
    disk_label.config(text=f"Disk Usage: {disk}%")


def check_website():
    try:
        requests.get("https://www.google.com", timeout=5)
        website_label.config(text="Google: Website is UP")
    except requests.RequestException:
        website_label.config(text="Google: Website is DOWN")


root = tk.Tk()
root.title("IT Infrastructure Health Monitor")
root.geometry("400x350")

title = tk.Label(root, text="IT Infrastructure Health Monitor")
title.pack(pady=15)

cpu_label = tk.Label(root, text="CPU Usage: --")
cpu_label.pack(pady=5)

memory_label = tk.Label(root, text="Memory Usage: --")
memory_label.pack(pady=5)

disk_label = tk.Label(root, text="Disk Usage: --")
disk_label.pack(pady=5)

website_label = tk.Label(root, text="Website: Not checked")
website_label.pack(pady=10)

refresh_button = tk.Button(
    root, text="Refresh System Data", command=refresh
)
refresh_button.pack(pady=5)

website_button = tk.Button(
    root, text="Check Website", command=check_website
)
website_button.pack(pady=5)

root.mainloop()
