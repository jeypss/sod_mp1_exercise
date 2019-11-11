from notebook import Notebook


class Menu:
    """
    Menu class
    """
    def __init__(self):
        self.nb = Notebook()
        self.options = {'View': self.view_all, 'Search': self.nb.search,
                        'Add': self.nb.add_note, 'Modify': self.nb.update}

    def display(self):
        """
        Shows the interactive options of Menu
        """
        mapping = {1: self.options.get('View'), 2: m.options.get('Search'), 3: m.options.get('Add')}
        while True:
            print("""Select an option:
            1. View all Notes
            2. Search a Note
            3. Add a Note
            """)
            try:
                selection = input('Enter your command:')
            except ValueError:
                while True:
                    cont = input('{} is not a valid option. Do you want to continue?[Y/N]'.format(selection))

                    if cont.lower() == 'y':
                        pass
                    elif cont.lower() == 'n':
                        pass
                    else:
                        continue

    def view_all(self):
        pass


if __name__ == '__main__':

    # Test Case
    m = Menu()
    m.display()

    # # Add Notes option
    # m.options.get('Add')(tags='news', content='hello and hi')
    # m.options.get('Add')(tags='local', content='boombastic')
    # m.options.get('Add')(tags='local,test', content='testing and')
    # # print(m.display())
    #
    # # Search option (with matched filters)
    # filtered_results1 = m.options.get('Search')(criteria='and', filter_tags=True, filter_content=True)
    # # print(filtered_results1)
    #
    # # Search option (without matched filters)
    # # filtered_results2 = m.options.get('Search')(criteria='case', filter_content=True)
    # # print(filtered_results2)
    #
    # # Update option (passed filtered_results1 variable that contains notes to be updated)
    # updated_results1 = m.options.get('Modify')(notes=filtered_results1, new_value='new_val', filter_tags=True)
    # print(updated_results1)
    #
    # for note in updated_results1:
    #      print(note.tags)
