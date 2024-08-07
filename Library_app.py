import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from fpdf import FPDF  

import cx_Oracle

# Define connection object
conn = cx_Oracle.connect('C##Mohammed/Moh2004@localhost:1521/orcl')

# Function to fetch members
def fetch_members():
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Member")
        return cursor.fetchall()
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to fetch members: " + str(error))
    finally:
        cursor.close()
        
def fetch_authors():
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Author")
        return cursor.fetchall()
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to fetch authors: " + str(error))
    finally:
        cursor.close()

def fetch_genres():
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Genre ORDER BY genre_id")
        return cursor.fetchall()
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to fetch genres: " + str(error))
        return []
    finally:
        cursor.close()
        
def fetch_libraries():
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Library")
        return cursor.fetchall()
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to fetch libraries: " + str(error))
        return []
    finally:
        cursor.close()

def fetch_books():
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Book")
        return cursor.fetchall()
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to fetch books: " + str(error))
        return []
    finally:
        cursor.close()
        
def fetch_borrowings():
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Borrowing")
        return cursor.fetchall()
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to fetch borrowing: " + str(error))
        return []
    finally:
        cursor.close()

# Function to insert member
def insert_member(name, address, phone):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Member (member_id, name, address, phone) VALUES (member_id_sq.NEXTVAL, :1, :2, :3)", (name, address, phone))
        conn.commit()
        messagebox.showinfo("Success", "Member inserted successfully!")
    except cx_Oracle.IntegrityError as e:
        if e.args[0].code == 1:
            messagebox.showerror("Error", "Failed to insert member: Member already exists.")
        else:
            messagebox.showerror("Error", "Failed to insert member: " + str(e))
    finally:
        cursor.close()

