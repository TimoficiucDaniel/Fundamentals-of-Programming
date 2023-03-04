class RepoError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        result = ""
        for message in self._message:
            result += message
            result += "\n"
        return result
