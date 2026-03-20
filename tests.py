import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, books_collector):
        books_collector.add_new_book('Гордость и предубеждение и зомби')
        books_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(books_collector.books_genre) == 2

    def test_add_new_book_valid_name(self, books_collector):
        books_collector.add_new_book('Война и мир')
        assert 'Война и мир' in books_collector.books_genre
        assert books_collector.books_genre['Война и мир'] == ''

    @pytest.mark.parametrize(
        'book_name',
        [
            'a',  # минимальная длина (1 символ)
            'a' * 40,  # максимальная длина (40 символов)
        ]
    )
    def test_add_new_book_boundary_values_valid(self, books_collector, book_name):
        books_collector.add_new_book(book_name)
        assert book_name in books_collector.books_genre
        assert books_collector.books_genre[book_name] == ''

    @pytest.mark.parametrize(
        'book_name',
        [
            '',  # 0 символов (невалидно)
            'a' * 41,  # 41 символ (невалидно)
        ]
    )
    def test_add_new_book_boundary_values_invalid(self, books_collector, book_name):
        books_collector.add_new_book(book_name)
        assert book_name not in books_collector.books_genre

    def test_add_new_book_duplicate_not_added(self, books_collector):
        books_collector.add_new_book('Преступление и наказание')
        books_collector.add_new_book('Преступление и наказание')
        assert len(books_collector.books_genre) == 1
        assert books_collector.books_genre['Преступление и наказание'] == ''

    @pytest.mark.parametrize(
        'book_name, genre',
        [
            ('Гарри Поттер', 'Фантастика'),
            ('Оно', 'Ужасы'),
        ]
    )
    def test_set_book_genre_valid_added(self, books_collector, book_name, genre):
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)
        assert books_collector.get_book_genre(book_name) == genre

    def test_set_book_genre_invalid_book_not_added(self, books_collector):
        books_collector.set_book_genre('Неизвестная книга', 'Фантастика')
        assert books_collector.get_book_genre('Неизвестная книга') is None

    def test_set_book_genre_invalid_genre_not_added(self, books_collector):
        books_collector.add_new_book('Книга без жанра')
        books_collector.set_book_genre('Книга без жанра', 'Романтика')
        assert books_collector.get_book_genre('Книга без жанра') == ''

    def test_get_book_genre_success(self, books_collector):
        books_collector.add_new_book('1984')
        books_collector.set_book_genre('1984', 'Фантастика')
        genre = books_collector.get_book_genre('1984')
        assert genre == 'Фантастика'

    def test_get_books_genre_success(self, books_collector):
        books_collector.add_new_book('1984')
        books_collector.set_book_genre('1984', 'Фантастика')
        books_collector.add_new_book('Оно')
        books_collector.set_book_genre('Оно', 'Ужасы')
        result = books_collector.get_books_genre()
        expected = {'1984': 'Фантастика', 'Оно': 'Ужасы'}
        assert result == expected

    def test_get_books_with_specific_genre_success(self, books_collector):
        books_collector.add_new_book('Дюна')
        books_collector.set_book_genre('Дюна', 'Фантастика')
        books_collector.add_new_book('Основание')
        books_collector.set_book_genre('Основание', 'Фантастика')
        books = books_collector.get_books_with_specific_genre('Фантастика')
        assert books == ['Дюна', 'Основание']

    def test_get_books_for_children_success(self, books_collector):
        books_collector.add_new_book('Винни-Пух')
        books_collector.set_book_genre('Винни-Пух', 'Мультфильмы')
        books_collector.add_new_book('Оно')
        books_collector.set_book_genre('Оно', 'Ужасы')
        children_books = books_collector.get_books_for_children()
        assert children_books == ['Винни-Пух']

    def test_add_book_in_favorites_valid_added(self, books_collector):
        books_collector.add_new_book('Мастер и Маргарита')
        books_collector.add_book_in_favorites('Мастер и Маргарита')
        assert 'Мастер и Маргарита' in books_collector.favorites

    def test_add_book_in_favorites_duplicate_1_added(self, books_collector):
        books_collector.add_new_book('Идиот')
        books_collector.add_book_in_favorites('Идиот')
        books_collector.add_book_in_favorites('Идиот')
        assert len(books_collector.favorites) == 1

    def test_add_book_in_favorites_invalid_not_added(self, books_collector):
        books_collector.add_book_in_favorites('Неизвестная книга')
        assert 'Неизвестная книга' not in books_collector.favorites
        assert books_collector.favorites == []

    def test_delete_book_from_favorites_success(self, books_collector):
        books_collector.add_new_book('Анна Каренина')
        books_collector.add_book_in_favorites('Анна Каренина')
        books_collector.delete_book_from_favorites('Анна Каренина')
        assert 'Анна Каренина' not in books_collector.favorites
        assert books_collector.favorites == []

    def test_delete_book_from_favorites_not_in_list_success(self, books_collector):
        books_collector.delete_book_from_favorites('Не в избранном')
        assert books_collector.favorites == []

    def test_get_list_of_favorites_books_success(self, books_collector):
        books_collector.add_new_book('Евгений Онегин')
        books_collector.add_new_book('Герой нашего времени')
        books_collector.add_book_in_favorites('Евгений Онегин')
        books_collector.add_book_in_favorites('Герой нашего времени')
        favorites = books_collector.get_list_of_favorites_books()
        assert favorites == ['Евгений Онегин', 'Герой нашего времени']
        assert len(favorites) == 2

    def test_get_book_genre_success(self, books_collector):
        books_collector.add_new_book('1984')
        books_collector.set_book_genre('1984', 'Фантастика')
        genre = books_collector.get_book_genre('1984')
        assert genre == 'Фантастика'

    def test_get_books_genre_success(self, books_collector):
        books_collector.add_new_book('1984')
        books_collector.set_book_genre('1984', 'Фантастика')
        books_collector.add_new_book('Оно')
        books_collector.set_book_genre('Оно', 'Ужасы')
        result = books_collector.get_books_genre()
        expected = {'1984': 'Фантастика', 'Оно': 'Ужасы'}
        assert result == expected


        