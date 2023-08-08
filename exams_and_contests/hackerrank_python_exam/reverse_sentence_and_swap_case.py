def reverse_words_order_and_swap_cases(sentence: str) -> str:
    sentence = list(map(lambda x: list(x), sentence.split(" ")))
    return " ".join(list(map(lambda word: "".join(list(map(lambda x: x.lower() if x.isupper() else x.upper(), word))), sentence))[::-1])

print(reverse_words_order_and_swap_cases("qw4 rLy aGaf"))
