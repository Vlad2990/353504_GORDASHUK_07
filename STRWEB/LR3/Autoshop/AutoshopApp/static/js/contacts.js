class Pagination {
    constructor(n, items, pag) {
        this.itemsPerPage = n;
        this.currentPage = 1;
        this.items = Array.from(document.querySelectorAll(items));
        this.tempItems = this.items.slice();
        this.pag = document.querySelector(pag);
        this.totalPages = Math.ceil(this.items.length / this.itemsPerPage);
        this.showItems();
        this.showPags();
    }

    showItems() {
        this.tempItems.forEach(el => el.style.display = "none");
        const start = (this.currentPage - 1) * this.itemsPerPage;
        const end = start + this.itemsPerPage;
        this.items.slice(start, end).forEach(el => el.style.display = "");
    }

    showPags() {
        this.pag.innerHTML = '';
        const prev = document.createElement('button');
        prev.textContent = 'Previous';
        prev.onclick = () => { this.currentPage--; this.showItems(); this.showPags(); };
        if (this.currentPage === 1) prev.disabled = true;
        this.pag.appendChild(prev);

        for (let i = 1; i <= this.totalPages; i++) {
            const btn = document.createElement('button');
            btn.textContent = i;
            if (i === this.currentPage) btn.classList.add('active');
            btn.onclick = () => { this.currentPage = i; this.showItems(); this.showPags(); };
            this.pag.appendChild(btn);
        }

        const next = document.createElement('button');
        next.textContent = 'Next';
        next.onclick = () => { this.currentPage++; this.showItems(); this.showPags(); };
        if (this.currentPage === this.totalPages) next.disabled = true;
        this.pag.appendChild(next);
    }

    findSubs(str) {
        const s = str.trim().toLowerCase();
        if (!s) {
            this.items = this.tempItems.slice();
            this.currentPage = 1;
            this.totalPages = Math.ceil(this.items.length / this.itemsPerPage);
            return;
        }
        this.items = this.tempItems.filter(el => el.innerText.toLowerCase().includes(s));
        this.currentPage = 1;
        this.totalPages = Math.ceil(this.items.length / this.itemsPerPage);
    }
}

function renderTable(data) {
    const tbody = document.querySelector("#table-contacts tbody");
    tbody.innerHTML = "";
    data.forEach(item => {
        const tr = document.createElement("tr");
        tr.className = "table-item";
        tr.innerHTML = `
            <td>${item.image ? `<img src="${item.image}" width="60">` : ""}</td>
            <td>${item.name}</td>
            <td>${item.description}</td>
            <td><a href="tel:${item.phone_number}">${item.phone_number}</a></td>
            <td><a href="mailto:${item.email}">${item.email}</a></td>
            <td><input type="checkbox" class="prem-check"></td>`;
        tbody.appendChild(tr);
    });
    initRowClicks();
}

function initRowClicks() {
    document.querySelectorAll(".table-item").forEach(row => {
        row.addEventListener("click", event => {
            const cells = row.querySelectorAll("td");
            const clickedCell = event.target.closest("td");
            if (Array.from(cells).indexOf(clickedCell) === 5) return;
            const image = cells[0].querySelector("img")?.src || "";
            const name = cells[1].innerText;
            const description = cells[2].innerText;
            const phone = cells[3].innerText;
            const email = cells[4].innerText;
            showDetails({ image, name, description, phone, email });
        });
    });
}

function showDetails(item) {
    const box = document.getElementById("details");
    box.style.display = "block";
    box.innerHTML = `
        <h3>${item.name}</h3>
        ${item.image ? `<img src="${item.image}">` : ""}
        <p><strong>Description:</strong> ${item.description}</p>
        <p><strong>Phone:</strong> ${item.phone}</p>
        <p><strong>Email:</strong> ${item.email}</p>`;
}

function generateAward(inds) {
    const msg = document.createElement('div');
    msg.className = "prem-msg";
    let names = [];
    Array.from(p.items).forEach((el, i) => {
        if (inds.includes(i)) names.push(el.querySelectorAll('td')[1].innerText.trim());
    });
    msg.textContent = "Awards given to: " + names.join(", ");
    document.body.appendChild(msg);
    setTimeout(() => msg.classList.add('show'), 10);
    setTimeout(() => { msg.classList.remove('show'); setTimeout(() => msg.remove(), 500); }, 3000);
}

function initSorting() {
    const table = document.getElementById("table-contacts");
    const headers = table.querySelectorAll("thead th");
    headers.forEach((th, index) => {
        if (th.classList.contains("sort-name") ||
            th.classList.contains("sort-desc") ||
            th.classList.contains("sort-phone") ||
            th.classList.contains("sort-email")) {
            let asc = true;
            th.addEventListener("click", () => {
                headers.forEach(header => header.textContent = header.textContent.replace(/ ▲| ▼/g, ''));
                th.textContent += asc ? ' ▲' : ' ▼';
                sortTable(index, asc);
                asc = !asc;
            });
        }
    });
}

