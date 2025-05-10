import pytest

class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    def test_add_new_book_valid_name(self, collector):
        collector.add_new_book("Гарри Поттер")
        assert "Гарри Поттер" in collector.books_genre
        assert collector.books_genre["Гарри Поттер"] == ""

    @pytest.mark.parametrize("name", ["", "a"*41])
    def test_add_new_book_invalid_name(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book("Властелин колец")
        collector.add_new_book("Властелин колец")
        assert len(collector.books_genre) == 1

    def test_set_book_genre_valid(self, collector):
        collector.add_new_book("Метро 2033")
        collector.set_book_genre("Метро 2033", "Фантастика")
        assert collector.books_genre["Метро 2033"] == "Фантастика"

    def test_set_book_genre_invalid_book(self, collector):
        collector.set_book_genre("Несуществующая книга", "Фантастика")
        assert "Несуществующая книга" not in collector.books_genre

    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Несуществующий жанр")
        assert collector.books_genre["Оно"] == ""

    def test_get_book_genre(self, collector):
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")
        assert collector.get_book_genre("Шерлок Холмс") == "Детективы"

    def test_get_book_genre_nonexistent(self, collector):
        assert collector.get_book_genre("Несуществующая книга") is None

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.set_book_genre("Книга 2", "Фантастика")
        result = collector.get_books_with_specific_genre("Фантастика")
        assert len(result) == 2
        assert "Книга 1" in result
        assert "Книга 2" in result

    def test_get_books_with_specific_genre_empty(self, collector):
        assert collector.get_books_with_specific_genre("Фантастика") == []

    def test_get_books_genre(self, collector):
        collector.add_new_book("Книга")
        assert collector.get_books_genre() == {"Книга": ""}

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Мультик")
        collector.add_new_book("Ужастик")
        collector.set_book_genre("Мультик", "Мультфильмы")
        collector.set_book_genre("Ужастик", "Ужасы")
        result = collector.get_books_for_children()
        assert "Мультик" in result
        assert "Ужастик" not in result

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Преступление и наказание")
        collector.add_book_in_favorites("Преступление и наказание")
        assert "Преступление и наказание" in collector.favorites

    def test_add_book_in_favorites_twice(self, collector):
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.add_book_in_favorites("Книга")
        assert len(collector.favorites) == 1

    def test_add_book_in_favorites_nonexistent(self, collector):
        collector.add_book_in_favorites("Несуществующая книга")
        assert len(collector.favorites) == 0

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.delete_book_from_favorites("Книга")
        assert "Книга" not in collector.favorites

    def test_delete_book_from_favorites_nonexistent(self, collector):
        collector.delete_book_from_favorites("Несуществующая книга")
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.add_book_in_favorites("Книга 1")
        collector.add_book_in_favorites("Книга 2")
        assert len(collector.get_list_of_favorites_books()) == 2
        assert "Книга 1" in collector.get_list_of_favorites_books()
        assert "Книга 2" in collector.get_list_of_favorites_books()
