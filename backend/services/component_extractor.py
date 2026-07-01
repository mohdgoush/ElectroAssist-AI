import re


def extract_components(text: str):

    components = []

    lines = text.splitlines()

    inside_components = False

    for line in lines:

        line = line.strip()

        if line.startswith("COMPONENTS"):
            inside_components = True
            continue

        if line.startswith("CIRCUIT_TYPE"):
            break

        if inside_components and line.startswith("-"):

            components.append(
                line.replace("-", "").strip()
            )

    return components