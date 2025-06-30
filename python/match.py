# Function to read file and return a set of lines
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return set(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return set()

# Function to find matched values
def find_matched_values(file1, file2):
    set1 = read_file(file1)
    set2 = read_file(file2)
    
    matched_values = set1.intersection(set2)
    
    return matched_values

# Example usage
if __name__ == "__main__":
    file1 = "outindex.txt"  # Replace with actual file path
    file2 = "active.txt"  # Replace with actual file path
    
    matches = find_matched_values(file1, file2)
    
    if matches:
        print("Matched Values:")
        for match in matches:
            print(match)
    else:
        print("No matched values found.")
