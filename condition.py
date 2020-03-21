#Python feature is that the whitespace indentation of a piece of code affects its meaning.
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s + s + s # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!'
    return result

def main():
	name=sys.argv[1]
    if name =="Guido":
        print (repeeeet(name) + '!!!')
    else:
        print (repeat(name))

if __name__== "__main__":
   main()