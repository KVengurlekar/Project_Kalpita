import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import os

# Server URL
SERVER_URL = "http://your-server-url.com"

class FileSharingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Sharing App")

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.grid(row=0, column=0, sticky="e")
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.grid(row=1, column=0, sticky="e")
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2, pady=10)

        # File management
        self.upload_button = tk.Button(self.root, text="Upload File", command=self.upload_file, state=tk.DISABLED)
        self.upload_button.grid(row=3, column=0, pady=10)
        self.download_button = tk.Button(self.root, text="Download File", command=self.download_file, state=tk.DISABLED)
        self.download_button.grid(row=3, column=1, pady=10)

    def login(self):
        # Dummy authentication for demonstration
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Perform authentication (replace with your authentication mechanism)
        if username == "admin" and password == "admin":
            self.show_file_management()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show_file_management(self):
        # Enable file management buttons
        self.upload_button.config(state=tk.NORMAL)
        self.download_button.config(state=tk.NORMAL)

    def upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            file_name = os.path.basename(file_path)
            with open(file_path, "rb") as file:
                files = {"file": (file_name, file)}
                response = requests.post(f"{SERVER_URL}/upload", files=files)
                if response.status_code == 200:
                    messagebox.showinfo("Upload Successful", "File uploaded successfully")
                else:
                    messagebox.showerror("Upload Failed", "Failed to upload file")

    def download_file(self):
        # Dummy download function
        # In a real application, you would request the file from the server
        response = requests.get(f"{SERVER_URL}/download")
        if response.status_code == 200:
            save_path = filedialog.asksaveasfilename(defaultextension=".txt")
            if save_path:
                with open(save_path, "wb") as file:
                    file.write(response.content)
                messagebox.showinfo("Download Successful", "File downloaded successfully")
        else:
            messagebox.showerror("Download Failed", "Failed to download file")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileSharingApp(root)
    root.mainloop()
