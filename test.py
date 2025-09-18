def splitfile(inputfile,basename, num_files=4):
    with open(inputfile,"r") as f:
        lines = f.readlines()
    
    total_lines = len(lines)

    chunk_size = total_lines // num_files

    for i in range(num_files):
        start = i * chunk_size
        if i == num_files -1:
            end = total_lines
        else:
            end = start + chunk_size

        part = lines [start:end]
        if not part:
            continue

        output_file = f"{basename}_{i+1}"
        with open(output_file, "w") as output: