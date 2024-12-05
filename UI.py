import tkinter as tk
from tkinter import filedialog, messagebox
import os
import create
import push


class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SQL and MCD Interface")
        self.root.geometry("800x600")
        
        # Section Create
        self.create_section = tk.LabelFrame(self.root, text="Create Section", padx=10, pady=10)
        self.create_section.pack(fill="both", expand="yes", padx=20, pady=10)

        self.filename_label = tk.Label(self.create_section, text="Filename:")
        self.filename_label.grid(row=0, column=0, padx=5, pady=5)

        self.filename_entry = tk.Entry(self.create_section, width=40)
        self.filename_entry.grid(row=0, column=1, padx=5, pady=5)

        self.action_label = tk.Label(self.create_section, text="Choose Action:")
        self.action_label.grid(row=1, column=0, padx=5, pady=5)

        self.action_dropdown = tk.StringVar(self.create_section)
        self.action_dropdown.set("input_to_sql")  # Default value
        self.action_menu = tk.OptionMenu(self.create_section, self.action_dropdown, "input_to_sql", "input_to_mcd")
        self.action_menu.grid(row=1, column=1, padx=5, pady=5)

        self.execute_button = tk.Button(self.create_section, text="Execute Create Action", command=self.execute_create_action)
        self.execute_button.grid(row=2, columnspan=2, padx=5, pady=5)

        # Section Push
        self.push_section = tk.LabelFrame(self.root, text="Push Section", padx=10, pady=10)
        self.push_section.pack(fill="both", expand="yes", padx=20, pady=10)

        self.push_filename_label = tk.Label(self.push_section, text="Push Filename (Full Path):")
        self.push_filename_label.grid(row=0, column=0, padx=5, pady=5)

        self.push_filename_entry = tk.Entry(self.push_section, width=40)
        self.push_filename_entry.grid(row=0, column=1, padx=5, pady=5)

        # Add Browse button
        self.browse_button = tk.Button(self.push_section, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=5, pady=5)

        self.push_action_label = tk.Label(self.push_section, text="Choose Push Action:")
        self.push_action_label.grid(row=1, column=0, padx=5, pady=5)

        self.push_action_dropdown = tk.StringVar(self.push_section)
        self.push_action_dropdown.set("afficher")  # Default value
        self.push_action_menu = tk.OptionMenu(self.push_section, self.push_action_dropdown, "afficher", "sqlite_exec")
        self.push_action_menu.grid(row=1, column=1, padx=5, pady=5)

        self.push_execute_button = tk.Button(self.push_section, text="Execute Push Action", command=self.execute_push_action)
        self.push_execute_button.grid(row=2, columnspan=2, padx=5, pady=5)

        # Terminal (Interactive container)
        self.terminal_section = tk.LabelFrame(self.root, text="Terminal", padx=10, pady=10)
        self.terminal_section.pack(fill="both", expand="yes", padx=20, pady=10)

        # Text widget to display terminal output
        self.terminal_text = tk.Text(self.terminal_section, height=15, width=70, wrap="word", state=tk.DISABLED)
        self.terminal_text.grid(row=0, column=0, padx=5, pady=5)

        # Entry for typing commands
        self.terminal_input = tk.Entry(self.terminal_section, width=70)
        self.terminal_input.grid(row=1, column=0, padx=5, pady=5)

        # Submit button to process terminal commands
        self.terminal_input_button = tk.Button(self.terminal_section, text="Submit Command", command=self.submit_command)
        self.terminal_input_button.grid(row=2, column=0, padx=5, pady=5)

    def write_to_terminal(self, text):
        """Write text to the terminal (Text widget)."""
        self.terminal_text.config(state=tk.NORMAL)
        self.terminal_text.insert(tk.END, text + '\n')
        self.terminal_text.config(state=tk.DISABLED)
        self.terminal_text.yview(tk.END)

    def submit_command(self):
        """Submit the command entered by the user and execute it."""
        command = self.terminal_input.get()
        if command.strip():
            self.write_to_terminal(f"> {command}")  # Show the command in the terminal
            self.terminal_input.delete(0, tk.END)  # Clear the input field

            if command == "help":
                self.write_to_terminal("Commands available: help, execute create, execute push.")
            elif command == "execute create":
                self.execute_create_action()
            elif command == "execute push":
                self.execute_push_action()
            else:
                self.write_to_terminal(f"Command '{command}' not recognized.")
        else:
            self.write_to_terminal("Please enter a valid command.")

    def execute_create_action(self):
        filename = self.filename_entry.get()
        action = self.action_dropdown.get()

        if not filename:
            self.write_to_terminal("Filename cannot be empty!")
            return
        
        create_instance = create.textinput(filename)

        if action == "input_to_sql":
            self.write_to_terminal("Executing 'input_to_sql'...")
            create_instance.input_to_sql()
            self.write_to_terminal(f"SQL file '{filename}.sql' created successfully!")
        elif action == "input_to_mcd":
            self.write_to_terminal("Executing 'input_to_mcd'...")
            create_instance.input_to_mcd()
            self.write_to_terminal(f"MCD file '{filename}.mcd' created successfully!")

    def execute_push_action(self):
        filename = self.push_filename_entry.get()
        action = self.push_action_dropdown.get()

        if not filename:
            self.write_to_terminal("Filename cannot be empty!")
            return

        if not os.path.exists(filename):
            self.write_to_terminal(f"Error: The file '{filename}' does not exist!")
            return
        
        push_instance = push.exect(filename)

        if action == "afficher":
            self.write_to_terminal("Executing 'afficher'...")
            push_instance.afficher()
            self.write_to_terminal(f"Executed the SQL from '{filename}' and displayed results.")
        elif action == "sqlite_exec":
            self.write_to_terminal("Executing 'sqlite_exec'...")
            push_instance.sqlite_exec()
            self.write_to_terminal(f"Executed the SQL from '{filename}' in memory.")

    def browse_file(self):
        """Open a file dialog to select a file."""
        file_path = filedialog.askopenfilename(filetypes=[("SQL Files", "*.sql"), ("All Files", "*.*")])
        if file_path:
            self.push_filename_entry.delete(0, tk.END)
            self.push_filename_entry.insert(0, file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()
