from colorama import Back, Fore, Style


def check_for_assertion_error(func):
    """Adds a decorator to check to see if the code has been completed instead of returning unhelpful expection"""
    def wrapper_check_for_assertion_error(*args, **kwargs):
        self = args[0]
        try:
            func(*args, **kwargs)
            return func(*args, **kwargs)
        except AssertionError as ex:
            if "Expected a `Response`" in ex.args[0]:
                return self.fail(format_message("HINT: Complete the code for this test"))
            if 'missing "Meta"' in ex.args[0]:
                return self.fail(format_message("HINT: Remember to fill in the serializer code"))
            return func(*args, **kwargs)

    return wrapper_check_for_assertion_error


def format_message(message):
    """Make it easy to see hints in the terminal"""
    return Fore.BLACK + Back.LIGHTRED_EX + message + Style.RESET_ALL
