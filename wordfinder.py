from random import randint

class WordFinder:
    # Dunders    
    """
    Class for finding random words from a dictionary

    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ("dog", "cat", "porcupine")
    True
    """

    def __init__(self, fpath: str="words.txt") -> None:
        self.fpath = fpath
        self.words = self.get_words(self.fpath)
        self.word_count = len(self.words)
        print(f"{self.word_count} words read")

    def __repr__(self) -> str:
        return f"WordFinder(`{self.fpath}`)"

    # Utility methods
    def get_words(self, fpath):
        """Read words from file
        Args:
            fpath (str): Relative or absolute path of file to read
        Returns:
            list: List of words from text file
        """
        with open(fpath, "r") as file:
            words = file.readlines()
            return [word.replace("\n", "") for word in words]

    def random(self, num_words: int = 1) -> str:
        """Get specified number of random words

        Args:
            num_words (int): Number of words to return

        Returns:
            str: Random word
        """
        
        return self.words[randint(0, self.word_count -1)]



class RandomWordFinder(WordFinder):
    """Subclass for handling comments and empty lines
    
    >>> rwf = RandomWordFinder("complex.txt")
    3 words read
    
    >>> rwf.random() in ("kale", "carrot", "pear")
    True

    Args:
        WordFinder (WordFinder): Parent class
    """

    def __init__(self, fpath) -> None:
        super().__init__(fpath)
    
    def get_words(self, fpath):
        with open(fpath, "r") as file:
            lines = [line for line in file.readlines()]
            return [line.replace("\n", "") for line in lines 
                if line.strip() != "" and line[0] != "#"]

            


def main():
    from doctest import testmod
    testmod(verbose=True)

if __name__ == "__main__":
    main()