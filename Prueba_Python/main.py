import requests
from jinja2 import Template

def fetch_birds_data():
    url = 'https://aves.ninjas.cl/api/birds'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def generate_html(birds_data):
    with open('template.html', 'r') as file:
        template_content = file.read()
        template = Template(template_content)

        bird_entries = []
        for bird in birds_data:
            bird_name_es = bird['name']['spanish']
            bird_name_en = bird['name']['english']
            bird_image_url = bird['images']['main']

            bird_entries.append({
                'nameSpanish': bird_name_es,
                'nameEnglish': bird_name_en,
                'imageUrl': bird_image_url
            })

        rendered_html = template.render(bird_entries=bird_entries)

        with open('aves_de_chile.html', 'w') as output_file:
            output_file.write(rendered_html)


def main():
    birds_data = fetch_birds_data()
    if birds_data:
        generate_html(birds_data)
        print("Sitio creado con éxito como 'aves_de_chile.html'")
    else:
        print("No se pudo obtener datos de la API.")

if __name__ == "__main__":
    main()
