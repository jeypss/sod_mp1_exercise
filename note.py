class Note:
    note_id = 0

    def __init__(self, created_date, tags, content):
        """
        :param note_id: int
        :param created_date: datetime object
        :param tags: str
        :param content: str
        """
        self.id = Note.note_id + 1
        self.created_date = created_date
        self.tags = tags
        self.memo = content

        Note.note_id += 1

    def get_id(self):
        """
        Returns the ID generated for a Note class
        :return: int
        """
        return self.id
