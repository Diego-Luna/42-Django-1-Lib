import sys
import requests
from bs4 import BeautifulSoup

def get_wikipedia_page(title):
    # *Obtener contenido de la página de Wikipedia y manejar redirecciones.
    base_url = "https://en.wikipedia.org/wiki/"
    try:
        # * Hacer la solicitud con seguimiento de redirecciones
        response = requests.get(base_url + title.replace(' ', '_'), allow_redirects=True)
        response.raise_for_status()

        # * Extraer el título final después de la redirección
        soup = BeautifulSoup(response.text, 'html.parser')
        canonical_link = soup.find("link", {"rel": "canonical"})
        if canonical_link:
            redirected_title = canonical_link['href'].split('/wiki/')[-1].replace('_', ' ')
            return response.text, redirected_title

        # * Si no se encuentra enlace canónico, usar el título de la página
        page_title = soup.find("h1", {"id": "firstHeading"})
        if page_title:
            return response.text, page_title.text

        # * Si todo falla, devolver el título original
        return response.text, title

    except requests.RequestException as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def is_valid_link(link):
    if not link.get('href', '').startswith('/wiki/'):
        return False
        
    # ! Excluir páginas especiales y secciones
    excludes = [
        'Wikipedia:', 'File:', 'Special:',
        'Help:', 'Category:', 'Portal:', 
        'Template:', '#', 'wikt:', 'Book:',
        'Talk:', 'Media:', 'User:'
    ]
    
    href = link.get('href', '')
    title = link.get('title', '')
    
    if any(ex in href for ex in excludes) or any(ex in title for ex in excludes):
        return False

    # ! Verificar si está dentro de paréntesis
    parent = link.parent
    if not parent:
        return False

    # ! Contar paréntesis en el texto anterior
    prev_text = ''.join(str(s) for s in link.find_previous_siblings(string=True))
    paren_count = prev_text.count('(') - prev_text.count(')')
    if paren_count > 0:
        return False

    # ! Verificar si está en itálicas o citas
    if any(parent.find_parent(tag) for tag in ['i', 'em', 'cite']):
        return False

    return True

def find_first_valid_link(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    content = soup.find(id="mw-content-text")
    if not content:
        return None

    # * Encontrar el contenido principal
    main_content = content.find('div', class_='mw-parser-output')
    if not main_content:
        return None

    for element in main_content.children:
        # * Saltar elementos que no sean párrafos o párrafos vacíos
        if element.name != 'p' or not element.text.strip():
            continue
        # * Saltar párrafos que contienen solo coordenadas o imágenes
        if element.find(class_="geo-nondefault") or element.find(class_="metadata"):
            continue
            
        # ? Encontrar todos los enlaces en este párrafo
        for link in element.find_all('a', recursive=True):
            if is_valid_link(link):
                return link.get('title')
    return None

def roads_to_philosophy(start_page):
    visited = []
    current_page = start_page
    
    while True:
        # * Obtener el contenido de la página y el título real (después de redirecciones)
        html, actual_title = get_wikipedia_page(current_page)
        print(actual_title)  # Mostrar el título real
        
        #  * comparaciones con minusculas
        title_lower = actual_title.lower()
        visited.append(title_lower)
        
        # * Caso especial para "Program"
        if title_lower == "program":
            current_page = "Programming_language"
            continue

        # *Encontrar el primer enlace válido
        next_link = find_first_valid_link(html)
        
        if not next_link:
            print("It leads to a dead end !")
            return
            
        # * Comprobar si hemos llegado a Filosofía
        if next_link.lower() == 'philosophy':
            print('Philosophy')
            print(f"{len(visited) + 1} roads from {start_page.replace('_', ' ')} to philosophy !")
            return
            
        # * Comprobar si debemos estar en el bucle
        if next_link.lower() in visited:
            print("It leads to an infinite loop !")
            return
            
        current_page = next_link

def main():
    if len(sys.argv) != 2:
        print(" ✋ Usage: python3 roads_to_philosophy.py \"Search Term\" 😎")
        sys.exit(1)
        
    roads_to_philosophy(sys.argv[1])

if __name__ == '__main__':
    main()
