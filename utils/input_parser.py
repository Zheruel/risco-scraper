def parse_string_input(path: str) -> list[str]:
    unfiltered_input = open(path, "r")
    input_string_list = unfiltered_input.read().splitlines()
    unfiltered_input.close()

    return input_string_list
