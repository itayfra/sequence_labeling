def process_conll2003_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # If it's a blank line, keep it in the output
            if line.strip() == "":
                outfile.write("\n")
            else:
                # Split the line into columns
                columns = line.strip().split()

                # Extract the 1st and 4th columns (token and named entity tag)
                token = columns[0]
                ner_tag = columns[3]

                # Write to the output file
                outfile.write(f"{token} {ner_tag}\n")


# Example usage:
input_file = "data/coNLL/eng/eng.train.iob"  # Replace with your input file name
output_file = "data/coNLL/eng/eng.train2.iob"  # Replace with your output file name

process_conll2003_file(input_file, output_file)
