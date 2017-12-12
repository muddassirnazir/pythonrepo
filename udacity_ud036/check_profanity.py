import urllib.request

def read_text():
    quotes = open(r"C:\Users\muddassir.nazir\Desktop\Udacity_Python\movie_quotes.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()
    check_profanity(contents)


def check_profanity(text_to_check):
    url = urllib.request.urlopen('http://www.wdylike.appspot.com/?q='+urllib.parse.quote(text_to_check))
    output = url.read()
#    print(output)
    url.close()
    if "true" in str(output):
        print("Profanity Alert")
    elif "false" in str(output):
        print("The file is clean")


read_text()
