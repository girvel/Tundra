def request_choice_index(variants, input_line=input, print=print, enumeration_start=1, ):
    print()
    for i, variant in enumerate(variants):
        print(f'{i + enumeration_start}. {variant}')

    while True:
        choice = input_line()

        if choice.isdigit():
            choice = int(choice) - enumeration_start
            if 0 <= choice < len(variants):
                break

    print()
    return choice


def request_choice(variants, input_line=input, print=print, enumeration_start=1):
    return variants[request_choice_index(variants, input_line, print, enumeration_start)]
