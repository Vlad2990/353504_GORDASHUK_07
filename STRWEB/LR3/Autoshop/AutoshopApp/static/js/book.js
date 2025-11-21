class BookBase {
    constructor(author, title, year) {
        this.author = author;
        this.title = title;
        this.year = year;
    }

    get author() { return this._author; }
    set author(value) {
        if (typeof value !== "string" || value.trim() === "")
            throw new Error("Wrong author");
        this._author = value.trim();
    }

    get title() { return this._title; }
    set title(value) {
        if (typeof value !== "string" || value.trim() === "")
            throw new Error("Wrong title");
        this._title = value.trim();
    }

    get year() { return this._year; }
    set year(value) {
        const n = Number(value);
        if (!Number.isFinite(n) || n < 1 || n > 2025)
            throw new Error("Wrong year");
        this._year = n;
    }

    static createFromForm(event) {
        const form = event.target;
        const data = new FormData(form);

        const author = data.get("author");
        const title = data.get("title");
        const year = data.get("year");

        form.author.classList.remove("error");
        form.title.classList.remove("error");
        form.year.classList.remove("error");

        try {
            return new BookBase(author, title, year);
        } 
        catch (e) {
            if (e.message.includes("author")) form.author.classList.add("error");
            if (e.message.includes("title")) form.title.classList.add("error");
            if (e.message.includes("year")) form.year.classList.add("error");
            alert(e.message);
            return null;
        }
    }

    static renderAll(list, containerSelector) {
        const place = document.querySelector(containerSelector);
        place.innerHTML = "";
        list.forEach(b => {
            const li = document.createElement("li");
            li.innerHTML = `<div>${b.author}</div><div>${b.title}</div><div>${b.year}</div>`;
            place.appendChild(li);
        });
    }
}



class Library extends BookBase {
    constructor(books = [], minYear = 1980) {
        super("none", "none", 1); 
        this.books = books;
        this.minYear = minYear;
    }

    addBook(book) {
        this.books.push(book);
    }

    render(selector) {
        BookBase.renderAll(this.books, selector);
    }

    filterByAuthor(author) {
        return this.books.filter(b => b.author === author);
    }

    filterByYear(year = this.minYear) {
        return this.books.filter(b => b.year >= year);
    }

    filterByAuthorAndYear(author, year = this.minYear) {
        return this.books.filter(b => b.author === author && b.year >= year);
    }
}


document.addEventListener("DOMContentLoaded", () => {
    const booksContainer = ".books-container";

    const books = [
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

    const library = new Library(books, 1980);
    library.render(booksContainer);

    const addForm = document.getElementById("add-book");
    addForm.addEventListener("submit", event => {
        event.preventDefault();
        const book = BookBase.createFromForm(event);
        if (!book) return;

        library.addBook(book);
        library.render(booksContainer);
    });

    const filterForm = document.getElementById("filter-author");
    filterForm.addEventListener("submit", event => {
        event.preventDefault();
        const name = new FormData(filterForm).get("author").trim();

        filterForm.author.classList.remove("error");
        if (!name) {
            filterForm.author.classList.add("error");
            return;
        }

        const res = library.filterByAuthorAndYear(name);
        const resultContainer = ".result-container";

        if (res.length) {
            document.querySelector(".result-title").textContent = "Books by this author published after 1980:";
            BookBase.renderAll(res, resultContainer);
        } 
        else {
            document.querySelector(resultContainer).innerHTML = "";
            document.querySelector(".result-title").textContent = "No such books found.";
        }
    });
});
