import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Travel record management system")
root.geometry("500x400")

airline_records = []
client_records = []
flight_records = []

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

    def create_airline():
        airline_id = id_entry.get()
        company_name = company_entry.get()

    # Check that both fields have been completed
        if airline_id == "" or company_name == "":
         messagebox.showerror(
            "Input Error",
            "Please complete all fields."
        )
         return

    # Check that Airline ID is a number
        if not airline_id.isdigit():
         messagebox.showerror(
            "Input Error",
            "Airline ID must be a number."
        )
         return

        airline_record = {
         "ID": int(airline_id),
         "Type": "Airline",
         "Company Name": company_name
        }
        airline_records.append(airline_record)

        messagebox.showinfo(
         "Airline Created",
         "Airline record created Successfully"
        )
        
        # Clear the input boxes
        id_entry.delete(0, tk.END)
        company_entry.delete(0, tk.END)

    def search_airline():
        airline_id = id_entry.get()

    # Check that an ID was entered
        if airline_id == "":
          messagebox.showerror(
            "Input Error",
            "Please enter an Airline ID."
        )
          return

    # Check that the ID is a number
        if not airline_id.isdigit():
          messagebox.showerror(
            "Input Error",
            "Airline ID must be a number."
        )
          return

    # Search through the airline records
        for record in airline_records:
          if record["ID"] == int(airline_id):

            # Clear the company name box
            company_entry.delete(0, tk.END)

            # Display the company name
            company_entry.insert(
                0,
                record["Company Name"]
            )
            return

    # If no matching record was found
        messagebox.showerror(
        "Not Found",
        "Airline record not found."
    )
        
    def update_airline():
        airline_id = id_entry.get()
        company_name = company_entry.get()

    # Check that both fields are completed
        if airline_id == "" or company_name == "":
          messagebox.showerror(
            "Input Error",
            "Please complete all fields."
        )
          return

    # Check that Airline ID is a number
        if not airline_id.isdigit():
          messagebox.showerror(
            "Input Error",
            "Airline ID must be a number."
        )
          return

    # Search for the airline record
        for record in airline_records:
          if record["ID"] == int(airline_id):
            # Update the company name
            record["Company Name"] = company_name

            messagebox.showinfo(
                "Airline Updated",
                "Airline record updated successfully."
            )

            # Clear the input boxes
            id_entry.delete(0, tk.END)
            company_entry.delete(0, tk.END)

            return

         # If the ID was not found
          messagebox.showerror(
           "Not Found",
           "Airline record not found."
    )
    def delete_airline():
        airline_id = id_entry.get()

       # Check that an ID was entered
        if airline_id == "":
          messagebox.showerror(
            "Input Error",
            "Please enter an Airline ID."
        )
          return

        # Check that the ID is a number
        if not airline_id.isdigit():
          messagebox.showerror(
            "Input Error",
            "Airline ID must be a number."
        )
          return

        # Search for the airline record
        for record in airline_records:
          if record["ID"] == int(airline_id):

            # Ask for confirmation before deleting
            confirm = messagebox.askyesno(
                "Confirm Delete",
                "Are you sure you want to delete this airline record?"
            )

            if confirm:
                airline_records.remove(record)

                messagebox.showinfo(
                    "Airline Deleted",
                    "Airline record deleted successfully."
                )

                id_entry.delete(0, tk.END)
                company_entry.delete(0, tk.END)

                return

       # If the ID was not found
        messagebox.showerror(
         "Not Found",
         "Airline record not found."
        )
    
    button_frame = tk.Frame(airline_window)
    button_frame.pack(pady=20)


   # Create button
    create_button = tk.Button(
    button_frame,
    text="Create",
    width=10,
    command=create_airline
)
    create_button.pack(side="left", padx=5)


   # Search button
    search_button = tk.Button(
    button_frame,
    text="Search",
    width=10,
    command=search_airline
)
    search_button.pack(side="left", padx=5)


   # Update button
    update_button = tk.Button(
    button_frame,
    text="Update",
    width=10,
    command=update_airline
)
    update_button.pack(side="left", padx=5)


   # Delete button
    delete_button = tk.Button(
    button_frame,
    text="Delete",
    width=10,
    command=delete_airline
)
    delete_button.pack(side="left", padx=5)

    # Back button
    back_button = tk.Button(
        airline_window,
        text="Back",
        width=15,
        command=airline_window.destroy
    )
    back_button.pack(pady=20)

