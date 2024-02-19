import pytest


class TestBooksCollector:

    @pytest.mark.parametrize('name', ['A', 'Книга', 'Книга, в названии которой сорок символов'])
    def test_add_new_book_add_books_with_correct_names(self, name, collector):
        collector.add_new_book(name)
        assert name in collector.get_books_genre() and list(collector.get_books_genre().values()) == ['']

    @pytest.mark.parametrize('name', ['', 'Книга, в названии которой 41 символ!!!!!!', 'Книга, в названии которой сорок три символа'])
    def test_add_new_book_add_books_with_wrong_name(self, name, collector):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_book_with_existing_name(self, collector):
        name = 'Книга для дублирования'
        collector.add_new_book(name)
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name, genre', [['Книга1', 'Фантастика'], ['Книга2', 'Ужасы'], ['Книга3', 'Детективы'], ['Книга4','Мультфильмы'], ['Книга5','Комедии']])
    def test_set_book_genre_check_book_from_books_genre(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_set_book_genre_check_genre_not_from_genre(self, collector):
        name = 'Книга'
        genre = 'Научная фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) != genre

    def test_get_books_with_specific_genre_check_equal_genre(self, collector):
        specific_genre = 'Фантастика'
        name = 'Книга'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert list(collector.get_books_with_specific_genre(specific_genre)) == [name]

    @pytest.mark.parametrize('name, genre', [['Книга1', 'Ужасы'], ['Книга2', 'Научная фантастика']])
    def test_get_books_with_specific_genre_check_unequal_genre(self, name, genre, collector):
        specific_genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert list(collector.get_books_with_specific_genre(specific_genre)) == []

    def test_get_books_for_children_check_books_with_genre_not_from_genre_age_rating(self, collector):
        name = 'Книга'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert list(collector.get_books_for_children()) == [name]

    @pytest.mark.parametrize('name, genre', [['Книга1', 'Ужасы'], ['Книга2', 'Научная фантастика']])
    def test_get_books_for_children_check_books_with_genre_from_genre_age_rating(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert list(collector.get_books_for_children()) == []

    def test_add_book_in_favorites_add_book_from_books_genre(self, collector):
        name = 'Книга'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_add_book_not_from_books_genre(self, collector):
        name = 'Книга, которой нет в books_genre'
        name_second = 'Книга, которая есть в books_genre'
        collector.add_new_book(name_second)
        collector.add_book_in_favorites(name_second)
        assert name not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_add_double_name_book(self, collector):
        name = 'Книга, которая есть в favorites'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_existing_book(self, collector):
        name = 'Книга'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_delete_unexisting_book(self, collector):
        name = 'Книга'
        name2 = 'Книга, которой нет в favorites'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name2)
        assert collector.get_list_of_favorites_books() == [name]
