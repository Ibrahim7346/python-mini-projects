def check_phishing_url(url):
    suspicious = []

    # check for HTTPS
    if not url.startswith("https://"):
        suspicious.append("URL does not use HTTPS")

    # check for @ symbol
    if "@" in url:
        suspicious.append("Contains @ symbol")

    # check for IP address
    parts = url.replace("https://", "").replace("http://", "").split("/")[0]

    if all(part.isdigit() for part in parts.split(".") if part):
        suspicious.append("Uses an IP address instead of a domain")

    #check for hyphens
    if "-" in parts:
        suspicious.append("Contains hyphen in domain")

    #result
    if suspicious:
        print("\n Potentially Suspicious URl")
        for item in suspicious:
            print("-", item)
    else:
        print("\n URL appears safer")


url = input("Enter a URL: ")
check_phishing_url(url)                            