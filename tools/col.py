infotypes = ("Name", "Age", "City")
credentials = ("Omer", "22", "Ramat gan")

def zipfunction(infotypes,credentials):
    x = zip(infotypes, credentials)

    print(tuple(x))

zipfunction(infotypes,credentials)
