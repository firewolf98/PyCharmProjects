class AbstractWordCounter:
    @staticmethod
    def can_count(filename):
        raise NotImplementedError()

    @staticmethod
    def count(filename):
        raise NotImplementedError()

class PlainTextWordCounter(AbstractWordCounter):
    @staticmethod
    def can_count(filename):
        return filename.lower().endswith(".txt")

    @staticmethod
    def count(filename):
        if not PlainTextWordCounter.can_count(filename):
            return 0
        import re
        regex=re.compile(r"\w+")
        total=0
        with open(filename,encoding="utf-8") as file:
            for line in file:
                for _ in regex.finditer(line):
                    total+=1
        return total

def count_words(filename):
    for wordCounter in (PlainTextWordCounter):
        if wordCounter.can_count(filename):
            return wordCounter.count(filename)
