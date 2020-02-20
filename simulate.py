class Running:
    currentProcessing = None  # The current library being processed
    daysLeft = 0  # How many days are left for the current library to be processed
    librariesLeft = []  # The libraries still to be processed
    processed = []  # Librarues that have been processed
    numberProcessed = 0
    totalScore = 0  # The total score


outputFile = open("output.txt", "w")  # create output file


def simulate(libraries, D):
    # ASSUMPTION: libraries is already sorted from best to worst
    Running.librariesLeft = libraries
    libForOutput = []  # list of LibrarySection objects -- used for building output

    for d in range(D):
        # Stuff for processing libraries
        if Running.daysLeft <= 0 and len(Running.librariesLeft) > 0:
            # Add next library
            if Running.currentProcessing is not None:
                Running.processed.append(Running.currentProcessing)
            Running.numberProcessed += 1

            libForOutput.append(Running.currentProcessing)  # add this libr to the list of output sections

            Running.currentProcessing = Running.librariesLeft.pop(0)
            Running.daysLeft = Running.currentProcessing.signupTime

        # Stuff for processing books
        for l in Running.processed:
            for i in range(l.nShipPerDay):
                if len(l.books) > 0:
                    popped = l.books.pop()
                    l.scanned.append(popped)
                    Running.totalScore += popped.score

        # Decrement the days left for the current library
        Running.daysLeft -= 1

    # adding data into output file
    outputFile.write("%d".format(len(Running.processed)))  # add nº of libraries processed
    # add section for each library int the output file
    for lib in libForOutput:
        line1 = "%d %d".format(lib.idx, len(lib.scanned))
        line2 = ""

        for thisBook in lib.scanned:
            line2 = line2 + "%d ".format(thisBook.idf)

        outputFile.write(line1)
        outputFile.write(line2)
