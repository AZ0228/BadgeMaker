def getTerminalInput():
    ret = {} #stores inputs
    mainColor = input("Enter main color (hex codes must not have #): ").strip()
    iconColor = input("Enter icon color (hex codes must not have #): ").strip()
    while True:
        badgeContent = input("Enter badge content: ")
        iconName = input("Enter icon name: ")
        ret[badgeContent] = iconName
        if input("Enter another badge? (y/n): ").strip() == "n":
            break
    return ret, mainColor, iconColor
        
def getFileInput(inputFile: str):
    ret = {}
    with open(inputFile, "r") as f:
        mainColor = f.readline().strip()
        iconColor = f.readline().strip()
        for line in f:
            line = line.strip().split(",")
            ret[line[0]] = line[1]
    return ret, mainColor, iconColor

def terminalOutput(output: list):
    for line in output:
        print(line)
        print("\n")

def fileOutput(outputFile: str, output: list):
    with open(outputFile, "w") as f:
        f.writelines("\n".join(output))
    print("output in file: " + outputFile)

def parseInput(input: dict, mainColor, iconColor) -> list:
    ret = []
    for badgeContent, iconName in input.items():
        ret.append(f"![Static Badge](https://img.shields.io/badge/%20-{badgeContent}-%23{mainColor}?logo={iconName}&logoColor=%23{iconColor})")
    return ret

if input == "none":
    pass

if __name__ == "__main__":
    inputFile = input("Enter input file, enter 'none' for terminal input: ")
    print("\n")
    outputFile = input("Enter output file, enter 'none' for terminal output: ")
    print("\n")
    if inputFile == "none":
        input, mainColor, iconColor = getTerminalInput()
    else:
        input, mainColor, iconColor = getFileInput(inputFile)
    output = parseInput(input, mainColor, iconColor)
    if outputFile == "none":
        terminalOutput(output)
    else:
        fileOutput(outputFile, output)