# Function to delete member
def delete_member(member_id):
    cursor = conn.cursor()
    try:
        # Check if member_id is provided
        if not member_id:
            raise ValueError("Member ID is required.")
        
        # Check if member exists
        cursor.execute("SELECT COUNT(*) FROM Member WHERE member_id = :1", (member_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            messagebox.showerror("Error", "Member with ID {} does not exist.".format(member_id))
            return
        
        # Delete member
        cursor.execute("DELETE FROM Member WHERE member_id = :1", (member_id,))
        conn.commit()
        messagebox.showinfo("Success", "Member deleted successfully!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to delete member: " + str(error))
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    finally:
        cursor.close()

# Function to update member
def update_member(member_id, name, address, phone):
    cursor = conn.cursor()
    try:
        # Check if member ID is provided
        if not member_id:
            raise ValueError("Member ID is required.")
        
        # Check if member exists
        cursor.execute("SELECT COUNT(*) FROM Member WHERE member_id = :1", (member_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            messagebox.showerror("Error", "Member with ID {} does not exist.".format(member_id))
            return
        
        # Update member details
        cursor.execute("UPDATE Member SET name = :1, address = :2, phone = :3 WHERE member_id = :4", (name, address, phone, member_id))
        conn.commit()
        messagebox.showinfo("Success", "Member updated successfully!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to update member: " + str(error))
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    finally:
        cursor.close()
        
# Function to insert author
def insert_author(name, biography):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Author (author_id, name, biography) VALUES (author_id_sq.NEXTVAL, :1, :2)", (name, biography))
        conn.commit()
        messagebox.showinfo("Success", "Author inserted successfully!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to insert author: " + str(error))
    finally:
        cursor.close()

# Function to delete author
def delete_author(author_id):
    cursor = conn.cursor()
    try:
        # Check if author ID is provided
        if not author_id:
            raise ValueError("Author ID is required.")
        
        # Check if author exists
        cursor.execute("SELECT COUNT(*) FROM Author WHERE author_id = :1", (author_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            messagebox.showerror("Error", "Author with ID {} does not exist.".format(author_id))
            return
        
        # Delete author
        cursor.execute("DELETE FROM Author WHERE author_id = :1", (author_id,))
        conn.commit()
        messagebox.showinfo("Success", "Author deleted successfully!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to delete author: " + str(error))
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    finally:
        cursor.close()

# Function to update author
def update_author(author_id, name, biography):
    cursor = conn.cursor()
    try:
        # Check if author ID is provided
        if not author_id:
            raise ValueError("Author ID is required.")
        
        # Check if author exists
        cursor.execute("SELECT COUNT(*) FROM Author WHERE author_id = :1", (author_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            messagebox.showerror("Error", "Author with ID {} does not exist.".format(author_id))
            return
        
        # Update author details
        cursor.execute("UPDATE Author SET name = :1, biography = :2 WHERE author_id = :3", (name, biography, author_id))
        conn.commit()
        messagebox.showinfo("Success", "Author updated successfully!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to update author: " + str(error))
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    finally:
        cursor.close()
        
def insert_genre(genre_name):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Genre (genre_id, genre_name) VALUES (genre_id_sq.NEXTVAL, :1)", (genre_name,))
        conn.commit()
        messagebox.showinfo("Success", "Genre inserted successfully!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to insert genre: " + str(error))
    finally:
        cursor.close()

# Function to delete genre
def delete_genre(genre_id):
    cursor = conn.cursor()
    try:
        # Check if genre ID is provided
        if not genre_id:
            raise ValueError("Genre ID is required.")
        
        # Check if genre exists
        cursor.execute("SELECT COUNT(*) FROM Genre WHERE genre_id = :1", (genre_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            messagebox.showerror("Error", "Genre with ID {} does not exist.".format(genre_id))
            return
        
        # Delete genre
        cursor.execute("DELETE FROM Genre WHERE genre_id = :1", (genre_id,))
        conn.commit()
        messagebox.showinfo("Success", "Genre deleted successfully!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to delete genre: " + str(error))
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    finally:
        cursor.close()

# Function to update genre
def update_genre(genre_id, genre_name):
    cursor = conn.cursor()
    try:
        # Check if genre ID is provided
        if not genre_id:
            raise ValueError("Genre ID is required.")
        
        # Check if genre exists
        cursor.execute("SELECT COUNT(*) FROM Genre WHERE genre_id = :1", (genre_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            messagebox.showerror("Error", "Genre with ID {} does not exist.".format(genre_id))
            return
        
        # Update genre name
        cursor.execute("UPDATE Genre SET genre_name = :1 WHERE genre_id = :2", (genre_name, genre_id))
        conn.commit()
        messagebox.showinfo("Success", "Genre updated successfully!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to update genre: " + str(error))
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    finally:
        cursor.close()
        
def insert_library(phone, address):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Library (library_id, phone, address) VALUES (library_id_sq.NEXTVAL, :1, :2)", (phone, address))
        conn.commit()
        messagebox.showinfo("Success", "Library inserted successfully!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to insert library: " + str(error))
    finally:
        cursor.close()

# Function to delete library
def delete_library(library_id):
    cursor = conn.cursor()
    try:
        # Check if library ID is provided
        if not library_id:
            raise ValueError("Library ID is required.")
        
        # Check if library exists
        cursor.execute("SELECT COUNT(*) FROM Library WHERE library_id = :1", (library_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            messagebox.showerror("Error", "Library with ID {} does not exist.".format(library_id))
            return
        
        # Delete library
        cursor.execute("DELETE FROM Library WHERE library_id = :1", (library_id,))
        conn.commit()
        messagebox.showinfo("Success", "Library deleted successfully!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to delete library: " + str(error))
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    finally:
        cursor.close()


# Function to update library
def update_library(library_id, phone, address):
    cursor = conn.cursor()
    try:
        # Check if library ID is provided
        if not library_id:
            raise ValueError("Library ID is required.")
        
        # Check if library exists
        cursor.execute("SELECT COUNT(*) FROM Library WHERE library_id = :1", (library_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            messagebox.showerror("Error", "Library with ID {} does not exist.".format(library_id))
            return
        
        # Update library details
        cursor.execute("UPDATE Library SET phone = :1, address = :2 WHERE library_id = :3", (phone, address, library_id))
        conn.commit()
        messagebox.showinfo("Success", "Library updated successfully!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to update library: " + str(error))
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    finally:
        cursor.close()
        
# Function to insert book
def insert_book(isbn, title, genre_id):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Book (isbn, book_id, title, genre_id) VALUES (:1, book_id_sq.NEXTVAL, :2, :3)", (isbn, title, genre_id))
        conn.commit()
        messagebox.showinfo("Success", "Book inserted successfully!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to insert book: " + str(error))
    finally:
        cursor.close()

# Function to delete book
def delete_book(book_id):
    cursor = conn.cursor()
    try:
        # Check if book ID is provided
        if not book_id:
            raise ValueError("Book ID is required.")
        
        # Check if book exists
        cursor.execute("SELECT COUNT(*) FROM Book WHERE book_id = :1", (book_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            messagebox.showerror("Error", "Book with ID {} does not exist.".format(book_id))
            return
        
        # Delete book
        cursor.execute("DELETE FROM Book WHERE book_id = :1", (book_id,))
        conn.commit()
        messagebox.showinfo("Success", "Book deleted successfully!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to delete book: " + str(error))
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    finally:
        cursor.close()


# Function to update book
def update_book(book_id, isbn, title, genre_id):
    cursor = conn.cursor()
    try:
        # Check if book ID is provided
        if not book_id:
            raise ValueError("Book ID is required.")
        
        # Check if book exists
        cursor.execute("SELECT COUNT(*) FROM Book WHERE book_id = :1", (book_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            messagebox.showerror("Error", "Book with ID {} does not exist.".format(book_id))
            return
        
        # Update book details
        cursor.execute("UPDATE Book SET isbn = :1, title = :2, genre_id = :3 WHERE book_id = :4", (isbn, title, genre_id, book_id))
        conn.commit()
        messagebox.showinfo("Success", "Book updated successfully!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to update book: " + str(error))
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    finally:
        cursor.close()


# Function to insert borrowing
def insert_borrowing(isbn, member_id, return_date, borrow_date):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Borrowing (borrowing_id, isbn, member_id, return_date, borrow_date) VALUES (borrowing_id_sq.NEXTVAL, :1, :2, TO_DATE(:3, 'YYYY-MM-DD'), TO_DATE(:4, 'YYYY-MM-DD'))", (isbn, member_id, return_date, borrow_date))
        conn.commit()
        messagebox.showinfo("Success", "Borrowing information inserted successfully!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to insert borrowing information: " + str(error))
    finally:
        cursor.close()

# Function to delete borrowing
def delete_borrowing(borrowing_id):
    cursor = conn.cursor()
    try:
        # Check if borrowing ID is provided
        if not borrowing_id:
            raise ValueError("Borrowing ID is required.")
        
        # Check if borrowing information exists
        cursor.execute("SELECT COUNT(*) FROM Borrowing WHERE borrowing_id = :1", (borrowing_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            messagebox.showerror("Error", "Borrowing information with ID {} does not exist.".format(borrowing_id))
            return
        
        # Delete borrowing information
        cursor.execute("DELETE FROM Borrowing WHERE borrowing_id = :1", (borrowing_id,))
        conn.commit()
        messagebox.showinfo("Success", "Borrowing information deleted successfully!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to delete borrowing information: " + str(error))
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    finally:
        cursor.close()


# Function to update borrowing
def update_borrowing(borrowing_id, isbn, member_id, return_date, borrow_date):
    cursor = conn.cursor()
    try:
        # Check if borrowing ID is provided
        if not borrowing_id:
            raise ValueError("Borrowing ID is required.")
        
        # Check if borrowing information exists
        cursor.execute("SELECT COUNT(*) FROM Borrowing WHERE borrowing_id = :1", (borrowing_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            messagebox.showerror("Error", "Borrowing information with ID {} does not exist.".format(borrowing_id))
            return
        
        # Update borrowing information
        cursor.execute("UPDATE Borrowing SET isbn = :1, member_id = :2, return_date = TO_DATE(:3, 'YYYY-MM-DD'), borrow_date = TO_DATE(:4, 'YYYY-MM-DD') WHERE borrowing_id = :5", (isbn, member_id, return_date, borrow_date, borrowing_id))
        conn.commit()
        messagebox.showinfo("Success", "Borrowing information updated successfully!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Error", "Failed to update borrowing information: " + str(error))
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    finally:
        cursor.close()


def create_member_form(notebook):
    member_frame = ttk.Frame(notebook)
    notebook.add(member_frame, text="Member Operations")

    # Define treeview to display member data
    member_tree = ttk.Treeview(member_frame, columns=("Name", "Address", "Phone"), height=7)
    member_tree.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

    # Add headings for each column
    member_tree.heading("#0", text="ID")
    member_tree.heading("Name", text="Name")
    member_tree.heading("Address", text="Address")
    member_tree.heading("Phone", text="Phone")

    def refresh_treeview():
        # Clear existing data from the treeview
        member_tree.delete(*member_tree.get_children())

        # Fetch member data and sort by ID (assuming ID is at index 0)
        members = fetch_members()
        sorted_members = sorted(members, key=lambda member: int(member[0]))

        # Insert sorted member data into the treeview
        for member in sorted_members:
            member_tree.insert("", "end", text=member[0], values=(member[1], member[2], member[3]))

    # Call refresh_treeview initially to populate the table
    refresh_treeview()

    # Labels for entry fields
    tk.Label(member_frame, text="Name:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(member_frame, text="Address:").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(member_frame, text="Phone:").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(member_frame, text="Member ID to delete:").grid(row=5, column=0, padx=10, pady=5)
    tk.Label(member_frame, text="Member ID to update:").grid(row=7, column=0, padx=10, pady=5)
    tk.Label(member_frame, text="New Name:").grid(row=8, column=0, padx=10, pady=5)
    tk.Label(member_frame, text="New Address:").grid(row=9, column=0, padx=10, pady=5)
    tk.Label(member_frame, text="New Phone:").grid(row=10, column=0, padx=10, pady=5)

    # Search label and entry
    search_label = tk.Label(member_frame, text="Search by Name/Address/Phone:")
    search_label.grid(row=12, column=0, padx=10, pady=5)
    search_entry = tk.Entry(member_frame)
    search_entry.grid(row=12, column=1, padx=10, pady=5)

    search_entry.bind('<Return>', lambda event: search())

    # Function to handle search operation
    def search():
        search_term = search_entry.get().lower()
        filtered_members = [member for member in fetch_members() if
                            search_term in member[1].lower() or
                            search_term in member[2].lower() or
                            search_term in member[3].lower()]
        refresh_search_table(filtered_members)

    # Button to trigger search operation
    search_button = tk.Button(member_frame, text="Search", command=search)
    search_button.grid(row=12, column=2, padx=10, pady=5)

    # Small table to show search results
    search_results_tree = ttk.Treeview(member_frame, columns=("Name", "Address", "Phone"), height=5)
    search_results_tree.grid(row=13, column=0, columnspan=3, padx=10, pady=5)
    search_results_tree.heading("#0", text="ID")
    search_results_tree.heading("Name", text="Name")
    search_results_tree.heading("Address", text="Address")
    search_results_tree.heading("Phone", text="Phone")

    # Function to refresh search results table
    def refresh_search_table(filtered_members):
        search_results_tree.delete(*search_results_tree.get_children())
        for member in filtered_members:
            search_results_tree.insert("", "end", text=member[0], values=(member[1], member[2], member[3]))

    # Entry fields for user input
    name_entry = tk.Entry(member_frame)
    name_entry.grid(row=1, column=1, padx=10, pady=5)
    address_entry = tk.Entry(member_frame)
    address_entry.grid(row=2, column=1, padx=10, pady=5)
    phone_entry = tk.Entry(member_frame)
    phone_entry.grid(row=3, column=1, padx=10, pady=5)
    delete_entry = tk.Entry(member_frame)
    delete_entry.grid(row=5, column=1, padx=10, pady=5)
    update_id_entry = tk.Entry(member_frame)
    update_id_entry.grid(row=7, column=1, padx=10, pady=5)
    new_name_entry = tk.Entry(member_frame)
    new_name_entry.grid(row=8, column=1, padx=10, pady=5)
    new_address_entry = tk.Entry(member_frame)
    new_address_entry.grid(row=9, column=1, padx=10, pady=5)
    new_phone_entry = tk.Entry(member_frame)
    new_phone_entry.grid(row=10, column=1, padx=10, pady=5)

    # Function to handle insert operation
    def insert_on_enter(event=None):
        insert_member(name_entry.get(), address_entry.get(), phone_entry.get())
        refresh_treeview()  # Refresh treeview after inserting
        # Clear entry fields after inserting
        name_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)

    # Button to trigger insert operation
    insert_button = tk.Button(member_frame, text="Insert", command=insert_on_enter, fg="grey3", bg="violetred1")
    insert_button.grid(row=4, column=0, columnspan=2, pady=5)
    name_entry.bind('<Return>', insert_on_enter)
    address_entry.bind('<Return>', insert_on_enter)
    phone_entry.bind('<Return>', insert_on_enter)

    # Function to handle delete operation
    def delete_on_enter(event=None):
        delete_member(delete_entry.get())
        refresh_treeview()  # Refresh treeview after deleting
        delete_entry.delete(0, tk.END)  # Clear entry field after deleting

    # Button to trigger delete operation
    delete_button = tk.Button(member_frame, text="Delete", command=delete_on_enter, fg="grey3", bg="violet")
    delete_button.grid(row=6, column=0, columnspan=2, pady=5)
    delete_entry.bind('<Return>', delete_on_enter)

    # Function to handle update operation
    def update_on_enter(event=None):
        update_member(update_id_entry.get(), new_name_entry.get(), new_address_entry.get(), new_phone_entry.get())
        refresh_treeview()  # Refresh treeview after updating
        # Clear entry fields after updating
        update_id_entry.delete(0, tk.END)
        new_name_entry.delete(0, tk.END)
        new_address_entry.delete(0, tk.END)
        new_phone_entry.delete(0, tk.END)

    # Button to trigger update operation
    update_button = tk.Button(member_frame, text="Update", command=update_on_enter, fg="grey3", bg="wheat1")
    update_button.grid(row=11, column=0, columnspan=2, pady=5)
    update_id_entry.bind('<Return>', update_on_enter)
    new_name_entry.bind('<Return>', update_on_enter)
    new_address_entry.bind('<Return>', update_on_enter)
    new_phone_entry.bind('<Return>', update_on_enter)

    # Function to generate PDF from table data
    def generate_pdf():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add column headings
        pdf.cell(50, 10, "ID", 1, 0, "C")
        pdf.cell(50, 10, "Name", 1, 0, "C")
        pdf.cell(50, 10, "Address", 1, 0, "C")
        pdf.cell(50, 10, "Phone", 1, 1, "C")

        # Add table data from member_tree
        for child in member_tree.get_children():
            values = member_tree.item(child)['values']
            pdf.cell(50, 10, str(member_tree.item(child)['text']), 1, 0, "C")
            for value in values:
                pdf.cell(50, 10, str(value), 1, 0, "C")
            pdf.cell(200, 10, txt="", ln=True, align="C")  # Add empty line

        pdf_output = "member_data.pdf"
        pdf.output(pdf_output)
        messagebox.showinfo("Success", "PDF generated successfully.")

    # Button to trigger PDF generation
    pdf_button = tk.Button(member_frame, text="Generate PDF", command=generate_pdf, fg="grey3", bg="lightblue")
    pdf_button.grid(row=4, column=2, padx=10, pady=5)

    # Place the button on the right side
    member_frame.grid_columnconfigure(2, weight=1)




    
def create_author_form(notebook):
    author_frame = ttk.Frame(notebook)
    notebook.add(author_frame, text="Author Operations")

    # Define treeview to display author data
    author_tree = ttk.Treeview(author_frame, columns=("Name", "Biography"), height=5)
    author_tree.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    # Add headings for each column
    author_tree.heading("#0", text="ID")
    author_tree.heading("Name", text="Name")
    author_tree.heading("Biography", text="Biography")
    author_tree.column("Name", width=150)
    author_tree.column("Biography", width=650)

    def refresh_treeview():
        # Clear existing data from the treeview
        author_tree.delete(*author_tree.get_children())

        # Fetch and insert author data into the treeview
        for author in fetch_authors():
            author_tree.insert("", "end", text=author[0], values=(author[1], author[2]))

    # Call refresh_treeview initially to populate the table
    refresh_treeview()

    # Labels and entries for name and biography
    tk.Label(author_frame, text="Name:").grid(row=1, column=0, padx=10, pady=5)
    name_entry = tk.Entry(author_frame)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(author_frame, text="Biography:").grid(row=2, column=0, padx=10, pady=5)
    bio_entry = tk.Text(author_frame, width=70, height=4)
    bio_entry.grid(row=2, column=1, padx=10, pady=5)

    # Function to insert an author
    def insert_on_enter(event=None):
        insert_author(name_entry.get(), bio_entry.get("1.0", tk.END))
        refresh_treeview()  # Refresh treeview after inserting
        # Clear entry fields after inserting
        name_entry.delete(0, tk.END)
        bio_entry.delete("1.0", tk.END)

    # Insert button
    insert_button = tk.Button(author_frame, text="Insert", command=insert_on_enter, fg="grey3", bg="violetred1")
    insert_button.grid(row=3, column=0, columnspan=2, pady=10)
    name_entry.bind('<Return>', insert_on_enter)
    bio_entry.bind('<Return>', insert_on_enter)

    # Labels and entry for author ID to delete
    tk.Label(author_frame, text="Author ID to delete:").grid(row=4, column=0, padx=10, pady=5)
    delete_entry = tk.Entry(author_frame)
    delete_entry.grid(row=4, column=1, padx=10, pady=5)

    # Function to delete an author
    def delete_on_enter(event=None):
        delete_author(delete_entry.get())
        refresh_treeview()  # Refresh treeview after deleting
        delete_entry.delete(0, tk.END)  # Clear entry field after deleting

    # Delete button
    delete_button = tk.Button(author_frame, text="Delete", command=delete_on_enter, fg="grey3", bg="violet")
    delete_button.grid(row=5, column=0, columnspan=2, pady=5)
    delete_entry.bind('<Return>', delete_on_enter)

    # Labels and entries for author ID, name, and biography for update
    tk.Label(author_frame, text="Author ID to update:").grid(row=6, column=0, padx=10, pady=5)
    update_id_entry = tk.Entry(author_frame)
    update_id_entry.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(author_frame, text="New Name:").grid(row=7, column=0, padx=10, pady=5)
    new_name_entry = tk.Entry(author_frame)
    new_name_entry.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(author_frame, text="New Biography:").grid(row=8, column=0, padx=10, pady=5)
    new_bio_entry = tk.Text(author_frame, width=70, height=4)
    new_bio_entry.grid(row=8, column=1, padx=10, pady=5)

    # Function to update an author
    def update_on_enter(event=None):
        update_author(update_id_entry.get(), new_name_entry.get(), new_bio_entry.get("1.0", tk.END))
        refresh_treeview()  # Refresh treeview after updating
        # Clear entry fields after updating
        update_id_entry.delete(0, tk.END)
        new_name_entry.delete(0, tk.END)
        new_bio_entry.delete("1.0", tk.END)

    # Update button
    update_button = tk.Button(author_frame, text="Update", command=update_on_enter, fg="grey3", bg="wheat1")
    update_button.grid(row=9, column=0, columnspan=2, pady=5)
    update_id_entry.bind('<Return>', update_on_enter)
    new_name_entry.bind('<Return>', update_on_enter)
    new_bio_entry.bind('<Return>', update_on_enter)

    # Search bar
    search_label = tk.Label(author_frame, text="Search:")
    search_label.grid(row=10, column=0, padx=10, pady=5)
    search_entry = tk.Entry(author_frame)
    search_entry.grid(row=10, column=1, padx=10, pady=5)
    
    search_entry.bind('<Return>', lambda event: search())

    # Function to handle search operation
    def search():
        search_term = search_entry.get().lower()
        filtered_authors = [author for author in fetch_authors() if search_term in author[1].lower()]
        refresh_search_table(filtered_authors)

    # Button to trigger search operation
    search_button = tk.Button(author_frame, text="Search", command=search)
    search_button.grid(row=10, column=2, padx=10, pady=5)

    # Small table to show search results
    search_results_tree = ttk.Treeview(author_frame, columns=("Name", "Biography"), height=5)
    search_results_tree.grid(row=11, column=0, columnspan=3, padx=10, pady=5)
    search_results_tree.heading("#0", text="ID")
    search_results_tree.heading("Name", text="Name")
    search_results_tree.heading("Biography", text="Biography")
    search_results_tree.column("#0",width=30)
    search_results_tree.column("Name", width=120)
    search_results_tree.column("Biography", width=650)

    def refresh_search_table(filtered_authors):
        search_results_tree.delete(*search_results_tree.get_children())
        for author in filtered_authors:
            search_results_tree.insert("", "end", text=author[0], values=(author[1], author[2]))

    def generate_pdf():
        # Tabloid size is 11x17 inches (792x1224 points)
        pdf = FPDF(format=(570, 300))
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add column headings
        pdf.cell(50, 10, "ID", 1, 0, "C")
        pdf.cell(250, 10, "Name", 1, 0, "C")
        pdf.cell(250, 10, "Biography", 1, 1, "C")  # Changed width to match "Name"

        # Add table data from author_tree
        for child in author_tree.get_children():
            values = author_tree.item(child)['values']
            pdf.cell(50, 10, str(author_tree.item(child)['text']), 1, 0, "C")
            for value in values:
                pdf.cell(250, 10, str(value), 1, 0, "C")  # Adjusted width to match "Name"
            pdf.cell(250, 10, txt="", ln=True, align="C")  # Add empty line

        pdf_output = "author_data.pdf"
        pdf.output(pdf_output)
        messagebox.showinfo("Success", "PDF generated successfully.")

# Button to trigger PDF generation
    pdf_button = tk.Button(author_frame, text="Generate PDF", command=generate_pdf, fg="grey3", bg="lightblue")
    pdf_button.grid(row=4, column=2, padx=10, pady=5)

    
    # Place the button on the right side
    author_frame.grid_columnconfigure(2, weight=0)  # Remove column expansion for the PDF button
    author_frame.grid_rowconfigure(11, weight=1)  # Allow row 11 to expand vertically for search results

    
def create_genre_form(notebook):
    genre_frame = ttk.Frame(notebook)
    notebook.add(genre_frame, text="Genre Operations")

    # Define treeview to display genre data
    genre_tree = ttk.Treeview(genre_frame, columns=("Genre Name",), height=5)
    genre_tree.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    # Add headings for each column
    genre_tree.heading("#0", text="ID")
    genre_tree.heading("Genre Name", text="Genre Name")

    def refresh_treeview():
        # Clear existing data from the treeview
        genre_tree.delete(*genre_tree.get_children())

        # Fetch and insert genre data into the treeview
        for genre in fetch_genres():
            genre_tree.insert("", "end", text=genre[0], values=(genre[1],))

    # Call refresh_treeview initially to populate the table
    refresh_treeview()

    # Labels and entry for genre name
    tk.Label(genre_frame, text="Genre Name:").grid(row=1, column=0, padx=10, pady=5)
    genre_entry = tk.Entry(genre_frame)
    genre_entry.grid(row=1, column=1, padx=10, pady=5)

    # Function to insert a genre
    def insert_on_enter(event=None):
        insert_genre(genre_entry.get())
        refresh_treeview()  # Refresh treeview after inserting
        genre_entry.delete(0, tk.END)  # Clear entry field after inserting

    # Insert button
    insert_button = tk.Button(genre_frame, text="Insert", command=insert_on_enter, fg="grey3", bg="violetred1")
    insert_button.grid(row=2, column=0, columnspan=2, pady=10)
    genre_entry.bind('<Return>', insert_on_enter)

    # Labels and entry for genre ID to delete
    tk.Label(genre_frame, text="Genre ID to delete:").grid(row=3, column=0, padx=10, pady=5)
    delete_entry = tk.Entry(genre_frame)
    delete_entry.grid(row=3, column=1, padx=10, pady=5)

    # Function to delete a genre
    def delete_on_enter(event=None):
        delete_genre(delete_entry.get())
        refresh_treeview()  # Refresh treeview after deleting
        delete_entry.delete(0, tk.END)  # Clear entry field after deleting

    # Delete button
    delete_button = tk.Button(genre_frame, text="Delete", command=delete_on_enter, fg="grey3", bg="violet")
    delete_button.grid(row=4, column=0, columnspan=2, pady=5)
    delete_entry.bind('<Return>', delete_on_enter)

    # Labels and entries for genre ID and name for update
    tk.Label(genre_frame, text="Genre ID to update:").grid(row=5, column=0, padx=10, pady=5)
    update_id_entry = tk.Entry(genre_frame)
    update_id_entry.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(genre_frame, text="New Genre Name:").grid(row=6, column=0, padx=10, pady=5)
    new_genre_entry = tk.Entry(genre_frame)
    new_genre_entry.grid(row=6, column=1, padx=10, pady=5)

    # Function to update a genre
    def update_on_enter(event=None):
        update_genre(update_id_entry.get(), new_genre_entry.get())
        refresh_treeview()  # Refresh treeview after updating
        # Clear entry fields after updating
        update_id_entry.delete(0, tk.END)
        new_genre_entry.delete(0, tk.END)

    # Update button
    update_button = tk.Button(genre_frame, text="Update", command=update_on_enter, fg="grey3", bg="wheat1")
    update_button.grid(row=7, column=0, columnspan=2, pady=5)
    update_id_entry.bind('<Return>', update_on_enter)
    new_genre_entry.bind('<Return>', update_on_enter)

    # Search bar
    search_label = tk.Label(genre_frame, text="Search:")
    search_label.grid(row=8, column=0, padx=10, pady=5)
    search_entry = tk.Entry(genre_frame)
    search_entry.grid(row=8, column=1, padx=10, pady=5)

    search_entry.bind('<Return>', lambda event: search())

    # Function to handle search operation
    def search():
        search_term = search_entry.get().lower()
        filtered_genres = [genre for genre in fetch_genres() if search_term in genre[1].lower()]
        refresh_search_table(filtered_genres)

    # Button to trigger search operation
    search_button = tk.Button(genre_frame, text="Search", command=search)
    search_button.grid(row=8, column=2, padx=10, pady=5)

    # Small table to show search results
    search_results_tree = ttk.Treeview(genre_frame, columns=("Genre Name",), height=7)
    search_results_tree.grid(row=9, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")
    search_results_tree.heading("#0", text="ID")
    search_results_tree.heading("Genre Name", text="Genre Name")

    def refresh_search_table(filtered_genres):
        search_results_tree.delete(*search_results_tree.get_children())
        for genre in filtered_genres:
            search_results_tree.insert("", "end", text=genre[0], values=(genre[1],))

    # Weight for search results table
    genre_frame.rowconfigure(13, weight=1)

    # Function to generate PDF from table data
    def generate_pdf():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add column headings
        pdf.cell(50, 10, "ID", 1, 0, "C")
        pdf.cell(100, 10, "Genre Name", 1, 1, "C")

        # Add table data from genre_tree
        for child in genre_tree.get_children():
            values = genre_tree.item(child)['values']
            pdf.cell(50, 10, str(genre_tree.item(child)['text']), 1, 0, "C")
            for value in values:
                pdf.cell(100, 10, str(value), 1, 1, "C")

        pdf_output = "genre_data.pdf"
        pdf.output(pdf_output)
        messagebox.showinfo("Success", "PDF generated successfully.")

    # Button to trigger PDF generation
    pdf_button = tk.Button(genre_frame, text="Generate PDF", command=generate_pdf, fg="grey3", bg="lightblue")
    pdf_button.grid(row=4, column=2, padx=10, pady=5)
    
    # Place the button on the right side
    genre_frame.grid_columnconfigure(2, weight=1)  # Allow column 2 to expand

    return genre_frame


    
def create_library_form(notebook):
    library_frame = ttk.Frame(notebook)
    notebook.add(library_frame, text="Library Operations")

    # Define treeview to display library data
    library_tree = ttk.Treeview(library_frame, columns=("Phone", "Address"))
    library_tree.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

    # Add headings for each column
    library_tree.heading("#0", text="ID")
    library_tree.heading("Phone", text="Phone")
    library_tree.heading("Address", text="Address")

    # Function to refresh library treeview
    def refresh_library_treeview():
        # Clear existing data from the treeview
        for child in library_tree.get_children():
            library_tree.delete(child)

        # Fetch and insert library data into the treeview
        for library in fetch_libraries():
            library_tree.insert("", "end", text=library[0], values=(library[1], library[2]))

    # Call refresh function initially to populate the table
    refresh_library_treeview()

    tk.Label(library_frame, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
    phone_entry = tk.Entry(library_frame)
    phone_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(library_frame, text="Address:").grid(row=2, column=0, padx=10, pady=5)
    address_entry = tk.Entry(library_frame)
    address_entry.grid(row=2, column=1, padx=10, pady=5)

    def insert_on_enter(event=None):
        insert_library(phone_entry.get(), address_entry.get())
        refresh_library_treeview()  # Refresh treeview after inserting
        # Clear entry fields after inserting
        phone_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

    insert_button = tk.Button(library_frame, text="Insert", command=insert_on_enter, fg="grey3", bg="violetred1")
    insert_button.grid(row=3, column=0, columnspan=2, pady=10)
    phone_entry.bind('<Return>', insert_on_enter)
    address_entry.bind('<Return>', insert_on_enter)

    tk.Label(library_frame, text="Library ID to delete:").grid(row=4, column=0, padx=10, pady=5)
    delete_entry = tk.Entry(library_frame)
    delete_entry.grid(row=4, column=1, padx=10, pady=5)

    def delete_on_enter(event=None):
        delete_library(delete_entry.get())
        refresh_library_treeview()  # Refresh treeview after deleting
        delete_entry.delete(0, tk.END)  # Clear entry field after deleting

    delete_button = tk.Button(library_frame, text="Delete", command=delete_on_enter, fg="grey3", bg="violet")
    delete_button.grid(row=5, column=0, columnspan=2, pady=5)
    delete_entry.bind('<Return>', delete_on_enter)

    tk.Label(library_frame, text="Library ID to update:").grid(row=6, column=0, padx=10, pady=5)
    update_id_entry = tk.Entry(library_frame)
    update_id_entry.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(library_frame, text="New Phone:").grid(row=7, column=0, padx=10, pady=5)
    new_phone_entry = tk.Entry(library_frame)
    new_phone_entry.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(library_frame, text="New Address:").grid(row=8, column=0, padx=10, pady=5)
    new_address_entry = tk.Entry(library_frame)
    new_address_entry.grid(row=8, column=1, padx=10, pady=5)

    def update_on_enter(event=None):
        update_library(update_id_entry.get(), new_phone_entry.get(), new_address_entry.get())
        refresh_library_treeview()  # Refresh treeview after updating
        # Clear entry fields after updating
        update_id_entry.delete(0, tk.END)
        new_phone_entry.delete(0, tk.END)
        new_address_entry.delete(0, tk.END)

    update_button = tk.Button(library_frame, text="Update", command=update_on_enter, fg="grey3", bg="wheat1")
    update_button.grid(row=9, column=0, columnspan=2, pady=5)
    update_id_entry.bind('<Return>', update_on_enter)
    new_phone_entry.bind('<Return>', update_on_enter)
    new_address_entry.bind('<Return>', update_on_enter)

    # Search bar
    search_label = tk.Label(library_frame, text="Search:")
    search_label.grid(row=10, column=0, padx=10, pady=5)
    search_entry = tk.Entry(library_frame)
    search_entry.grid(row=10, column=1, padx=10, pady=5)
    
    search_entry.bind('<Return>', lambda event: search())


    # Function to handle search operation
    def search():
        search_term = search_entry.get().lower()
        filtered_libraries = [library for library in fetch_libraries() if search_term in str(library).lower()]
        refresh_search_table(filtered_libraries)

    # Button to trigger search operation
    search_button = tk.Button(library_frame, text="Search", command=search)
    search_button.grid(row=10, column=2, padx=10, pady=5)

    # Small table to show search results
    search_results_tree = ttk.Treeview(library_frame, columns=("Phone", "Address"), height=3)
    search_results_tree.grid(row=11, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")
    search_results_tree.heading("#0", text="ID")
    search_results_tree.heading("Phone", text="Phone")
    search_results_tree.heading("Address", text="Address")

    def refresh_search_table(filtered_libraries):
        search_results_tree.delete(*search_results_tree.get_children())
        for library in filtered_libraries:
            search_results_tree.insert("", "end", text=library[0], values=(library[1], library[2]))

    # Weight for search results table
    library_frame.rowconfigure(11, weight=1)

    # Function to generate PDF from table data
    def generate_pdf():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add column headings
        pdf.cell(50, 10, "ID", 1, 0, "C")
        pdf.cell(70, 10, "Phone", 1, 0, "C")
        pdf.cell(70, 10, "Address", 1, 1, "C")

        # Add table data from library_tree
        for child in library_tree.get_children():
            values = library_tree.item(child)['values']
            pdf.cell(50, 10, str(library_tree.item(child)['text']), 1, 0, "C")
            for value in values:
                pdf.cell(70, 10, str(value), 1, 0, "C")
            pdf.cell(150, 10, txt="", ln=True, align="C")  # Add empty line

        pdf_output = "library_data.pdf"
        pdf.output(pdf_output)
        messagebox.showinfo("Success", "PDF generated successfully.")

    # Button to trigger PDF generation
    pdf_button = tk.Button(library_frame, text="Generate PDF", command=generate_pdf, fg="grey3", bg="lightblue")
    pdf_button.grid(row=4, column=2, padx=10, pady=5)
    
    # Place the button on the right side
    library_frame.grid_columnconfigure(2, weight=1)  # Allow column 2 to expand

    return library_frame


  
def create_book_form(notebook):
    book_frame = ttk.Frame(notebook)
    notebook.add(book_frame, text="Book Operations")

    # Define treeview to display book data
    book_tree = ttk.Treeview(book_frame, columns=("ISBN", "Title", "Genre ID"), height=7)
    book_tree.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

    # Add headings for each column
    book_tree.heading("#0", text="ID")
    book_tree.heading("ISBN", text="ISBN")
    book_tree.heading("Title", text="Title")
    book_tree.heading("Genre ID", text="Genre ID")

    # Function to refresh book treeview
    def refresh_book_treeview():
        # Clear existing data from the treeview
        for child in book_tree.get_children():
            book_tree.delete(child)

        # Fetch and insert book data into the treeview
        for book in fetch_books():
            book_tree.insert("", "end", text=book[0], values=(book[1], book[2], book[3]))

    # Call refresh function initially to populate the table
    refresh_book_treeview()

    # Labels and entries for ISBN, title, and genre ID
    tk.Label(book_frame, text="ISBN:").grid(row=1, column=0, padx=10, pady=5)
    isbn_entry = tk.Entry(book_frame)
    isbn_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(book_frame, text="Title:").grid(row=2, column=0, padx=10, pady=5)
    title_entry = tk.Entry(book_frame)
    title_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(book_frame, text="Genre ID:").grid(row=3, column=0, padx=10, pady=5)
    genre_entry = tk.Entry(book_frame)
    genre_entry.grid(row=3, column=1, padx=10, pady=5)

    # Function to insert a book
    def insert_on_enter(event=None):
        insert_book(isbn_entry.get(), title_entry.get(), genre_entry.get())
        refresh_book_treeview()  # Refresh treeview after inserting
        # Clear entry fields after inserting
        isbn_entry.delete(0, tk.END)
        title_entry.delete(0, tk.END)
        genre_entry.delete(0, tk.END)

    # Insert button
    insert_button = tk.Button(book_frame, text="Insert", command=insert_on_enter, fg="grey3", bg="violetred1")
    insert_button.grid(row=4, column=0, columnspan=2, pady=10)
    isbn_entry.bind('<Return>', insert_on_enter)
    title_entry.bind('<Return>', insert_on_enter)
    genre_entry.bind('<Return>', insert_on_enter)

    # Labels and entry for book ID to delete
    tk.Label(book_frame, text="Book ID to delete:").grid(row=5, column=0, padx=10, pady=5)
    delete_entry = tk.Entry(book_frame)
    delete_entry.grid(row=5, column=1, padx=10, pady=5)

    # Function to delete a book
    def delete_on_enter(event=None):
        delete_book(delete_entry.get())
        refresh_book_treeview()  # Refresh treeview after deleting
        delete_entry.delete(0, tk.END)  # Clear entry field after deleting

    # Delete button
    delete_button = tk.Button(book_frame, text="Delete", command=delete_on_enter, fg="grey3", bg="violet")
    delete_button.grid(row=6, column=0, columnspan=2, pady=5)
    delete_entry.bind('<Return>', delete_on_enter)

    # Labels and entries for book ID, ISBN, title, and genre ID for update
    tk.Label(book_frame, text="Book ID to update:").grid(row=7, column=0, padx=10, pady=5)
    update_id_entry = tk.Entry(book_frame)
    update_id_entry.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(book_frame, text="New ISBN:").grid(row=8, column=0, padx=10, pady=5)
    new_isbn_entry = tk.Entry(book_frame)
    new_isbn_entry.grid(row=8, column=1, padx=10, pady=5)

    tk.Label(book_frame, text="New Title:").grid(row=9, column=0, padx=10, pady=5)
    new_title_entry = tk.Entry(book_frame)
    new_title_entry.grid(row=9, column=1, padx=10, pady=5)

    tk.Label(book_frame, text="New Genre ID:").grid(row=10, column=0, padx=10, pady=5)
    new_genre_entry = tk.Entry(book_frame)
    new_genre_entry.grid(row=10, column=1, padx=10, pady=5)

    # Function to update a book
    def update_on_enter(event=None):
        update_book(update_id_entry.get(), new_isbn_entry.get(), new_title_entry.get(), new_genre_entry.get())
        refresh_book_treeview()  # Refresh treeview after updating
        # Clear entry fields after updating
        update_id_entry.delete(0, tk.END)
        new_isbn_entry.delete(0, tk.END)
        new_title_entry.delete(0, tk.END)
        new_genre_entry.delete(0, tk.END)

    # Update button
    update_button = tk.Button(book_frame, text="Update", command=update_on_enter, fg="grey3", bg="wheat1")
    update_button.grid(row=11, column=0, columnspan=2, pady=5)
    update_id_entry.bind('<Return>', update_on_enter)
    new_isbn_entry.bind('<Return>', update_on_enter)
    new_title_entry.bind('<Return>', update_on_enter)
    new_genre_entry.bind('<Return>', update_on_enter)

    # Search bar
    search_label = tk.Label(book_frame, text="Search:")
    search_label.grid(row=12, column=0, padx=10, pady=5)
    search_entry = tk.Entry(book_frame)
    search_entry.grid(row=12, column=1, padx=10, pady=5)
    
    search_entry.bind('<Return>', lambda event: search())

    # Function to handle search operation
    def search():
        search_term = search_entry.get().lower()
        filtered_books = [book for book in fetch_books() if search_term in str(book).lower()]
        refresh_search_table(filtered_books)

    # Button to trigger search operation
    search_button = tk.Button(book_frame, text="Search", command=search)
    search_button.grid(row=12, column=2, padx=10, pady=5)

    # Small table to show search results
    search_results_tree = ttk.Treeview(book_frame, columns=("ISBN", "Title", "Genre ID"), height=3)
    search_results_tree.grid(row=13, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")
    search_results_tree.heading("#0", text="ID")
    search_results_tree.heading("ISBN", text="ISBN")
    search_results_tree.heading("Title", text="Title")
    search_results_tree.heading("Genre ID", text="Genre ID")

    def refresh_search_table(filtered_books):
        search_results_tree.delete(*search_results_tree.get_children())
        for book in filtered_books:
            search_results_tree.insert("", "end", text=book[0], values=(book[1], book[2], book[3]))

    # Weight for search results table
    book_frame.rowconfigure(13, weight=1)

    # Function to generate PDF from table data
    def generate_pdf():
        # Tabloid size is 11x17 inches (792x1224 points)
        pdf = FPDF(format=(300, 300))
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add column headings
        pdf.cell(40, 10, "ID", 1, 0, "C")
        pdf.cell(80, 10, "ISBN", 1, 0, "C")
        pdf.cell(80, 10, "Title", 1, 0, "C")
        pdf.cell(80, 10, "Genre ID", 1, 1, "C")

        # Add table data from book_tree
        for child in book_tree.get_children():
            values = book_tree.item(child)['values']
            pdf.cell(40, 10, str(book_tree.item(child)['text']), 1, 0, "C")
            for value in values:
                pdf.cell(80, 10, str(value), 1, 0, "C")
            pdf.cell(180, 10, txt="", ln=True, align="C")  # Add empty line

        pdf_output = "book_data.pdf"
        pdf.output(pdf_output)
        messagebox.showinfo("Success", "PDF generated successfully.")

    # Button to trigger PDF generation
    pdf_button = tk.Button(book_frame, text="Generate PDF", command=generate_pdf, fg="grey3", bg="lightblue")
    pdf_button.grid(row=4, column=2, padx=10, pady=5)
    
    # Place the button on the right side
    book_frame.grid_columnconfigure(2, weight=1)  # Allow column 2 to expand

    return book_frame



def create_borrowing_form(notebook):
    borrowing_frame = ttk.Frame(notebook)
    notebook.add(borrowing_frame, text="Borrowing Operations")

    # Define treeview to display borrowing data
    borrowing_tree = ttk.Treeview(borrowing_frame, columns=("ISBN", "Member ID", "Return Date", "Borrow Date"), height=5)
    borrowing_tree.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

    # Add headings for each column
    borrowing_tree.heading("#0", text="ID")
    borrowing_tree.heading("ISBN", text="ISBN")
    borrowing_tree.heading("Member ID", text="Member ID")
    borrowing_tree.heading("Return Date", text="Return Date")
    borrowing_tree.heading("Borrow Date", text="Borrow Date")

    # Function to refresh borrowing treeview
    def refresh_borrowing_treeview():
        # Clear existing data from the treeview
        for child in borrowing_tree.get_children():
            borrowing_tree.delete(child)

        # Fetch and insert borrowing data into the treeview
        for borrowing in fetch_borrowings():
            borrowing_tree.insert("", "end", text=borrowing[0], values=(borrowing[1], borrowing[2], borrowing[3], borrowing[4]))

    # Call refresh function initially to populate the table
    refresh_borrowing_treeview()

    # Labels and entries for ISBN, member ID, return date, and borrow date
    tk.Label(borrowing_frame, text="ISBN:").grid(row=1, column=0, padx=10, pady=5)
    isbn_entry = tk.Entry(borrowing_frame)
    isbn_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(borrowing_frame, text="Member ID:").grid(row=2, column=0, padx=10, pady=5)
    member_entry = tk.Entry(borrowing_frame)
    member_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(borrowing_frame, text="Return Date (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
    return_entry = tk.Entry(borrowing_frame)
    return_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(borrowing_frame, text="Borrow Date (YYYY-MM-DD):").grid(row=4, column=0, padx=10, pady=5)
    borrow_entry = tk.Entry(borrowing_frame)
    borrow_entry.grid(row=4, column=1, padx=10, pady=5)

    # Function to insert a borrowing
    def insert_on_enter(event=None):
        insert_borrowing(isbn_entry.get(), member_entry.get(), return_entry.get(), borrow_entry.get())
        refresh_borrowing_treeview()  # Refresh treeview after inserting
        # Clear entry fields after inserting
        isbn_entry.delete(0, tk.END)
        member_entry.delete(0, tk.END)
        return_entry.delete(0, tk.END)
        borrow_entry.delete(0, tk.END)

    # Insert button
    insert_button = tk.Button(borrowing_frame, text="Insert", command=insert_on_enter, fg="grey3", bg="violetred1")
    insert_button.grid(row=5, column=0, columnspan=2, pady=10)
    isbn_entry.bind('<Return>', insert_on_enter)
    member_entry.bind('<Return>', insert_on_enter)
    return_entry.bind('<Return>', insert_on_enter)
    borrow_entry.bind('<Return>', insert_on_enter)

    # Labels and entry for borrowing ID to delete
    tk.Label(borrowing_frame, text="Borrowing ID to delete:").grid(row=6, column=0, padx=10, pady=5)
    delete_entry = tk.Entry(borrowing_frame)
    delete_entry.grid(row=6, column=1, padx=10, pady=5)

    # Function to delete a borrowing
    def delete_on_enter(event=None):
        delete_borrowing(delete_entry.get())
        refresh_borrowing_treeview()  # Refresh treeview after deleting
        delete_entry.delete(0, tk.END)  # Clear entry field after deleting

    # Delete button
    delete_button = tk.Button(borrowing_frame, text="Delete", command=delete_on_enter, fg="grey3", bg="violet")
    delete_button.grid(row=7, column=0, columnspan=2, pady=5)
    delete_entry.bind('<Return>', delete_on_enter)

    # Labels and entries for borrowing ID, ISBN, member ID, return date, and borrow date for update
    tk.Label(borrowing_frame, text="Borrowing ID to update:").grid(row=8, column=0, padx=10, pady=5)
    update_id_entry = tk.Entry(borrowing_frame)
    update_id_entry.grid(row=8, column=1, padx=10, pady=5)

    tk.Label(borrowing_frame, text="New ISBN:").grid(row=9, column=0, padx=10, pady=5)
    new_isbn_entry = tk.Entry(borrowing_frame)
    new_isbn_entry.grid(row=9, column=1, padx=10, pady=5)

    tk.Label(borrowing_frame, text="New Member ID:").grid(row=10, column=0, padx=10, pady=5)
    new_member_entry = tk.Entry(borrowing_frame)
    new_member_entry.grid(row=10, column=1, padx=10, pady=5)

    tk.Label(borrowing_frame, text="New Return Date (YYYY-MM-DD):").grid(row=11, column=0, padx=10, pady=5)
    new_return_entry = tk.Entry(borrowing_frame)
    new_return_entry.grid(row=11, column=1, padx=10, pady=5)

    tk.Label(borrowing_frame, text="New Borrow Date (YYYY-MM-DD):").grid(row=12, column=0, padx=10, pady=5)
    new_borrow_entry = tk.Entry(borrowing_frame)
    new_borrow_entry.grid(row=12, column=1, padx=10, pady=5)

    # Function to update a borrowing
    def update_on_enter(event=None):
        update_borrowing(update_id_entry.get(), new_isbn_entry.get(), new_member_entry.get(), new_return_entry.get(), new_borrow_entry.get())
        refresh_borrowing_treeview()  # Refresh treeview after updating
        # Clear entry fields after updating
        update_id_entry.delete(0, tk.END)
        new_isbn_entry.delete(0, tk.END)
        new_member_entry.delete(0, tk.END)
        new_return_entry.delete(0, tk.END)
        new_borrow_entry.delete(0, tk.END)

    # Update button
    update_button = tk.Button(borrowing_frame, text="Update", command=update_on_enter, fg="grey3", bg="wheat1")
    update_button.grid(row=13, column=0, columnspan=2, pady=5)
    update_id_entry.bind('<Return>', update_on_enter)
    new_isbn_entry.bind('<Return>', update_on_enter)
    new_member_entry.bind('<Return>', update_on_enter)
    new_return_entry.bind('<Return>', update_on_enter)
    new_borrow_entry.bind('<Return>', update_on_enter)

    # Search bar
    search_label = tk.Label(borrowing_frame, text="Search:")
    search_label.grid(row=14, column=0, padx=10, pady=5)
    search_entry = tk.Entry(borrowing_frame)
    search_entry.grid(row=14, column=1, padx=10, pady=5)
    
    search_entry.bind('<Return>', lambda event: search())

    # Function to handle search operation
    def search():
        search_term = search_entry.get().lower()
        filtered_borrowings = [borrowing for borrowing in fetch_borrowings() if search_term in borrowing[1].lower()]
        refresh_search_table(filtered_borrowings)

    # Button to trigger search operation
    search_button = tk.Button(borrowing_frame, text="Search", command=search)
    search_button.grid(row=14, column=2, padx=10, pady=5)

    # Small table to show search results
    search_results_tree = ttk.Treeview(borrowing_frame, columns=("ISBN", "Member ID", "Return Date", "Borrow Date"), height=4)
    search_results_tree.grid(row=15, column=0, columnspan=2, padx=10, pady=5)
    search_results_tree.heading("#0", text="ID")
    search_results_tree.heading("ISBN", text="ISBN")
    search_results_tree.heading("Member ID", text="Member ID")
    search_results_tree.heading("Return Date", text="Return Date")
    search_results_tree.heading("Borrow Date", text="Borrow Date")

    def refresh_search_table(filtered_borrowings):
        search_results_tree.delete(*search_results_tree.get_children())
        for borrowing in filtered_borrowings:
            search_results_tree.insert("", "end", text=borrowing[0], values=(borrowing[1], borrowing[2], borrowing[3], borrowing[4]))

    # Weight for search results table
    borrowing_frame.rowconfigure(15, weight=1)

    # Function to generate PDF from table data
    def generate_pdf():
        pdf = FPDF(format=(300, 300))
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add column headings
        pdf.cell(40, 10, "ID", 1, 0, "C")
        pdf.cell(60, 10, "ISBN", 1, 0, "C")
        pdf.cell(60, 10, "Member ID", 1, 0, "C")
        pdf.cell(60, 10, "Return Date", 1, 0, "C")
        pdf.cell(60, 10, "Borrow Date", 1, 1, "C")

        # Add table data from borrowing_tree
        for child in borrowing_tree.get_children():
            values = borrowing_tree.item(child)['values']
            pdf.cell(40, 10, str(borrowing_tree.item(child)['text']), 1, 0, "C")
            for value in values:
                pdf.cell(60, 10, str(value), 1, 0, "C")
            pdf.cell(180, 10, txt="", ln=True, align="C")  # Add empty line

        pdf_output = "borrowing_data.pdf"
        pdf.output(pdf_output)
        messagebox.showinfo("Success", "PDF generated successfully.")

    # Button to trigger PDF generation
    pdf_button = tk.Button(borrowing_frame, text="Generate PDF", command=generate_pdf, fg="grey3", bg="lightblue")
    pdf_button.grid(row=4, column=2, padx=10, pady=5)
    
   # Place the button on the right side
    borrowing_frame.grid_columnconfigure(2, weight=0)  # Remove column expansion for the PDF button
    borrowing_frame.grid_rowconfigure(11, weight=1)  # Allow row 11 to expand vertically for search results
    
    return borrowing_frame

def main():
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("1100x750")
    root.iconbitmap("D:\Second Year\Second Term\Database Systems\Project\icon\icon.ico")

    login(root)

    root.mainloop()


def login(root):
    # Dictionary to store username-password pairs
    users = {
        "Mohammed": "Moh2004",
        "Fatma": "Fatma2004",
        "Reem": "Reem2004"
    }

    # Create login frame
    login_frame = tk.Frame(root)
    login_frame.pack(fill=tk.BOTH, expand=True)
    
    # Load and display the background image
    image = Image.open("D:\Second Year\Second Term\Database Systems\Project\icon\R.jpeg")
    photo = ImageTk.PhotoImage(image)
    bg_label = tk.Label(login_frame, image=photo)
    bg_label.image = photo  # Retain reference to the image object to prevent garbage collection
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Username label and entry
    username_label = tk.Label(login_frame, text="Username:",font="blood",bg="darkkhaki")
    username_label.pack(pady=(275, 1))
    username_entry = tk.Entry(login_frame,font="blood")
    username_entry.pack()

    # Password label and entry
    password_label = tk.Label(login_frame, text="Password:",font="blood",bg="darkkhaki")
    password_label.pack()
    password_entry = tk.Entry(login_frame, show="*",font="blood")
    password_entry.pack()

    def validate_login(event=None):  # Accept an event argument for key binding
        username = username_entry.get()
        password = password_entry.get()
        if username in users and users[username] == password:
            # If username and password match, destroy login frame and proceed
            login_frame.destroy()
            create_main_page(root)
        else:
            # If username and password don't match, show error message
            error_label = tk.Label(login_frame, text="Invalid username or password",bg="darkkhaki" ,fg="red")
            error_label.pack()
            login_frame.after(2000, error_label.destroy)
    
    # Login button
    login_button = tk.Button(login_frame, text="Login", command=validate_login,font="blood",fg="gray3",bg="darkolivegreen1")
    login_button.pack(pady=10)

    # Bind Enter key to validate_login function
    root.bind('<Return>', validate_login)




# Create the main page after login
def create_main_page(root):
    # Create a notebook to switch between different operations
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True)

    # Create forms for different operations
    create_member_form(notebook)
    create_author_form(notebook)
    create_genre_form(notebook)
    create_library_form(notebook)
    create_book_form(notebook)
    create_borrowing_form(notebook)

    
    
    # Create a logout button
    logout_button = tk.Button(root, text="Logout", command=lambda: logout(root),font="blood",fg="grey3",bg="red")
    logout_button.pack(side=tk.BOTTOM, pady=10)

# Function to log out
def logout(root):
    # Destroy the root window and recreate the main window
    root.destroy()
    main()

# Add your other functions and GUI components here

# Run the main function
if __name__ == "__main__":
    main()