### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

def create_new_book(book_source):
    '''Adds a book to the txt file'''
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

    with open(book_source,'a')as file:
        file.write(f"{title},{author},{year},{rating},{pages}\n")
                
### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
def print_all_books(book_source):
    '''Prints all the book information from the txt file'''
    with open(book_source,'r') as f:
        file = f.readlines()    
        for line in file:
            title, author, year, rating, pages = line.split(",")
            print(f"Title: {title}, Author: {author}, Year Published: {year}, Rating: {rating}, Pages:{pages}")


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def turn_into_dictionary(book_source):
    '''Converts txt file to a list of dictionaries that some of my functions use'''
    books_list = []
    with open(book_source,'r') as f:
        file = f.readlines()    
        for line in file:
            title, author, year, rating, pages = line.split(",")
            books_list.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
    return books_list

def delete_book(book_source):
    '''Deletes a book based on inputted title of the book'''
    list_dict = turn_into_dictionary(book_source)
    print(list_dict)
    option = input("Input title to delete book from list.")
    for dict in list_dict:
        if option == dict['title']:
            print('Title deleted successfully')
            list_dict.remove(dict)
            with open('library.txt','w')as file:
                for dictionary in list_dict:
                    file.write(f"{dictionary['title']},{dictionary['author']},{dictionary['year']},{dictionary['rating']},{dictionary['pages']}\n")

def book_count(book_source):
    '''Counts the number of books in the txt file'''
    list_dict = turn_into_dictionary(book_source)
    count = 0
    for dict in list_dict:
        count+=1
    print(count)
    return count

def page_count(book_source):
    '''Counts the total number of all the pages in the books in the txt file'''
    list_dict = turn_into_dictionary(book_source)
    pages = 0
    for dict in list_dict:
        pages += dict['pages']
    print(pages)
    return pages

def sort_rating(book_source):
    '''Sorts books from highest rating to lowest'''
    list_dict = turn_into_dictionary(book_source)
    list_dict = sorted(list_dict, key = lambda dict:dict['rating'],reverse=True)
    for dict in list_dict:
        print(dict)

def main_menu(book_source):
    active = True
    while active:    
        option = int(input('''
        Input 1 to create a new book,
        Input 2 to see all books, 
        Input 3 to delete a book, 
        Input 4 to return the number of books in the list, 
        Input 5 to see total pages,
        Input 6 to see books sorted by rating,
        Input 7 to exit the function'''))
        if option == 1:
            create_new_book(book_source)
        elif option ==2:
            print_all_books(book_source)
        elif option == 3:
            delete_book(book_source)
        elif option == 4:
            book_count(book_source)
        elif option == 5:
            page_count(book_source)
        elif option ==6:
            sort_rating(book_source)
        elif option == 7:
            print('Goodbye')
            active = False
        else:
            option = int(input('''
        Please select between a number between 1 and 7. 
        Input 1 to create a new book,
        Input 2 to see all books, 
        Input 3 to delete a book, 
        Input 4 to return the number of books in the list, 
        Input 5 to see total pages,
        Input 6 to see books sorted by rating,
        Input 7 to exit the function'''))

if __name__=="__main__":
    main_menu('library.txt')