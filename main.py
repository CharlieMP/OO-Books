# Write Python code for both the Novel and Magazine classes modelled in the previous slide. Include a suitable constructor method which uses the Book constructor method. Instantiate 2 novels and 2 magazines and print their details.
# Create the Book class (plus methods and attributes)
# Create the Novel class that inherits from Book class.
# Create the Magazine class that inherits from Book class.

class book:
    def __init__(self, title, author, year, numPages):
        self.title = str
        self.author = str
        self.year = int
        self.numPages = int


    def displayDetails(self):
        print(
            f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nNumber of Pages: {self.numPages}"
        )

class novel(book):
    def __init__(self, title, author, year, numPages, genre, numChapters):
        super().__init__(title, author, year, numPages)
        self.genre = str
        self.numChapters = int



    def displayDetails(self):
        print(
            f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nNumber of Pages: {self.numPages}\nGenre: {self.genre}\nNumber of Chapters: {self.numChapters}"
        )





ninjasguidetogaming = book()