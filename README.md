# Бударин Виктор


В проекте реализованы следующие тесты:

Список реализованных тестов
test_add_new_book_add_two_books — проверяет добавление двух книг в коллекцию.

test_add_new_book_valid_name — проверяет добавление книги с валидным именем.

test_add_new_book_boundary_values_valid (с параметризацией) — проверяет граничные значения валидной длины имени (1 и 40 символов).

test_add_new_book_boundary_values_invalid (с параметризацией) — проверяет невалидные длины имени (0 и 41 символ).

test_add_new_book_duplicate_not_added — проверяет, что дубликат книги не добавляется.

test_set_book_genre_valid_added (с параметризацией) — проверяет установку валидных жанров для существующих книг.

test_set_book_genre_invalid_book_not_added — проверяет попытку установить жанр для несуществующей книги.

test_set_book_genre_invalid_genre_not_added — проверяет попытку установить невалидный жанр.

test_get_book_genre_success — проверяет получение жанра существующей книги.

test_get_books_genre_success — проверяет возврат полного словаря books_genre.

test_get_books_with_specific_genre_success — проверяет фильтрацию книг по жанру.

test_get_books_for_children_success — проверяет фильтрацию книг для детей (без возрастного рейтинга).

test_add_book_in_favorites_valid_added — проверяет добавление книги в избранное.

test_add_book_in_favorites_duplicate_1_added — проверяет, что дубликат в избранное не добавляется.

test_add_book_in_favorites_invalid_not_added — проверяет попытку добавить в избранное несуществующую книгу.

test_delete_book_from_favorites_success — проверяет удаление книги из избранного.

test_delete_book_from_favorites_not_in_list_success — проверяет попытку удалить из избранного несуществующую книгу.

test_get_list_of_favorites_books_success — проверяет корректность списка избранных книг.

Оценка покрытия ~ 95%

Ниже результаты тестов:

================================================== test session starts ===================================================
platform win32 -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\Admin\AppData\Local\Python\pythoncore-3.14-64\python.exe
cachedir: .pytest_cache
rootdir: C:\sprint_4_Budarin
plugins: cov-7.0.0
collected 21 items

tests.py::TestBooksCollector::test_add_new_book_add_two_books PASSED                                                [  4%]
tests.py::TestBooksCollector::test_add_new_book_valid_name PASSED                                                   [  9%] 
tests.py::TestBooksCollector::test_add_new_book_boundary_values_valid[a] PASSED                                     [ 14%] 
tests.py::TestBooksCollector::test_add_new_book_boundary_values_valid[aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa] PASSED [ 19%]
tests.py::TestBooksCollector::test_add_new_book_boundary_values_invalid[] PASSED                                    [ 23%] 
tests.py::TestBooksCollector::test_add_new_book_boundary_values_invalid[aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa] PASSED [ 28%]
tests.py::TestBooksCollector::test_add_new_book_duplicate_not_added PASSED                                          [ 33%] 
tests.py::TestBooksCollector::test_set_book_genre_valid_added[\u0413\u0430\u0440\u0440\u0438 \u041f\u043e\u0442\u0442\u0435\u0440-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED [ 38%]
tests.py::TestBooksCollector::test_set_book_genre_valid_added[\u041e\u043d\u043e-\u0423\u0436\u0430\u0441\u044b] PASSED [ 42%]
tests.py::TestBooksCollector::test_set_book_genre_invalid_genre_not_added PASSED                                    [ 52%] 
tests.py::TestBooksCollector::test_get_book_genre_success PASSED                                                    [ 57%] 
tests.py::TestBooksCollector::test_get_books_genre_success PASSED                                                   [ 61%] 
tests.py::TestBooksCollector::test_get_books_with_specific_genre_success PASSED                                     [ 66%] 
tests.py::TestBooksCollector::test_get_books_for_children_success PASSED                                            [ 71%] 
tests.py::TestBooksCollector::test_add_book_in_favorites_valid_added PASSED                                         [ 76%] 
tests.py::TestBooksCollector::test_add_book_in_favorites_duplicate_1_added PASSED                                   [ 80%] 
tests.py::TestBooksCollector::test_add_book_in_favorites_invalid_not_added PASSED                                   [ 85%] 
tests.py::TestBooksCollector::test_delete_book_from_favorites_success PASSED                                        [ 90%] 
tests.py::TestBooksCollector::test_delete_book_from_favorites_not_in_list_success PASSED                            [ 95%] 
tests.py::TestBooksCollector::test_get_list_of_favorites_books_success PASSED                                       [100%] 

=========================================== 21 passed in 0.16s ===========================================
