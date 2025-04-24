from fileAnalyz import FileAnalazer
from result import Result
from zipfile import ZipFile
from decorator import repeat_on_demand

@repeat_on_demand()
def Task2():
    """Analizy text from file and save result to zip"""
    file = open("text.txt", 'r')
    content = file.read()
    file.close()
    print(content)
    print(FileAnalazer.in_len_increase(content))
    result = Result()
    result.char_with_num = FileAnalazer.get_char_with_num(content)
    result.shortest_with_w = FileAnalazer.shortest_with_w(content)
    result.len_increase_order = FileAnalazer.in_len_increase(content)
    result.is_ip = FileAnalazer.is_ip(content[0:14:1])
    result.sentences_count = FileAnalazer.sent_num(content)
    result.narrative_count = FileAnalazer.num_of_narrative(content)
    result.interrogative_count = FileAnalazer.num_of_interrogative(content)
    result.incentive_count = FileAnalazer.num_of_incentive(content)
    result.average_sent_length = FileAnalazer.avr_sent_len(content)
    result.average_word_length = FileAnalazer.avr_word_len(content)
    result.smiles_count = FileAnalazer.num_of_smiles(content)
    
    print(result)
    
    file2 = open("result.txt", 'w')
    file2.write(str(result))
    file2.close()
    
    with ZipFile("result.zip", 'w') as zip:
        zip.write("result.txt")
        item = zip.getinfo("result.txt")
        print(f"File Name: {item.filename} Date: {item.date_time} Size: {item.file_size}")
    