def open_client_window():
    # Create a new window
    client_window = tk.Toplevel(root)

    # Set the window title and size
    client_window.title("Client Records")
    client_window.geometry("600x700")

    # Page title
    title_label = tk.Label(
        client_window,
        text="Client Records",
        font=("Arial", 18)
    )
    title_label.pack(pady=20)

    # Client ID
    id_label = tk.Label(
        client_window,
        text="Client ID"
    )
    id_label.pack()

    id_entry = tk.Entry(
        client_window,
        width=35
    )
    id_entry.pack(pady=5)

    # Name
    name_label = tk.Label(
        client_window,
        text="Name"
    )
    name_label.pack()

    name_entry = tk.Entry(
        client_window,
        width=35
    )
    name_entry.pack(pady=5)

    # Address Line 1
    address1_label = tk.Label(
        client_window,
        text="Address Line 1"
    )
    address1_label.pack()

    address1_entry = tk.Entry(
        client_window,
        width=35
    )
    address1_entry.pack(pady=5)

    # Address Line 2
    address2_label = tk.Label(
        client_window,
        text="Address Line 2"
    )
    address2_label.pack()

    address2_entry = tk.Entry(
        client_window,
        width=35
    )
    address2_entry.pack(pady=5)

    # Address Line 3
    address3_label = tk.Label(
        client_window,
        text="Address Line 3"
    )
    address3_label.pack()

    address3_entry = tk.Entry(
        client_window,
        width=35
    )
    address3_entry.pack(pady=5)

    # City
    city_label = tk.Label(
        client_window,
        text="City"
    )
    city_label.pack()

    city_entry = tk.Entry(
        client_window,
        width=35
    )
    city_entry.pack(pady=5)

    # State
    state_label = tk.Label(
        client_window,
        text="State"
    )
    state_label.pack()

    state_entry = tk.Entry(
        client_window,
        width=35
    )
    state_entry.pack(pady=5)

    # Zip Code
    zip_label = tk.Label(
        client_window,
        text="Zip Code"
    )
    zip_label.pack()

    zip_entry = tk.Entry(
        client_window,
        width=35
    )
    zip_entry.pack(pady=5)

    # Country
    country_label = tk.Label(
        client_window,
        text="Country"
    )
    country_label.pack()

    country_entry = tk.Entry(
        client_window,
        width=35
    )
    country_entry.pack(pady=5)

    # Phone Number
    phone_label = tk.Label(
        client_window,
        text="Phone Number"
    )
    phone_label.pack()

    phone_entry = tk.Entry(
        client_window,
        width=35
    )
    phone_entry.pack(pady=5)

    def create_client():
        client_id = id_entry.get()
        name = name_entry.get()
        address1 = address1_entry.get()
        address2 = address2_entry.get()
        address3 = address3_entry.get()
        city = city_entry.get()
        state = state_entry.get()
        zip_code = zip_entry.get()
        country = country_entry.get()
        phone = phone_entry.get()

        # Check Client ID
        if client_id == "":
            messagebox.showerror(
                "Input Error",
                "Please enter a Client ID."
            )
            return

        # Check that Client ID is a number
        if not client_id.isdigit():
            messagebox.showerror(
                "Input Error",
                "Client ID must be a number."
            )
            return

        # Check that a name was entered
        if name == "":
            messagebox.showerror(
                "Input Error",
                "Please enter the client's name."
            )
            return

        # Create the client record
        client_record = {
            "ID": int(client_id),
            "Type": "Client",
            "Name": name,
            "Address Line 1": address1,
            "Address Line 2": address2,
            "Address Line 3": address3,
            "City": city,
            "State": state,
            "Zip Code": zip_code,
            "Country": country,
            "Phone Number": phone
        }

        # Add the record to the list
        client_records.append(client_record)

        messagebox.showinfo(
            "Client Created",
            "Client record created successfully."
        )

    def search_client():
        client_id = id_entry.get()

        # Check that an ID was entered
        if client_id == "":
          messagebox.showerror(
            "Input Error",
            "Please enter a Client ID."
        )
          return

        # Check that the ID is a number
        if not client_id.isdigit():
          messagebox.showerror(
            "Input Error",
            "Client ID must be a number."
        )
          return

         # Search through the client records
        for record in client_records:
          if record["ID"] == int(client_id):

            # Clear the current fields
            name_entry.delete(0, tk.END)
            address1_entry.delete(0, tk.END)
            address2_entry.delete(0, tk.END)
            address3_entry.delete(0, tk.END)
            city_entry.delete(0, tk.END)
            state_entry.delete(0, tk.END)
            zip_entry.delete(0, tk.END)
            country_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)

            # Display the stored client information
            name_entry.insert(0, record["Name"])
            address1_entry.insert(0, record["Address Line 1"])
            address2_entry.insert(0, record["Address Line 2"])
            address3_entry.insert(0, record["Address Line 3"])
            city_entry.insert(0, record["City"])
            state_entry.insert(0, record["State"])
            zip_entry.insert(0, record["Zip Code"])
            country_entry.insert(0, record["Country"])
            phone_entry.insert(0, record["Phone Number"])

            return

         # If no record was found
        messagebox.showerror(
         "Not Found",
         "Client record not found."
        )

    def update_client():
        client_id = id_entry.get()
         # Check Client ID
        if client_id == "":
          messagebox.showerror(
            "Input Error",
            "Please enter a Client ID."
        )
          return

        if not client_id.isdigit():
          messagebox.showerror(
            "Input Error",
            "Client ID must be a number."
        )
          return

        # Get the current values from the form
        name = name_entry.get()
        address1 = address1_entry.get()
        address2 = address2_entry.get()
        address3 = address3_entry.get()
        city = city_entry.get()
        state = state_entry.get()
        zip_code = zip_entry.get()
        country = country_entry.get()
        phone = phone_entry.get()

      # Search for the client
        for record in client_records:
          if record["ID"] == int(client_id):

            record["Name"] = name
            record["Address Line 1"] = address1
            record["Address Line 2"] = address2
            record["Address Line 3"] = address3
            record["City"] = city
            record["State"] = state
            record["Zip Code"] = zip_code
            record["Country"] = country
            record["Phone Number"] = phone

            messagebox.showinfo(
                "Client Updated",
                "Client record updated successfully."
            )

            return

        messagebox.showerror(
          "Not Found",
          "Client record not found."
        )

    def delete_client():
        client_id = id_entry.get()

         # Check that an ID was entered
        if client_id == "":
          messagebox.showerror(
            "Input Error",
            "Please enter a Client ID."
          )
          return

         # Check that the ID is a number
        if not client_id.isdigit():
          messagebox.showerror(
            "Input Error",
            "Client ID must be a number."
          )
          return

         # Search for the client record
        for record in client_records:
          if record["ID"] == int(client_id):

            confirm = messagebox.askyesno(
                "Confirm Delete",
                "Are you sure you want to delete this client record?"
            )

            if confirm:
                client_records.remove(record)

                messagebox.showinfo(
                    "Client Deleted",
                    "Client record deleted successfully."
                )

                # Clear all fields
                id_entry.delete(0, tk.END)
                name_entry.delete(0, tk.END)
                address1_entry.delete(0, tk.END)
                address2_entry.delete(0, tk.END)
                address3_entry.delete(0, tk.END)
                city_entry.delete(0, tk.END)
                state_entry.delete(0, tk.END)
                zip_entry.delete(0, tk.END)
                country_entry.delete(0, tk.END)
                phone_entry.delete(0, tk.END)

                return

        messagebox.showerror(
          "Not Found",
          "Client record not found."
        )
    # Frame for action buttons
    button_frame = tk.Frame(client_window)
    button_frame.pack(pady=20)

    create_button = tk.Button(
        button_frame,
        text="Create",
        width=10,
        command=create_client
    )
    create_button.pack(side="left", padx=5)

    search_button = tk.Button(
        button_frame,
        text="Search",
        width=10,
        command=search_client
    )
    search_button.pack(side="left", padx=5)

    update_button = tk.Button(
        button_frame,
        text="Update",
        width=10,
        command=update_client
    )
    update_button.pack(side="left", padx=5)

    delete_button = tk.Button(
        button_frame,
        text="Delete",
        width=10,
        command=delete_client
    )
    delete_button.pack(side="left", padx=5)

    # Back button
    back_button = tk.Button(
        client_window,
        text="Back",
        width=15,
        command=client_window.destroy
    )
    back_button.pack(pady=20)

