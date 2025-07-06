def tools(input_text: str) -> str:
    if "create file" in input_text:
        with open("generated.txt", "w") as f:
            f.write("This is a new file created by Solyn.")
        return "File created: generated.txt"
    return "No tool used."
