import nltk

## Match any of the nasalized letters in Guarani or the glottal stop.
## the ones listed explicitly can be represented as their own unicode
## characters; we also consider the special unicode character for
## combining-tilde, which is the way to get '̃g' and could occur in other places
## too if the unicode isn't as normalized as we would like.
special_gn = "ÃẼĨÑÕŨỸ'ãẽĩñõũỹ\u0303"

def gn_tokenizer():
    letters = "{0}\\w".format(special_gn)
    pattern = "[{0}]+|[^{0}\\s]+".format(letters)
    print(pattern)
    return nltk.RegexpTokenizer(pattern)

def main():
    tokenizer = gn_tokenizer()
    text = "Pe kuru okakuaave ramo, pa'i he'i rire pe tapicha ipotĩha, \
            toho jey pa'i rendápe oma'ẽ haguã hese."
    print(tokenizer.tokenize(text))

if __name__ == "__main__": main()