def open_flight_window():
    # Create a new window
    flight_window = tk.Toplevel(root)

    # Set the window title and size
    flight_window.title("Flight Records")
    flight_window.geometry("500x550")

    # Page title
    title_label = tk.Label(
        flight_window,
        text="Flight Records",
        font=("Arial", 18)
    )
    title_label.pack(pady=20)

     # Flight ID (separate Flight_ID is the cleaner option)
    flight_id_label = tk.Label(
    flight_window,
    text="Flight ID"
    )
    flight_id_label.pack()

    flight_id_entry = tk.Entry(
    flight_window,
    width=30
 )
    flight_id_entry.pack(pady=5)

    # Client ID
    client_id_label = tk.Label(
        flight_window,
        text="Client ID"
    )
    client_id_label.pack()

    client_id_entry = tk.Entry(
        flight_window,
        width=30
    )
    client_id_entry.pack(pady=5)

    # Airline ID
    airline_id_label = tk.Label(
        flight_window,
        text="Airline ID"
    )
    airline_id_label.pack()

    airline_id_entry = tk.Entry(
        flight_window,
        width=30
    )
    airline_id_entry.pack(pady=5)

    # Date and Time
    date_label = tk.Label(
        flight_window,
        text="Date / Time"
    )
    date_label.pack()

    date_entry = tk.Entry(
        flight_window,
        width=30
    )
    date_entry.pack(pady=5)

    # Start City
    start_city_label = tk.Label(
        flight_window,
        text="Start City"
    )
    start_city_label.pack()

    start_city_entry = tk.Entry(
        flight_window,
        width=30
    )
    start_city_entry.pack(pady=5)

    # End City
    end_city_label = tk.Label(
        flight_window,
        text="End City"
    )
    end_city_label.pack()

    end_city_entry = tk.Entry(
        flight_window,
        width=30
    )
    end_city_entry.pack(pady=5)

    def create_flight():
        flight_id = flight_id_entry.get()
        client_id = client_id_entry.get()
        airline_id = airline_id_entry.get()
        date_time = date_entry.get()
        start_city = start_city_entry.get()
        end_city = end_city_entry.get()

         # Check that all fields are completed
        if (
            flight_id == ""
            or client_id == ""
            or airline_id == ""
            or date_time == ""
            or start_city == ""
            or end_city == ""
           ):
         messagebox.showerror(
            "Input Error",
            "Please complete all fields."
           )
         return

        # Check that Flight ID is a number
        if not flight_id.isdigit():
         messagebox.showerror(
          "Input Error",
          "Flight ID must be a number."
         )
         return
        
        # Check that Client ID is a number
        if not client_id.isdigit():
          messagebox.showerror(
            "Input Error",
            "Client ID must be a number."
          )
          return

         # Check that Airline ID is a number
        if not airline_id.isdigit():
          messagebox.showerror(
            "Input Error",
            "Airline ID must be a number."
          )
          return
         # Check that the Client ID exists
        client_exists = False

        for record in client_records:
          if record["ID"] == int(client_id):
            client_exists = True
            break

        if not client_exists:
            messagebox.showerror(
             "Client Not Found",
             "The Client ID does not exist."
            )
            return


         # Check that the Airline ID exists
        airline_exists = False

        for record in airline_records:
          if record["ID"] == int(airline_id):
            airline_exists = True
            break

        if not airline_exists:
            messagebox.showerror(
             "Airline Not Found",
             "The Airline ID does not exist."
            )
            return
        # Check that Flight ID is unique
        for record in flight_records:
            if record["Flight_ID"] == int(flight_id):
               messagebox.showerror(
                 "Duplicate Flight ID",
                 "This Flight ID already exists."
                )
               return
        
         # Create the flight record
        flight_record = {
          "Flight_ID": int(flight_id),
          "Client_ID": int(client_id),
          "Airline_ID": int(airline_id),
          "Date": date_time,
          "Start City": start_city,
          "End City": end_city
         }

         # Add the record to the list
        flight_records.append(flight_record)

        messagebox.showinfo(
          "Flight Created",
          "Flight record created successfully."
       )


    def search_flight():
        flight_id = flight_id_entry.get()

    # Check that a Flight ID was entered
        if flight_id == "":
            messagebox.showerror(
             "Input Error",
             "Please enter a Flight ID."
             )
            return

         # Check that Flight ID is a number
        if not flight_id.isdigit():
             messagebox.showerror(
             "Input Error",
             "Flight ID must be a number."
             )
             return

         # Search through the flight records
        for record in flight_records:
             if record["Flight_ID"] == int(flight_id):

                 # Clear the current fields
                 client_id_entry.delete(0, tk.END)
                 airline_id_entry.delete(0, tk.END)
                 date_entry.delete(0, tk.END)
                 start_city_entry.delete(0, tk.END)
                 end_city_entry.delete(0, tk.END)

                  # Display the stored flight information
                 client_id_entry.insert(0, record["Client_ID"])
                 airline_id_entry.insert(0, record["Airline_ID"])
                 date_entry.insert(0, record["Date"])
                 start_city_entry.insert(0, record["Start City"])
                 end_city_entry.insert(0, record["End City"])

                 return

         # If no matching flight was found
        messagebox.showerror(
             "Not Found",
             "Flight record not found."
        )


    def update_flight():
         flight_id = flight_id_entry.get()
         client_id = client_id_entry.get()
         airline_id = airline_id_entry.get()
         date_time = date_entry.get()
         start_city = start_city_entry.get()
         end_city = end_city_entry.get()

         # Check that all fields are completed
         if (
             flight_id == ""
             or client_id == ""
             or airline_id == ""
             or date_time == ""
             or start_city == ""
             or end_city == ""
            ):
             messagebox.showerror(
                 "Input Error",
                 "Please complete all fields."
             )
             return

    # Check that IDs are numbers
         if not flight_id.isdigit():
             messagebox.showerror(
                 "Input Error",
                 "Flight ID must be a number."
             )
             return

         if not client_id.isdigit():
             messagebox.showerror(
                 "Input Error",
                 "Client ID must be a number."
             )
             return

         if not airline_id.isdigit():
             messagebox.showerror(
                 "Input Error",
                 "Airline ID must be a number."
             )
             return

         # Check that Client ID exists
         client_exists = False

         for record in client_records:
             if record["ID"] == int(client_id):
                 client_exists = True
                 break

         if not client_exists:
             messagebox.showerror(
                 "Client Not Found",
                 "The Client ID does not exist."
             )
             return

         # Check that Airline ID exists
         airline_exists = False

         for record in airline_records:
             if record["ID"] == int(airline_id):
                 airline_exists = True
                 break

         if not airline_exists:
             messagebox.showerror(
                 "Airline Not Found",
                 "The Airline ID does not exist."
             ) 
             return

    # Search for the flight
         for record in flight_records:
             if record["Flight_ID"] == int(flight_id):

                 record["Client_ID"] = int(client_id)
                 record["Airline_ID"] = int(airline_id)
                 record["Date"] = date_time
                 record["Start City"] = start_city
                 record["End City"] = end_city

                 messagebox.showinfo(
                     "Flight Updated",
                     "Flight record updated successfully."
                 )

                 return

         messagebox.showerror(
             "Not Found",
             "Flight record not found."
         )

    def delete_flight():
         flight_id = flight_id_entry.get()

         # Check that a Flight ID was entered
         if flight_id == "":
             messagebox.showerror(
                 "Input Error",
                 "Please enter a Flight ID."
             )
             return

         # Check that Flight ID is a number
         if not flight_id.isdigit():
             messagebox.showerror(
                 "Input Error",
                 "Flight ID must be a number."
             )
             return

         # Search for the flight record
         for record in flight_records:
             if record["Flight_ID"] == int(flight_id):

                 # Ask for confirmation
                 confirm = messagebox.askyesno(
                     "Confirm Delete",
                     "Are you sure you want to delete this flight record?"
                     )

                 if confirm:
                     flight_records.remove(record)

                     messagebox.showinfo(
                         "Flight Deleted",
                         "Flight record deleted successfully."
                     )

                     # Clear all fields
                     flight_id_entry.delete(0, tk.END)
                     client_id_entry.delete(0, tk.END)
                     airline_id_entry.delete(0, tk.END)
                     date_entry.delete(0, tk.END)
                     start_city_entry.delete(0, tk.END)
                     end_city_entry.delete(0, tk.END)

                     return

         # If the Flight ID was not found
         messagebox.showerror(
             "Not Found",
             "Flight record not found."
        )
         
    # Frame for action buttons
    button_frame = tk.Frame(flight_window)
    button_frame.pack(pady=20)

    create_button = tk.Button(
        button_frame,
        text="Create",
        width=10,
        command=create_flight
    )
    create_button.pack(side="left", padx=5)

    search_button = tk.Button(
        button_frame,
        text="Search",
        width=10,
        command=search_flight
    )
    search_button.pack(side="left", padx=5)

    update_button = tk.Button(
        button_frame,
        text="Update",
        width=10,
        command=update_flight
    )
    update_button.pack(side="left", padx=5)

    delete_button = tk.Button(
        button_frame,
        text="Delete",
        width=10,
        command=delete_flight
    )
    delete_button.pack(side="left", padx=5)

    # Back button
    back_button = tk.Button(
        flight_window,
        text="Back",
        width=15,
        command=flight_window.destroy
    )
    back_button.pack(pady=20)

title_Label=tk.Label(root,
                     text="Travel Record Management System",
                    font=("Arial",18)
)
title_Label.pack(pady=30)



clients_button=tk.Button(root, 
                          text="Manage Clients", 
                          width=20,
                           command=open_client_window)
clients_button.pack(pady=10)


flights_button=tk.Button(root,
                         text="Manage Flights",
                         width=20,
                         command=open_flight_window)
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