class Pagination {
    constructor(n, items, pag, settings) {
        this.itemsPerPage = n;
        this.currentPage = 1;
        this.items = Array.from(document.querySelectorAll(items));
        this.pag = document.querySelector(pag);
        this.totalPages = Math.ceil(this.items.length / this.itemsPerPage);
        if (settings) this.settings = document.getElementById(settings);
        this.settings.addEventListener("submit", this.settingsApply.bind(this));
        this.showItems();
        this.showPags();
        
    }

    get itemsPerPage() {
        return this._itemsPerPage;
    }

    set itemsPerPage(value) {
        if (!Number.isFinite(value) || value <= 1 || value > 10) {
            alert("Input value > 2 and < 11");
            return;
        }
        if (value === this._itemsPerPage) return;
        this._itemsPerPage = value;
    }

    settingsApply(event) {
        event.preventDefault();
        const formData = new FormData(this.settings);
        this.itemsPerPage = Number(formData.get("items-input"));
        this.totalPages = Math.ceil(this.items.length / this.itemsPerPage);
        this.currentPage = 1;

    this.showItems();
    this.showPags();
    }

    showItems() {
        const start = (this.currentPage - 1) * this.itemsPerPage;
        const end = start + this.itemsPerPage;
        this.items.forEach((item, i) => {
            item.style.display = (i >= start && i < end) ? 'block' : 'none';
        });
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
            if (i === this.currentPage) {
                btn.classList.add('active'); 
            }
            btn.onclick = () => { this.currentPage = i; this.showItems(); this.showPags(); };
            this.pag.appendChild(btn);
        }

        const next = document.createElement('button');
        next.textContent = 'Next';
        next.onclick = () => { this.currentPage++; this.showItems(); this.showPags(); };
        if (this.currentPage === this.totalPages) next.disabled = true;
        this.pag.appendChild(next);
    
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const t = new Pagination(3, ".product-card", ".pagination", "pagination-settings");
    document.querySelectorAll(".product-card").forEach(card => {
    card.addEventListener("mousemove", e => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;  
        const y = e.clientY - rect.top;

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = (centerY - y) / 20; 
        const rotateY = (x - centerX) / 20;

        card.style.transform = `
            perspective(700px)
            rotateX(${rotateX}deg)
            rotateY(${rotateY}deg)
            scale(1.05)
        `;
    });

    card.addEventListener("mouseleave", () => {
        card.style.transform = `
            perspective(700px)
            rotateX(0deg)
            rotateY(0deg)
            scale(1)
        `;
    });
});

});
