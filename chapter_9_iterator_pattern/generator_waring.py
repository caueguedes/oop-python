import sys

#generator expression
inname, outname = sys.argv[1:3]

with open(inname) as infile:
    with open(outname), "w" as outfile:
        # for l in infile:
        #     if "WARNING" in l:
        #         outfile.write(l.replace("\tWARNING", ""))
        warnings = (l.replace("\tWARNING", "") for l in infile if "WARNING" in l)
        for l in warnings:
            outfile.write(l)


