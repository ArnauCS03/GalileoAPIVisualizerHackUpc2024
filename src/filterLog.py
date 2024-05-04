def filter_log(file_path):
    with open(file_path, 'r') as file:
        with open("../out/filtered.out", 'w') as filtered_file:
            for line in file:
                # Remove leading and trailing whitespace from the line
                values_line = line.split(',')

                if line.startswith("Fix"):  # only the GPS ones
                    if values_line[1] == "GPS":
                        filtered_file.write(line)

                elif line.startswith("Raw"):
                    if values_line[28] == "6":
                        filtered_file.write(line)

                elif line.startswith("Status"):  
                    if values_line[4] == "6":
                        filtered_file.write(line)


# Example usage:
file_path = "../logs/gnss_log_2024_05_04_03_38_42.txt" 
filter_log(file_path)
