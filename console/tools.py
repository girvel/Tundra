def request(string, input=input, print=print):
    print(f'{string}: ', end='')
    return input()


def request_choice_index(variants, input=input, print=print):
    print()
    for i, variant in enumerate(variants):
        print(f'{i + 1}. {variant}')

    while True:
        choice = input()

        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(variants):
                break

    print()
    return choice


def request_choice(variants, input=input, print=print):
    return variants[request_choice_index(variants, input, print)]
