import sys
import json

# Validate input file is valide json file
def validate_json (inputFile):
    try:
        with open (inputFile) as f:
            json.load(f)
    except:
        return False
    return True

def main():
    if len(sys.argv) != 2:
        print("You must insert one file as an argument. Please try again.")
        exit(1)
    validJson = validate_json(sys.argv[1])
    print (validJson)
    

if __name__ == '__main__':
    main()