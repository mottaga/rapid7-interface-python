def print_json(json_data : dict) -> None:
    json_data = str(json_data).replace(" ", "")
    
    # Indentation settings
    indentation_level = 0
    indentation_increment = 4
    
    # Inside strings change the behaviour of the parser
    is_string = False

    # Loop through all the string
    for index, char in enumerate(json_data):
        # Check if we are inside of a string
        if char == "'" and is_string:
            is_string = False
        
        elif char == "'" and (not is_string):
            is_string = True
        
        # Print
        if is_string:
            print(char, end = "")

        elif char == ":":
            print(" : ", end = "")
        
        elif char == "{":
            if (index + 1 < len(json_data)) and (json_data[index + 1] != "}"): 
                indentation_level += indentation_increment
                print("{")
                print(" " * indentation_level, end = "")
            
            else:
                print("{", end = "")
        
        elif char == "[":
            if (index + 1 < len(json_data)) and (json_data[index + 1] != "]"):
                indentation_level += indentation_increment
                print("[")
                print(" " * indentation_level, end = "")

            else:
                print("[", end = "")
        
        elif char == "}":
            if (index - 1 > 0) and (json_data[index - 1] != "{"):
                indentation_level -= indentation_increment
                print(f"\n{' ' * indentation_level}", end = "")

            print("}", end = "")
        
        elif char == "]":
            if (index - 1 > 0) and (json_data[index - 1] != "["):
                indentation_level -= indentation_increment
                print(f"\n{' ' * indentation_level}", end = "")

            print("]", end = "")
        
        elif char == ",":
            print(",")
            print(" " * indentation_level, end = "")
        
        else:
            print(char, end = "")
    
    print()
