import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Progressbar


def filter_passwords(file_content):

    def is_valid_password(password):
        return (
            8 <= len(password) <= 16 and
            any(char.isupper() for char in password) and
            any(char.islower() for char in password) and
            any(char.isdigit() for char in password) and
            any(char in '#!*%-_=' for char in password) and
            not any(char in 'üÆñßØ ' for char in password)
        )

    passwords = file_content.split('\n')
    filtered_passwords = [password for password in passwords if is_valid_password(password)]
    return '\n'.join(filtered_passwords)

def handle_file_upload():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                filtered_content = filter_passwords(file_content)
                result_text.delete('1.0', tk.END)
                result_text.insert(tk.END, filtered_content)
                update_progress()  # Update progress to 100%
        except UnicodeDecodeError as e:
            messagebox.showerror("Error", f"Failed to read the file: {str(e)}")

def handle_download():
    filtered_content = result_text.get('1.0', tk.END)
    if filtered_content.strip():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(filtered_content)
            except UnicodeEncodeError as e:
                messagebox.showerror("Error", f"Failed to write the file: {str(e)}")
    else:
        messagebox.showinfo("Information", "No filtered passwords to download.")

def update_progress(current_progress=0):
    progress_var.set(current_progress)
    if current_progress < 100:
        current_progress += 1
        root.after(50, update_progress, current_progress)  # Delayed update

root = tk.Tk()
root.title("Password Filter")

# Create a frame with a subtle gray background
frame = tk.Frame(root, bg="#F0F0F0")
frame.pack(fill=tk.BOTH, expand=True)

# Create a style for buttons
style = tk.ttk.Style()
style.configure('TButton', foreground='#FFF', background='#007bff', font=('Helvetica', 12))

# Create and configure a progressbar
progress_var = tk.DoubleVar()
progress_bar = Progressbar(frame, variable=progress_var, maximum=100, mode='determinate')
progress_var.set(0)
progress_bar.pack(fill=tk.X, padx=10, pady=10)

# Create and style buttons
file_button = tk.Button(frame, text="Upload File", command=handle_file_upload)
download_button = tk.Button(frame, text="Download Filtered Passwords", command=handle_download)
file_button.pack(pady=10)
download_button.pack(pady=10)

# Create and configure a text widget for the result
result_text = tk.Text(frame, wrap=tk.WORD, height=10, width=40, font=('Helvetica', 12))
result_text.pack(padx=10, pady=10)

root.mainloop()
