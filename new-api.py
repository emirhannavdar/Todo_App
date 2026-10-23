def api_exmp(name: str):
    return f"Hello {name}"

@api.get("/emir-1")
def main_one():
    return api_exmp("Emirhan")

@api.get("/emir-2")
def main_two():
    return api_exmp("Emirhan")