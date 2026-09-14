import tkinter as tk
root=tk.Tk()
root.title("Travel record management system")
root.geometry("500x400")

def open_airline_window():
    # Create a new window
    airline_window = tk.Toplevel(root)

    # Set the window title and size
    airline_window.title("Airline Records")
    airline_window.geometry("500x350")

    # Page title
    title_label = tk.Label(
        airline_window,
        text="Airline Records",
        font=("Arial", 18)
    )
    title_label.pack(pady=20)

    # Airline ID
    id_label = tk.Label(
        airline_window,
        text="Airline ID"
    )
    id_label.pack()

    id_entry = tk.Entry(
        airline_window,
        width=30
    )
    id_entry.pack(pady=5)

    # Company Name
    company_label = tk.Label(
        airline_window,
        text="Company Name"
    )
    company_label.pack()

    company_entry = tk.Entry(
        airline_window,
        width=30
    )
    company_entry.pack(pady=5)

    # Back button
    back_button = tk.Button(
        airline_window,
        text="Back",
        width=15,
        command=airline_window.destroy
    )
    back_button.pack(pady=20)


title_Label=tk.Label(root,
                     text="Travel Record Management System",
                    font=("Arial",18)
)
title_Label.pack(pady=30)



clients_button=tk.Button(root, 
                          text="Manage Clients", 
                          width=20)
clients_button.pack(pady=10)


flights_button=tk.Button(root,
                         text="Manage Flights",
                         width=20)
flights_button.pack(pady=10)


airlines_button=tk.Button(root,
                          text="Manage Airlines",
                          width=20,
                          command=open_airline_window)
airlines_button.pack(pady=10)


exit_button=tk.Button(root,
                      text="Exit",
                      width=20,
                      command=root.destroy)
exit_button.pack(pady=10)
root.mainloop()