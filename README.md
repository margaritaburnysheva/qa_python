# qa_python
В проекте были реализованы юнит-тесты для приложения **BooksCollector** (оно позволяет установить жанр книг и добавить их в избранное):

1. **test_add_new_book_add_books_with_correct_names** - позитивный тест для метода add_new_book. Можно добавить в books_genre книгу, в названии которой от 1 до 40 символов (без указания жанра)
2. **test_add_new_book_add_books_with_wrong_name** - негативный тест для метода add_new_book. 
Нельзя добавить в books_genre книгу, в названии которой 0 или >40 символов
3. **test_add_new_book_add_book_with_existing_name** - негативный тест для метода add_new_book. 
Нельзя добавить в books_genre книгу, которая уже добавлена
4. **test_set_book_genre_check_book_from_books_genre** - позитивный тест для метода set_book_genre. 
Можно установить жанр книги, если книга есть в books_genre и ее жанр входит в список genre
5. **test_set_book_genre_check_genre_not_from_genre** - негативный тест для метода set_book_genre. 
Нельзя установить жанр книги, если жанр не входит в список genre
6. **test_get_books_with_specific_genre_check_equal_genre** - позитивный тест для метода get_books_with_specific_genre. 
Можно вывести список книг с определенным жанром
7. **test_get_books_with_specific_genre_check_unequal_genre** - негативный тест для метода get_books_with_specific_genre. 
Нельзя вывести список книг с определенным жанром, если жанра нет в books_genre
8. **test_get_books_for_children_check_books_with_genre_not_from_genre_age_rating** - позитивный тест для метода get_books_for_children. 
Можно вывести книги без возрастного рейтинга
9. **test_get_books_for_children_check_books_with_genre_from_genre_age_rating** - негативный тест для метода get_books_for_children. 
Нельзя вывести книги с возрастным рейтингом
10. **test_add_book_in_favorites_add_book_from_books_genre** - позитивный тест для метода add_book_in_favorites. 
Можно добавить книгу в favorites, если книга есть в books_genre
11. **test_add_book_in_favorites_add_book_not_from_books_genre** - негативный тест для метода add_book_in_favorites. 
Нельзя добавить книгу в favorites, если книги нет в books_genre
12. **test_add_book_in_favorites_add_double_name_book** - негативный тест для метода add_book_in_favorites. 
Нельзя добавить книгу в favorites, если книга уже есть в favorites
13. **test_delete_book_from_favorites_delete_existing_book** - позитивный тест для метода delete_book_from_favorites. 
Можно удалить книгу из favorites
14. **test_delete_book_from_favorites_delete_unexisting_book** - негативный тест для метода delete_book_from_favorites. 
Нельзя удалить книгу из favorites, если книги нет в favorites

Метод get_book_genre используется в тестах test_set_book_genre_check_book_from_books_genre, test_set_book_genre_check_genre_not_from_genre

Метод get_books_genre используется в тестах test_add_new_book_add_books_with_correct_names, test_add_new_book_add_books_with_wrong_name, test_add_new_book_add_book_with_existing_name

Метод get_list_of_favorites_books используется в тестах test_add_book_in_favorites_add_book_from_books_genre, test_add_book_in_favorites_add_book_not_from_books_genre, test_add_book_in_favorites_add_double_name_book, test_delete_book_from_favorites_delete_existing_book, test_delete_book_from_favorites_delete_unexisting_book
