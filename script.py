import os
import re

# Répertoire des fichiers SVG et de sortie
INPUT_DIR = "SVG"
OUTPUT_DIR = "JS"


# Fonction pour générer un composant React à partir d'un fichier SVG
def generate_react_component(svg_content, component_name):
    svg_content = re.sub(
        r'<svg[^>]*\bwidth="[^"]*"\s*height="[^"]*"',
        '<svg width="auto" height="100%"',
        svg_content,
        count=1  # Limite à un remplacement
    )
    svg_content = svg_content.replace('fill="#656461"', 'fill={color}')
    svg_content = svg_content.replace('clip-path', 'clipPath')
    svg_content = svg_content.replace('fill-rule', 'fillRule')
    svg_content = svg_content.replace('clip-rule', 'clipRule')

    # Template du composant React
    react_component = f"""
import React from 'react';

function {component_name}({{ color = '#1B1B1B' }}) {{
    return (
        {svg_content.strip()}
    );
}}

{component_name}.metadata = {{ tags: ["test", "test2"] }};

export default {component_name};
"""
    return react_component.strip()


# Fonction principale pour transformer tous les fichiers SVG
def transform_svgs(input_dir, output_dir):
    # Création du répertoire de sortie si inexistant
    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".svg"):
            input_path = os.path.join(input_dir, file_name)

            # Transformation du nom du fichier en format attendu
            base_name = os.path.splitext(file_name)[0]
            component_name = "".join(
                word.capitalize() for word in base_name.split("-")
            )  # PascalCase pour la fonction
            output_file_name = f"{base_name}.js"

            output_file = os.path.join(output_dir, output_file_name)

            # Lecture du fichier SVG
            with open(input_path, "r", encoding="utf-8") as svg_file:
                svg_content = svg_file.read()

            # Transformation en composant React
            react_component = generate_react_component(svg_content,
                                                       component_name)

            # Sauvegarde du fichier .js
            with open(output_file, "w", encoding="utf-8") as js_file:
                js_file.write(react_component)

            print(f"Transformé : {file_name} -> {output_file_name}")


# Exécution
if __name__ == "__main__":
    transform_svgs(INPUT_DIR, OUTPUT_DIR)
