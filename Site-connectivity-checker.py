import urllib.request as urllib


def main(url):
    print("Checking connectivity... ")
    
    response = urllib.urlopen(url)
    print("connected to" , url ,"successfully")
    print("The response code was: ", response.getcode())

print("This a site connectivity checker program")
input_url = input("input the url of the site you want to check: ")

main(input_url)

