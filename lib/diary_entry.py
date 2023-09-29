class DiaryEntry:
    def __init__(self, date, contents) -> None:
        # entry stored as {date: contents} dictionary
        self.entry = {date: contents}    
        pass

    def count_words_in_entry_contents(self):
        # returns int for number of words in contents
        pass

    def reading_time(self, wpm):
        # returns int for estimate reading time in minutes of entry contents
        pass

    def reading_chunk(self, time):
        # returns chunk of diary according to reading time/speed
        pass

    def find_phone_numbers(self):
        # extracts phone numbers from diary entry contents
        pass