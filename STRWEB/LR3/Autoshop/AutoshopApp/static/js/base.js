class ThemeChanger {
	constructor() {
		this.toggleButton = document.getElementById('theme-toggle');
		this.body = document.body;
		
        if (this.isDark()) {
            this.body.classList.add('dark-theme');
        } 
		else {
            this.body.classList.remove('dark-theme');
        }

        this.toggleButton.innerHTML = this.isDark() ? '&#9789;' : '&#9788;';
        this.toggleButton.addEventListener('click', this.togglePressed.bind(this));
	}

	togglePressed() {
        const newTheme = this.isDark() ? 'light' : 'dark';
        localStorage.setItem('theme', newTheme);
        this.body.classList.toggle('dark-theme');
        this.toggleButton.innerHTML = newTheme === 'dark' ? '&#9789;' : '&#9788;';
	}

	getTheme() {
		return localStorage.getItem('theme');
	}


	isDark() {
		return this.getTheme() === 'dark';
	}
}

window.onload = function () {
    document.body.classList.add('loaded');
}

document.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", function (e) {
        const url = this.getAttribute("href");

        if (url && !url.startsWith("#") && !this.classList.contains("nav-button")) {
            e.preventDefault();
            document.body.classList.remove("loaded"); 
            setTimeout(() => {
                window.location.href = url;
            }, 100); 
        }
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const t = new ThemeChanger();
})