import datetime
from note import Note


class Notebook:
    """
    Notebook class that contains all Note classes with Search, Add and Update Note methods
    """
    def __init__(self):
        self.notes = list()

    def update(self, notes: list, new_value: str, filter_tags: bool = False, filter_content: bool = False):
        """
        Modify a value in tags or content of a Note depending on the parameter given
        :param notes: list
        :param new_value: str
        :param filter_tags: bool
        :param filter_content: bool
        :return:
        """
        assert isinstance(new_value, str)

        if not filter_tags and not filter_content:
            raise TypeError('At least filter_tags or filter_content should be True')

        param_list = self.convert_param(filter_tags=filter_tags, filter_content=filter_content)

        for note in notes:
            for param in param_list:
                note.__dict__[param] = new_value

        return notes

    def add_note(self, tags: str, content: str):
        """
        Adds a Note class in the notes attribute
        :param tags: str
        :param content: str
        :return:
        """
        assert isinstance(tags, str)
        assert isinstance(content, str)

        created_date = datetime.datetime.now()

        # Create New Note Object
        new_note = Note(created_date, tags, content)

        # Append to Notes attribute
        self.notes.append(new_note)

    def search(self, criteria: str, filter_tags: bool = False, filter_content: bool = False):
        """
        Search through the tags or content in the notes attribute which depends on the param given in the boolean values
        of filter_tags and filter_content
        :param criteria: str
        :param filter_tags: bool
        :param filter_content: bool
        :return:
        """
        assert isinstance(criteria, str)

        if not filter_tags and not filter_content:
            raise TypeError('At least filter_tags or filter_content should be True')

        param_list = self.convert_param(filter_tags=filter_tags, filter_content=filter_content)

        filtered_notes = list()
        for note in self.notes:
            if self.match(note, criteria, param_list):
                filtered_notes.append(note)

        return filtered_notes

    @staticmethod
    def match(note: Note, criteria: str, param_list: list):
        """
        Checks whether the criteria parameter is located in the tags or content of a Note class depending on the
        parameter list given
        :param note: list
        :param criteria: str
        :param param_list: list
        :return: bool
        """
        for param in param_list:
            if criteria in note.__dict__[param]:
                return True

        return False

    @staticmethod
    def convert_param(filter_tags: bool = False, filter_content: bool = False):
        """

        :param filter_tags:
        :param filter_content:
        :return:
        """
        if filter_tags and filter_content:
            param_list = ['tags', 'memo']
        elif filter_tags:
            param_list = ['tags']
        elif filter_content:
            param_list = ['memo']
        else:
            return None

        return param_list
