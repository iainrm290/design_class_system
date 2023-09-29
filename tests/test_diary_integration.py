from lib.diary import *
from lib.diary_entry import *
import pytest

def test_diary_add():
    diary = Diary()
    entry = DiaryEntry("29/9/23",  "Not a lot really.")
    diary.add(entry)
    assert diary.entries == ("29/9/23",  "Not a lot really.")