def compare_files(file1, file2, output_file): 
    # Read first file (full names)
    with open(file1, "r", encoding="utf-8") as f1:
        file1_lines = {line.strip() for line in f1}  # Convert to set for fast lookup

    # Read second file (partial names)
    with open(file2, "r", encoding="utf-8") as f2:
        file2_lines = {line.strip() for line in f2}

    # Find unmatched values from file1
    unmatched = [line for line in file1_lines if not any(part in line for part in file2_lines)]

    # Write unmatched values to output file
    with open(output_file, "w", encoding="utf-8") as out:
        out.write("\n".join(unmatched))

    print(f"✅ Unmatched values saved in {output_file}")


# File names (change as needed)
file1 = "index.txt"  # Contains full values (tenant-dev-drp1-siva, etc.)
file2 = "active.txt"  # Contains partial values (siva)
output_file = "outindex.txt"  # Output file

# Run comparison
compare_files(file1, file2, output_file)