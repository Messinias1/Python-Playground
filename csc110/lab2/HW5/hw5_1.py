
def getSpeeds():
    speedList = []
    inFile = open('groundhog.txt', 'r')
    line = inFile.readline()
    line = line.strip()

    while line != '':
        speed = line
        speedList.append(speed)
        line = inFile.readline()
        line = line.strip()

    inFile.close()

    return speedList


def main():
    print(getSpeeds())


main()