def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Characters to look for to add new lines after
    special_chars = ['.', '?', ':']
    
    # Initialize an empty string to hold the modified text
    new_text = ""
    
    # Iterate through each character in the text
    i = 0
    while i < len(text):
        new_text += text[i]
        if text[i] in special_chars:
            new_text += "\n\n"
            # Skip any following spaces after the special character
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1

    # Print the result, removing any leading/trailing spaces from each line
    print("\n".join(line.strip() for line in new_text.split("\n")))

# Example usage:
text_indentation("Hello. How are you? I hope you are well: stay safe.")
