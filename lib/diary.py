class Diary:
    def __init__(self) -> None:
        # holds collection of diary entries (as a list of dicts ?)
        self.entries = []
        

    def add(self, entry):
        # entry comes from DiaryEntry
        # updates self.entries
        # returns nothing
        self.entries.append(entry)

    def read(self):
        # is this done in diary entry? or here?
        # returns diary entries in a readable format
        pass

    def select_diary_entry_for_time_available(self, time, wpm):
        # uses method in DiaryEntry
        # returns selected entry
        pass

    def see_phone_numbers(self):
        # uses method in DiaryEntry
        # returns list of phone numbers
        pass

    def task_tracker(self):
        # uses separate Todo and TodoList classes
        # returns nothing as it stands
        pass
