### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

# Commented out because function is updated later
# def create_book():
#     title = input('What is the title of the book?:')
#     author = input('What is the name of the author of the book?:')
#     year = input('In why year was the book published?:')
#     rating = input("What is the book's rating (out of 5)?:")
#     pages = input("How many pages does the book have?:")
    
#     book_dictionary = {
#         'title':title,
#         'author':author,
#         'year':year,
#         'rating':rating,
#         'pages':pages
#     }

#     return book_dictionary

# print(create_book())


### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# Commented out because function is updated later
# def create_book():
#     title = input('What is the title of the book?:')
#     author = input('What is the name of the author of the book?:')
#     year = int(input('In why year was the book published?:'))
#     rating = float(input("What is the book's rating (out of 5)?:"))
#     pages = int(input("How many pages does the book have?:"))
    
#     book_dictionary = {
#         'title':title,
#         'author':author,
#         'year':year,
#         'rating':rating,
#         'pages':pages
#     }

#     return book_dictionary

# print(create_book())


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

# Commented out because function is updated later
# def create_book():
#     title = input('What is the title of the book?:')
#     author = input('What is the name of the author of the book?:')
#     try:
#         year = int(input('In which year was the book published?:'))
#     except:
#         year = int(input('Please type a number for the year:'))
#     try:
#         rating = float(input("What is the book's rating (out of 5)?:"))
#     except:
#         rating = float(input("Please type a number for the rating:"))
#     try:
#         pages = int(input("How many pages does the book have?:"))
#     except:    
#         pages = int(input("Please type a number for number of pages:"))
    
    
#     book_dictionary = {
#         'title':title,
#         'author':author,
#         'year':year,
#         'rating':rating,
#         'pages':pages
#     }

#     return book_dictionary

# print(create_book())

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

# books_list is used to test my functions
books_list= [
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

def create_book():
    '''Adds a book to a list based on inputs, then prints and returns the list of books'''
    title = input('What is the title of the book?:')
    author = input('What is the name of the author of the book?:')
    try:
        year = int(input('In which year was the book published?:'))
    except:
        year = int(input('Please type a number for the year:'))
    try:
        rating = float(input("What is the book's rating (out of 5)?:"))
    except:
        rating = float(input("Please type a number for the rating:"))
    try:
        pages = int(input("How many pages does the book have?:"))
    except:    
        pages = int(input("Please type a number for number of pages:"))
    
    
    book_dictionary = {
        'title':title,
        'author':author,
        'year':year,
        'rating':rating,
        'pages':pages
    }

    books_list.append(book_dictionary)
    print(books_list)
    return books_list


def delete_book(book):
    '''Deletes a book based on inputted title of the book'''
    option = input("Input title to delete book from list.")
    for dict in book:
        if option == dict['title']:
            book.remove(dict)
            print(book)
            return book
    option = input("Book title does not match any book titles in the list. Please try again.")
    print(book)
    return book

def menu(book):
    '''Does the create book or delete book functions depending on what's input'''
    option = int(input('Input 1 to create a new book, Input 2 to delete a book, Input 3 to exit this function'))
    if option == 1:
        create_book()
    elif option == 2:
        delete_book(book)
    elif option == 3:
        print('Goodbye')
    else:
        option = int(input('Please select between a number between 1 and 3. Input 1 to create a new book, Input 2 to delete a book (after inputting 2 input the index number starting at 0 to delete), Input 3 to exit this function'))

menu(books_list)

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

def main_menu(book):
    '''Updated menu function that implements a while loop'''
    active = True
    while active:    
        option = int(input('Input 1 to create a new book, Input 2 to delete a book, Input 3 to exit this function'))
        if option == 1:
            create_book()
        elif option == 2:
            delete_book(book)
        elif option == 3:
            print('Goodbye')
            active = False
        else:
            option = int(input('Please select between a number between 1 and 3. Input 1 to create a new book, Input 2 to delete a book (after inputting 2 input the index number starting at 0 to delete), Input 3 to exit this function'))

main_menu(books_list)