# Import the tkinter library for creating GUI applications.
import tkinter as tk
from tkinter import messagebox

# Create a class for the Contact Book application.
class ContactBookApp:
    # Initialize the application with the main root window.
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Initialize an empty list to store contacts and set the selected contact index to None.
        self.contacts = []
        self.selected_contact_index = None

        # Create labels and entry fields for name and phone.
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.pack()

        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        # Create a button to add a new contact.
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        # Create a listbox to display the list of contacts.
        self.contacts_listbox = tk.Listbox(root)
        self.contacts_listbox.pack()

        # Create buttons for updating and deleting contacts.
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()

        # Load existing contacts when the application starts.
        self.load_contacts()

    # Function to load contacts into the listbox.
    def load_contacts(self):
        self.contacts_listbox.delete(0, tk.END)  # Clear the listbox.
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, contact['name'])  # Insert contact names.

    # Function to add a new contact to the list.
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            contact = {'name': name, 'phone': phone}
            self.contacts.append(contact)
            self.load_contacts()  # Update the listbox.
            self.name_entry.delete(0, tk.END)  # Clear the name entry.
            self.phone_entry.delete(0, tk.END)  # Clear the phone entry.
        else:
            messagebox.showwarning("Warning", "Name and Phone are required.")

    # Function to update an existing contact.
    def update_contact(self):
        if self.selected_contact_index is not None:
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            if name and phone:
                # Update the selected contact's information.
                self.contacts[self.selected_contact_index]['name'] = name
                self.contacts[self.selected_contact_index]['phone'] = phone
                self.load_contacts()  # Update the listbox.
                self.name_entry.delete(0, tk.END)  # Clear the name entry.
                self.phone_entry.delete(0, tk.END)  # Clear the phone entry.
                self.selected_contact_index = None  # Clear the selected index.
            else:
                messagebox.showwarning("Warning", "Name and Phone are required.")
        else:
            messagebox.showwarning("Warning", "Select a contact to update.")

    # Function to delete a selected contact.
    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]  # Delete the selected contact.
            self.load_contacts()  # Update the listbox.
            self.name_entry.delete(0, tk.END)  # Clear the name entry.
            self.phone_entry.delete(0, tk.END)  # Clear the phone entry.

    # Function to handle contact selection from the listbox.
    def on_contact_selected(self, event):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.selected_contact_index = index
            contact = self.contacts[index]
            # Display the selected contact's information in the entry fields.
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.name_entry.insert(0, contact['name'])
            self.phone_entry.insert(0, contact['phone'])

# Entry point of the program.
if __name__ == "__main__":
    root = tk.Tk()  # Create the main root window.
    app = ContactBookApp(root)  # Create an instance of the ContactBookApp class.
    app.contacts_listbox.bind("<<ListboxSelect>>", app.on_contact_selected)  # Bind selection event.
    root.mainloop()  # Start the GUI event loop.
