def api_exmp(name: str):
    return f"Hello {name}"

@api_exmp("Emir")
def main():
    print(api_exmp("Emir"))
