class Result:
    def __init__(self):
        self.char_with_num = []       
        self.is_ip = []          
        self.shortest_with_w = ""        
        self.len_increase_order = []     
        self.sentences_count = 0       
        self.narrative_count = 0      
        self.interrogative_count = 0     
        self.incentive_count = 0      
        self.average_sent_length = 0.0
        self.average_word_length = 0.0 
        self.smiles_count = 0    
      
    def __str__(self):
        return (
            f"Text analysis results:\n"
            f"- Words with numbers and letters: {self.char_with_num}\n"
            f"- Contains valid IPs:\n" + "\n".join(f"\t{flag}" for flag in self.is_ip) + "\n"
            f"- Shortest word with 'w': '{self.shortest_with_w}'\n"
            f"- Words sorted by length: {self.len_increase_order}\n"
            f"- Total sentences: {self.sentences_count}\n"
            f"- Narrative sentences (.): {self.narrative_count}\n"
            f"- Interrogative sentences (?): {self.interrogative_count}\n"
            f"- Incentive sentences (!): {self.incentive_count}\n"
            f"- Average sentences length: {self.average_sent_length:.2f}\n"
            f"- Average word length: {self.average_word_length:.2f}\n"
            f"- Smileys found: {self.smiles_count}"
        )