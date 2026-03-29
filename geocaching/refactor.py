import sys
# ----------------------------
# Main script
# ----------------------------
if __name__ == "__main__":
    
    # try:
        # input = sys.argv[1]
        
        # if input == "x":
            # print("Null input. One sentence is required.")
            # exit
    # except ValueError:
        # print("Invalid argument. Must be a single string.")
        # exit 
        
    input = r"C:\Users\alexd\Documents\repos\refactor_text.txt"
    
    with open(input, "r", encoding="utf-8") as f:
        content = f.read()
   
    print("---- input: ----")
    print(content)
    print("------------------------------") 
    
    input_array = list(content)
    final_string = "N"
    
    for c in input_array:
        if c.isnumeric():
            final_string = final_string + c
            
            if len(final_string) == 3:
                final_string = final_string + " "
            elif len(final_string) == 6:
                final_string = final_string + "."
            elif len(final_string) == 10:
                final_string = final_string + " W"
            elif len(final_string) == 15:
                final_string = final_string + " "
            elif len(final_string) == 18:
                final_string = final_string + "."
 
    print("------------------------------")
    print("--- " + final_string + " ---")      
    print("------------------------------")    
    