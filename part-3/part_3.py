my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

more_books= [
{
    'title':'The Way of Kings',
    'author':'Brandon Sanderson',
    'year':2010,
    'rating':4.65,
    'pages':1007
},
{
    'title':'Words of Radiance',
    'author':'Brandon Sanderson',
    'year':2014,
    'rating':4.76,
    'pages':1087
},
{
    'title':'Oathbringer',
    'author':'Brandon Sanderson',
    'year':2017,
    'rating':4.62,
    'pages':1248
},
{
    'title':'Rhythm of War',
    'author':'Brandon Sanderson',
    'year':2020,
    'rating':4.62,
    'pages':1232
}
]

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def returnKeys(book):
    return f'The book is {book["title"]} by {book["author"]} and was published in {book["year"]}. The book has a rating of {book["rating"]} and {book["pages"]} pages.'

print(returnKeys(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def returnBook(book):
    return book["title"]

def returnAuthor(book):
    return book['author']

def returnRating(book):
    return book['rating']

print(returnBook(my_book))
print(returnAuthor(my_book))
print(returnRating(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def returnTitles(books):
    authorList = []
    for titles in books:
        authorList.append(titles['title'])
    return authorList

print(returnTitles(more_books))

def totalPages(books):
    total = 0
    for pages in books:
        total+=pages['pages']
    return total
print(totalPages(more_books))

filter_by_year=lambda book_list,year: [book for book in book_list if book['year']>year]
print(filter_by_year(more_books,2015))