function sortTable(colIndex, asc = true) {
    const tbody = document.querySelector("#table-contacts tbody");
    const rows = Array.from(tbody.querySelectorAll("tr"));
    rows.sort((a, b) => {
        const cellA = a.children[colIndex].innerText.toLowerCase();
        const cellB = b.children[colIndex].innerText.toLowerCase();
        return (cellA < cellB ? -1 : 1) * (asc ? 1 : -1);
    });
    tbody.innerHTML = "";
    rows.forEach(row => tbody.appendChild(row));
    p.items = Array.from(document.querySelectorAll(".table-item"));
    p.totalPages = Math.ceil(p.items.length / p.itemsPerPage);
    p.currentPage = 1;
    p.showItems();
    p.showPags();
}

function validateURL(url) {
    const pattern = /^(https?:\/\/).+\.(png|jpg)$/i;
    return pattern.test(url.trim());
}

function validatePhone(phone) {
    const pattern = /^(\+375|8)\s?\(?\d{2}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$/;
    return pattern.test(phone.trim());
}

function showResult(input, isValid) {
    let parent = input.parentNode;
    let existing = parent.querySelector('.check-result');
    if (!existing) {
        existing = document.createElement('div');
        existing.className = 'check-result';
        existing.style.marginTop = '5px';
        existing.style.fontWeight = 'bold';
        existing.style.fontSize = '14px';
        parent.appendChild(existing);
    }
    existing.textContent = isValid ? '✔ Valid' : '✖ Invalid';
    existing.style.color = isValid ? 'green' : 'red';
}

function getForm() {
    let form = document.forms["add-form"];
    const nameOk = form.name.value.trim() !== "";
    const descOk = form.description.value.trim() !== "";
    const emailOk = form.email.value.trim() !== "";
    const urlOk = validateURL(document.getElementById("url-input").value);
    const phoneOk = validatePhone(document.getElementById("phone-input").value);
    createBtn.disabled = !(nameOk && descOk && emailOk && urlOk && phoneOk);
}

document.addEventListener("DOMContentLoaded", function() {
    const preloader = document.querySelector(".preloader");
    const table = document.getElementById("table-contacts");
    table.style.display = "none";
    preloader.style.display = "flex";

    fetch("/api/contacts/")
        .then(res => res.json())
        .then(data => {
            const arr = Array.isArray(data) ? data : data.contacts || [];
            renderTable(arr);
            window.p = new Pagination(3, '.table-item', '.pagination');
            preloader.style.display = "none";
            table.style.display = "table";
            initSorting();
        });

    document.querySelector(".finder").addEventListener("submit", event => {
        event.preventDefault();
        let form = document.forms.finder;
        p.findSubs(form.elements.text.value);
        p.showItems();
        p.showPags();
    });

    document.querySelector(".prem").addEventListener("click", () => {
        let checks = Array.from(document.querySelectorAll(".prem-check"));
        let inds = [];
        checks.forEach((cb, i) => { if (cb.checked) inds.push(i); });
        generateAward(inds);
        checks.forEach(cb => cb.checked = false);
    });

    window.addBtn = document.getElementById("add-btn");
    addBtn.addEventListener("click", () => {
        document.getElementById("add-form").style.display = "block";
        addBtn.style.display = "none";
    });

    window.createBtn = document.getElementById("add-cont");
    const urlInput = document.getElementById("url-input");
    const urlCheckBtn = document.getElementById("check-url");
    const phoneInput = document.getElementById("phone-input");
    const phoneCheckBtn = document.getElementById("check-phone");

    document.querySelectorAll("#add-form input, #add-form textarea")
        .forEach(el => el.addEventListener("input", getForm));

    urlCheckBtn.addEventListener('click', e => { e.preventDefault(); showResult(urlInput, validateURL(urlInput.value)); getForm(); });
    phoneCheckBtn.addEventListener('click', e => { e.preventDefault(); showResult(phoneInput, validatePhone(phoneInput.value)); getForm(); });

    createBtn.addEventListener("click", e => {
    e.preventDefault();
    const form = document.getElementById("add-form");
    const formData = new FormData(form);

    fetch("/api/contacts/", {
        method: "POST",
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        const arr = Array.isArray(data) ? data : [data];
        arr.forEach(item => {
            const tbody = document.querySelector("#table-contacts tbody");
            const tr = document.createElement("tr");
            tr.className = "table-item";
            tr.innerHTML = `
                <td>${item.image ? `<img src="${item.image}" width="60">` : ""}</td>
                <td>${item.name}</td>
                <td>${item.description}</td>
                <td><a href="tel:${item.phone_number}">${item.phone_number}</a></td>
                <td><a href="mailto:${item.email}">${item.email}</a></td>
                <td><input type="checkbox" class="prem-check"></td>`;
            tbody.appendChild(tr);
        });

    p.items = Array.from(document.querySelectorAll(".table-item"));
    p.tempItems = p.items.slice();
    p.totalPages = Math.ceil(p.items.length / p.itemsPerPage);
    p.currentPage = p.totalPages;
    p.showItems();
    p.showPags();

    initRowClicks();
    initSorting();
    document.getElementById("add-form").reset();
});

});


    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
