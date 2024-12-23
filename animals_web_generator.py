import data_fetcher

def generate_website(data, file_name="animals_template.html"):
    with open(file_name, "w") as file:
        file.write("<html><body>")
        if data:
            for animal in data:
                file.write(f"<h1>{animal.get('name')}</h1>")
                file.write(f"<p>Taxonomy: {animal.get('taxonomy')}</p>")
                file.write(f"<p>Locations: {', '.join(animal.get('locations', []))}</p>")
                file.write(f"<p>Characteristics: {animal.get('characteristics')}</p>")
        else:
            file.write("<h2>No animals found matching the given name.</h2>")
        file.write("</body></html>")
    print(f"Website was successfully generated to the file {file_name}.")

def main():
    animal_name = input("Please enter an animal: ")
    try:
        data = data_fetcher.fetch_data(animal_name)
        generate_website(data)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
