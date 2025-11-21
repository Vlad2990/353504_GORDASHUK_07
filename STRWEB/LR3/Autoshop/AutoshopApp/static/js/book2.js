function BookBase(author, title, year) {
    this.setAuthor(author);
    this.setTitle(title);
    this.setYear(year);
}

BookBase.prototype.getAuthor = function() { return this._author; };
BookBase.prototype.setAuthor = function(value) {
    if (typeof value !== "string" || value.trim() === "") throw new Error("Wrong author");
    this._author = value.trim();
};

BookBase.prototype.getTitle = function() { return this._title; };
BookBase.prototype.setTitle = function(value) {
    if (typeof value !== "string" || value.trim() === "") throw new Error("Wrong title");
    this._title = value.trim();
};

BookBase.prototype.getYear = function() { return this._year; };
BookBase.prototype.setYear = function(value) {
    const n = Number(value);
    if (!Number.isFinite(n) || n < 1 || n > 2025) throw new Error("Wrong year");
    this._year = n;
};

BookBase.createFromForm = function(event) {
    var form = event.target;
    var data = new FormData(form);
    var author = data.get("author");
    var title = data.get("title");
    var year = data.get("year");

    form.author.classList.remove("error");
    form.title.classList.remove("error");
    form.year.classList.remove("error");

    try { return new BookBase(author, title, year); }
    catch (e) {
        if (e.message.includes("author")) form.author.classList.add("error");
        if (e.message.includes("title")) form.title.classList.add("error");
        if (e.message.includes("year")) form.year.classList.add("error");
        alert(e.message);
        return null;
    }
};

BookBase.renderAll = function(list, containerSelector) {
    var place = document.querySelector(containerSelector);
    place.innerHTML = "";
    list.forEach(function(b) {
        var li = document.createElement("li");
        li.innerHTML = "<div>" + b.getAuthor() + "</div><div>" + b.getTitle() + "</div><div>" + b.getYear() + "</div>";
        place.appendChild(li);
    });
};

function Library(books, minYear) {
    this.books = books || [];
    this.minYear = minYear || 1980;
}

Library.prototype.addBook = function(book) { 
    this.books.push(book); 
};
Library.prototype.render = function(selector) { 
    BookBase.renderAll(this.books, selector);
};
Library.prototype.filterByAuthor = function(author) { 
    return this.books.filter(function(b) { 
        return b.getAuthor() === author;
    }); 
};
Library.prototype.filterByYear = function(year) { 
    year = year || this.minYear;
    return this.books.filter(function(b) { 
        return b.getYear() >= year; 
    }); 
};
Library.prototype.filterByAuthorAndYear = function(author, year) { 
    year = year || this.minYear; 
    return this.books.filter(function(b) { 
        return b.getAuthor() === author && b.getYear() >= year; 
    }); 
};

document.addEventListener("DOMContentLoaded", function() {
    var booksContainer = ".books-container";
    var books = [
        new BookBase("George Orwell", "1984", 1981),
        new BookBase("George Orwell", "Animal Farm", 1985),
        new BookBase("J.K. Rowling", "Harry Potter", 1997),
        new BookBase("J.R.R. Tolkien", "The Hobbit", 1978),
        new BookBase("J.R.R. Tolkien", "The Lord of the Rings", 1983),
        new BookBase("Stephen King", "The Shining", 1980),
        new BookBase("Stephen King", "It", 1986),
        new BookBase("Agatha Christie", "Murder on the Orient Express", 1990),
        new BookBase("Isaac Asimov", "Foundation", 1982),
        new BookBase("Ray Bradbury", "Fahrenheit 451", 1984)
    ];
    var library = new Library(books, 1980);
    library.render(booksContainer);

    var addForm = document.getElementById("add-book");
    addForm.addEventListener("submit", function(event){
        event.preventDefault();
        var book = BookBase.createFromForm(event);
        if (!book) return;
        library.addBook(book);
        library.render(booksContainer);
    });

    var filterForm = document.getElementById("filter-author");
    filterForm.addEventListener("submit", function(event){
        event.preventDefault();
        var name = new FormData(filterForm).get("author").trim();
        filterForm.author.classList.remove("error");
        if (!name) { filterForm.author.classList.add("error"); return; }

        var res = library.filterByAuthorAndYear(name);
        var resultContainer = ".result-container";
        if (res.length) {
            document.querySelector(".result-title").textContent = "Books by this author published after 1980:";
            BookBase.renderAll(res, resultContainer);
        } else {
            document.querySelector(resultContainer).innerHTML = "";
            document.querySelector(".result-title").textContent = "No such books found.";
        }
    });
});
