import data_fetcher

def generate_website(data, file_name="animal_output.html"):
    # HTML template with placeholders for dynamic content
    template = """
    <html>
        <head>
            <title>Animal Details</title>
        </head>
        <body>
            <h1>Animal Details</h1>
            <table border="1">
                <tr>
                    <th>Attribute</th>
                    <th>Details</th>
                </tr>
                <tr>
                    <td>Name</td>
                    <td>{{name}}</td>
                </tr>
                <tr>
                    <td>Scientific Name</td>
                    <td>{{scientific_name}}</td>
                </tr>
                <tr>
                    <td>Diet</td>
                    <td>{{diet}}</td>
                </tr>
                <tr>
                    <td>Location</td>
                    <td>{{location}}</td>
                </tr>
                <tr>
                    <td>Lifespan</td>
                    <td>{{lifespan}}</td>
                </tr>
                <tr>
                    <td>Habitat</td>
                    <td>{{habitat}}</td>
                </tr>
                <tr>
                    <td>Type</td>
                    <td>{{type}}</td>
                </tr>
            </table>
        </body>
    </html>
    """

    # If data is not empty, replace placeholders with actual data
    if data:
        animal = data[0]  # Assuming the data contains a list, and we take the first animal entry

        # Access nested data and handle lists like "locations"
        scientific_name = animal.get('taxonomy', {}).get('scientific_name', 'Unknown')
        diet = animal.get('characteristics', {}).get('prey', 'Unknown')
        location = ', '.join(animal.get('locations', ['Unknown']))  # Handle list and join locations
        lifespan = 'Unknown'  # This field is not in the response, you can modify if necessary
        habitat = 'Unknown'  # Similar to lifespan, you can add this if data is available
        animal_type = animal.get('taxonomy', {}).get('class', 'Unknown')  # Assuming "class" is the type

        # Use .get() to safely access data and use default values if the data is missing
        html_output = template.replace("{{name}}", animal.get('name', 'Unknown'))
        html_output = html_output.replace("{{scientific_name}}", scientific_name)
        html_output = html_output.replace("{{diet}}", diet)
        html_output = html_output.replace("{{location}}", location)
        html_output = html_output.replace("{{lifespan}}", lifespan)
        html_output = html_output.replace("{{habitat}}", habitat)
        html_output = html_output.replace("{type}}", animal_type)

        # Write the output to the file
        with open(file_name, "w") as file:
            file.write(html_output)

        print(f"Website successfully generated and saved to {file_name}")

    else:
        print("No data found for the entered animal.")

def main():
    animal_name = input("Please enter an animal: ")
    try:
        # Fetch data using the fetch_data function from the data_fetcher module
        animal_data = data_fetcher.fetch_data(animal_name)

        # Print the full response to check the structure of the data
        print(f"Fetched data for {animal_name}: {animal_data}")

        # Check if data exists before passing it to the website generation function
        if animal_data:
            generate_website(animal_data)
        else:
            print("No data found for the entered animal.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
