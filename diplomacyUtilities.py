from collections import OrderedDict

def returnOrderedDict(the_dict):
    return OrderedDict(sorted(the_dict.items()))

def makeSortedStringRepOfDict(the_dict):
    return '\n'.join(map(str, returnOrderedDict(the_dict).values()))



def main ():
    print('diplomacyUtilities is main')



if __name__ == "__main__":
    main ()
