import urllib as urllib


def main(url):
    print("Checking connectivity")
    response = urllib.urlopen(url)
    print("Connect to", url, "successfully")
    print("The response code was:", response.getcode())


print("This is a site connectivity checker")
input_url = input("Input the URL of the site: ")


main(input_url)
