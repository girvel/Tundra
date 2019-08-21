def request_choice_index(variants, input_line=input, print=print, enumeration_start=1, ):
    print()
    variants = [v if not isinstance(v, tuple) else (v[1] if v[0] else None) for v in variants]
    output_variants = [v for v in variants if v is not None]

    for i, variant in enumerate(output_variants):
        print(f'{i + enumeration_start}. {variant}')

    while True:
        choice = input_line()

        if choice.isdigit():
            choice = int(choice) - enumeration_start
            if 0 <= choice < len(output_variants):
                choice = output_variants[choice]
                break

    print()
    return variants.index(choice)


def request_choice(variants, input_line=input, print=print, enumeration_start=1):
    return variants[request_choice_index(variants, input_line, print, enumeration_start)]
