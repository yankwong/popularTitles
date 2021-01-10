import language


def prompt_for_keyword() -> str:
    return input(language.ASK_FOR_KEYWORD)


def prompt_for_page() -> int:
    return int(input(language.ASK_FOR_TOTAL_PAGE))


def print_loading_msg() -> None:
    print(language.PROCESSING_DATA)


def print_done_msg() -> None:
    print(language.DONE_PROCESSING)
