import re

class FileAnalazer:
    @staticmethod
    def get_char_with_num(content):
        """
        Search for word with num and upper case char 
        Args:
            content (str): text

        Returns:
            int: num of words
        """
        pattern = r'\b\w*[А-ЯA-Z][0-9]|\w*[0-9][А-ЯA-Z]\w*\b'
        matches = re.findall(pattern, content)
        return matches
    
    @staticmethod
    def is_ip(string):
        """
        Сhecking whether it is an IP
        Args:
            content (str): string

        Returns:
            bool
        """
        pattern = r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$'
        return bool(re.fullmatch(pattern, string))
    
    @staticmethod
    def shortest_with_w(content):
        """
        Find shortest word with 'w'
        Args:
            content (str): text

        Returns:
            str: shorter word
        """
        pattern = r'\b\w*w\b'        
        matches = re.findall(pattern, content)
        return min(matches, key=len)
    
    @staticmethod
    def in_len_increase(content: str):
        
        """
        Sort words in length increasing
        Args:
            content (str): text

        Returns:
            list[string]
        """
        words = re.findall(r"\b[a-zA-Zа-яА-Я']+\b", content)
        return sorted(words, key=len)
    
    @staticmethod
    def sent_num(content: str):
        """
        Count num of sentences
        Args:
            content (str): text

        Returns:
            int: num of sentences
        """
        words = re.findall(r'[.!?]', content)
        if len(words) < 1:
            return 1
        return len(words)
    
    @staticmethod
    def num_of_narrative(content: str):
        """
        Count num of narrative sentences
        Args:
            content (str): text

        Returns:
            int: num of narrative sentences
        """
        words = re.findall('\.', content)
        return len(words)
    
    @staticmethod
    def num_of_interrogative(content: str):
        """
        Count num of interrogative sentences
        Args:
            content (str): text

        Returns:
            int: num of interrogative sentences
        """
        words = re.findall('\?', content)
        return len(words)
    
    @staticmethod
    def num_of_incentive(content: str):
        """
        Count num of incentive sentences
        Args:
            content (str): text

        Returns:
            int: num of incentive sentences
        """
        words = re.findall('!', content)
        return len(words)
    
    @staticmethod
    def avr_sent_len(content: str):
        """
        Calculate avarage length of sentences
        Args:
            content (str): text

        Returns:
            float
        """
        words = content.split()
        return len(words) / FileAnalazer.sent_num(content)
    
    @staticmethod
    def avr_word_len(content: str):
        """
        Calculate avarage length of word
        Args:
            content (str): text

        Returns:
            float
        """
        words = content.split()
        num = 0
        for word in words:
            num += len(word)
        return num / len(words)
    
    @staticmethod
    def num_of_smiles(content: str):
        """
        Count num of smiles
        Args:
            content (str): text

        Returns:
            int
        """
        pattern = r'[:;]-*([(\[)\]])\1*'
        matches = re.findall(pattern, content)
        return len(matches)