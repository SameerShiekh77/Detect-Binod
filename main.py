import os
# Creatig file reading function
def isBinod(filename):
    with open(filename, "r") as f:
        fileContent = f.read()
    if "binod" in fileContent.lower():
        return True
    else:
        return False

if __name__ == '__main__':
    dir_loc = os.listdir()
    # print(dir_loc)
    nbinod = 0
    for item in dir_loc:
        if(item.endswith('txt')):
            # File Deduction
            print(f"==========Deducting Binod in this file {item}==============")
            file = isBinod(item)
            # Founding Binod
            if(file):
                print(f"\t\tBinod found in {item}")
                nbinod += 1
            else:
                print(f"\t\tBinod not found in {item}")
    print("\n**************Binod Detect Summary***************")
    print(f"{nbinod} files found with Binod info hidden into item")