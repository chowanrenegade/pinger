import platform
import subprocess
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext
import urllib.parse


class PingApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Website Ping Tool")
    self.root.geometry("550x450")

    # Input Frame
    input_frame = tk.Frame(root, padx=10, pady=10)
    input_frame.pack(fill=tk.X)

    self.label = tk.Label(
        input_frame, text="Enter Website or IP (e.g., https://google.com):"
    )
    self.label.pack(anchor="w", pady=(0, 5))

    self.entry = tk.Entry(input_frame, width=45, font=("Arial", 10))
    self.entry.pack(side=tk.LEFT, padx=(0, 10), pady=5)
    self.entry.insert(0, "https://www.google.com")
    # Bind Enter key to trigger ping
    self.entry.bind("<Return>", lambda event: self.start_ping_thread())

    self.ping_button = tk.Button(
        input_frame,
        text="Ping",
        command=self.start_ping_thread,
        width=10,
        bg="#007ACC",
        fg="white",
    )
    self.ping_button.pack(side=tk.LEFT, pady=5)

    # Output Area
    output_frame = tk.Frame(root, padx=10, pady=5)
    output_frame.pack(fill=tk.BOTH, expand=True)

    self.text_area = scrolledtext.ScrolledText(
        output_frame,
        wrap=tk.WORD,
        state="disabled",
        bg="#1e1e1e",
        fg="#d4d4d4",
        font=("Consolas", 10),
    )
    self.text_area.pack(fill=tk.BOTH, expand=True)

  def clean_url(self, raw_input):
    """Strips https://, http://, and trailing paths from the input."""
    raw_input = raw_input.strip()
    if "://" not in raw_input:
      raw_input = "//" + raw_input
    parsed = urllib.parse.urlparse(raw_input)
    host = parsed.netloc if parsed.netloc else parsed.path
    return host.split("/")[0]

  def start_ping_thread(self):
    raw_target = self.entry.get()
    if not raw_target:
      messagebox.showerror("Error", "Please enter a website or IP address.")
      return

    target = self.clean_url(raw_target)

    # Disable button and clear text area during ping
    self.ping_button.config(state="disabled")
    self.text_area.config(state="normal")
    self.text_area.delete(1.0, tk.END)
    self.text_area.insert(tk.END, f"Pinging {target}...\n\n")
    self.text_area.config(state="disabled")

    # Run in a separate thread to prevent the GUI from freezing
    threading.Thread(target=self.run_ping, args=(target,), daemon=True).start()

  def run_ping(self, target):
    # Determine the correct flag based on OS (Windows uses -n, Linux/macOS use -c)
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "4", target]

    try:
      process = subprocess.Popen(
          command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
      )
      stdout, stderr = process.communicate()
      output = stdout if stdout else stderr
      self.root.after(0, self.update_output, output)
    except Exception as e:
      self.root.after(0, self.update_output, f"An error occurred: {e}")

  def update_output(self, result):
    self.text_area.config(state="normal")
    self.text_area.insert(tk.END, result)
    self.text_area.config(state="disabled")
    self.ping_button.config(state="normal")


if __name__ == "__main__":
  root = tk.Tk()
  app = PingApp(root)
  root.mainloop()