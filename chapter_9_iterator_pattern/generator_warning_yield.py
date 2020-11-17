import sys
inname, outname = sys.argv[1:3]


def warnings_filter(insequence):
    for l in insequence:
        if "WARNING" in l:
            yield l.replace("\tWARNING", "")


with open(inname) as infile:
    with open(outname, "w") as outfile:
        filter = warnings_filter(infile)
        for l in filter:
            outfile.write(l)


print(warnings_filter([]))  # <generator object warnings_filter at 0xb728c6bc>


# yield from another iterator
def warnings_filter_from(infilename):
    with open(infilename) as infile:
        yield from (
            l.replace("\tWARNING", "") for l in infile if "WARNING" in l
        )


filter = warnings_filter_from(inname)
with open(outname, "w") as outfile:
    for l in filter:
        outfile.write(l)