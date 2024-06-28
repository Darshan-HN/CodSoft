import tkinter as tk
from tkinter import messagebox

# Dummy initial data (for testing)
contacts = [
    {"name": "John Doe", "phone": "1234567890", "email": "john.doe@example.com", "address": "123 Main St"},
    {"name": "Jane Smith", "phone": "9876543210", "email": "jane.smith@example.com", "address": "456 Elm St"}
]

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name == "":
        messagebox.showerror("Error", "Name field cannot be empty.")
        return
    
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    
    # Clear input fields
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    
    messagebox.showinfo("Success", "Contact added successfully.")

# Function to view all contacts
def view_contacts():
    contacts_listbox.delete(0, tk.END)  # Clear previous entries
    
    for contact in contacts:
        contacts_listbox.insert(tk.END, f"{contact['name']}: {contact['phone']}")

# Function to search for a contact
def search_contact():
    query = search_entry.get().strip().lower()
    
    if query == "":
        messagebox.showerror("Error", "Please enter a search query.")
        return
    
    results_listbox.delete(0, tk.END)  # Clear previous search results
    
    found = False
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            results_listbox.insert(tk.END, f"{contact['name']}: {contact['phone']}")
            found = True
    
    if not found:
        results_listbox.insert(tk.END, "No matching contacts found.")

# Function to update a contact
def update_contact():
    selected_contact = contacts_listbox.curselection()
    
    if not selected_contact:
        messagebox.showerror("Error", "Please select a contact to update.")
        return
    
    index = selected_contact[0]
    name = contacts[index]['name']
    
    new_phone = phone_update_entry.get()
    new_email = email_update_entry.get()
    new_address = address_update_entry.get()
    
    contacts[index]['phone'] = new_phone
    contacts[index]['email'] = new_email
    contacts[index]['address'] = new_address
    
    messagebox.showinfo("Success", f"Contact '{name}' updated successfully.")
    update_window.destroy()  # Close the update window after updating
    view_contacts()  # Refresh the contacts list after update

# Function to delete a contact
def delete_contact():
    selected_contact = contacts_listbox.curselection()
    
    if not selected_contact:
        messagebox.showerror("Error", "Please select a contact to delete.")
        return
    
    index = selected_contact[0]
    name = contacts[index]['name']
    
    del contacts[index]
    
    messagebox.showinfo("Success", f"Contact '{name}' deleted successfully.")
    view_contacts()  # Refresh the contacts list after deletion

# Function to open update contact window
def open_update_window():
    selected_contact = contacts_listbox.curselection()
    
    if not selected_contact:
        messagebox.showerror("Error", "Please select a contact to update.")
        return
    
    global update_window
    update_window = tk.Toplevel(root)
    update_window.title("Update Contact")
    
    index = selected_contact[0]
    name_label = tk.Label(update_window, text=f"Name: {contacts[index]['name']}")
    name_label.pack()
    
    tk.Label(update_window, text="Phone Number:").pack()
    global phone_update_entry
    phone_update_entry = tk.Entry(update_window)
    phone_update_entry.pack()
    phone_update_entry.insert(0, contacts[index]['phone'])
    
    tk.Label(update_window, text="Email:").pack()
    global email_update_entry
    email_update_entry = tk.Entry(update_window)
    email_update_entry.pack()
    email_update_entry.insert(0, contacts[index]['email'])
    
    tk.Label(update_window, text="Address:").pack()
    global address_update_entry
    address_update_entry = tk.Entry(update_window)
    address_update_entry.pack()
    address_update_entry.insert(0, contacts[index]['address'])
    
    tk.Button(update_window, text="Update Contact", command=update_contact).pack()

# Main Tkinter window
root = tk.Tk()
root.title("Contact Management System")

# Labels and Entry widgets for adding contacts
tk.Label(root, text="Name:").grid(row=0, column=0, sticky='e')
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone Number:").grid(row=1, column=0, sticky='e')
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

tk.Label(root, text="Email:").grid(row=2, column=0, sticky='e')
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

tk.Label(root, text="Address:").grid(row=3, column=0, sticky='e')
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)

# Buttons for adding contacts
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=1, pady=10)

# View Contacts button and listbox
view_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_button.grid(row=5, column=1, pady=10)

contacts_listbox = tk.Listbox(root, width=40)
contacts_listbox.grid(row=6, column=1, padx=10)

# Search Contacts
tk.Label(root, text="Search:").grid(row=7, column=0, sticky='e')
search_entry = tk.Entry(root)
search_entry.grid(row=7, column=1)

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.grid(row=7, column=2, padx=10)

results_listbox = tk.Listbox(root, width=40)
results_listbox.grid(row=8, column=1, padx=10, pady=10)

# Update and Delete Contacts buttons
update_button = tk.Button(root, text="Update Contact", command=open_update_window)
update_button.grid(row=9, column=1, pady=10)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=10, column=1, pady=10)

root.mainloop()
