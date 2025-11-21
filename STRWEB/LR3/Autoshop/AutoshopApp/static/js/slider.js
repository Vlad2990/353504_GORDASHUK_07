class Slider {
    constructor(length) {
        this.length = length;
        this.delay = 5000;
        this.currentSlide = 0;
        this.loop = true;
        this.navs = true;
        this.pags = true;
        this.auto = true;
        this.stopMouseHover = true;

        this.slides = document.querySelectorAll(".slide");
        this.dots = document.querySelectorAll(".slider-dot");

        this.onMouseEnter = () => this.auto = false;
        this.onMouseLeave = () => this.auto = true;

        this.settings = document.getElementById("slider-settings");
        this.settings.addEventListener("submit", this.settingsApply.bind(this));
    }


    settingsApply(event) {
        event.preventDefault();
        const formData = new FormData(this.settings);
        this.delay = Number(formData.get("interval-input"));
        this.navs = formData.get("navs-toggle") !== null;
        this.pags = formData.get("pags-toggle") !== null;
        this.auto = formData.get("auto-toggle") !== null;
        this.stopMouseHover = formData.get("mouse-toggle") !== null;       
        this.loop = formData.get("loop-toggle") !== null;
    }

    get navs() {
        return this._navs;
    }

    set navs(value) {
        this._navs = value;
        document.querySelector(".next").style.display = value === true ? "block" : "none";
        document.querySelector(".prev").style.display = value === true ? "block" : "none";
    }

    get pags() {
        return this._pags;
    }

    set pags(value) {
        this._pags = value;
        document.querySelector(".dots").style.display = value === true ? "flex" : "none";  
        document.getElementById("pags-toggle").value = value;   
    }

    get delay() {
        return this._delay;
    }

    set delay(value) {
        if (Number.isFinite(value) && value <= 10000 && value >= 1000) {
            this._delay = value;
            document.getElementById("interval-input").value = value;
            if (this.intervalId) {
                clearInterval(this.intervalId)
            }
            this.intervalId = setInterval(() => this.autoChange(), value)
        } else {
            alert("Wrong delay")
        }
    }

    get stopMouseHover() {
        return this._stopMouseHover;
    }
    
    set stopMouseHover(value) {
        this._stopMouseHover = value;
    
        const slider = document.querySelector(".slider-container");
    
        if (value) {
            slider.addEventListener("mouseenter", this.onMouseEnter);
            slider.addEventListener("mouseleave", this.onMouseLeave);
        } else {
            slider.removeEventListener("mouseenter", this.onMouseEnter);
            slider.removeEventListener("mouseleave", this.onMouseLeave);
        }
    }


    calculateCurrent(n) {
        if (this.loop) {
            if (n >= this.length) this.currentSlide = 0;
            else if (n < 0) this.currentSlide = this.length - 1;
            else this.currentSlide = n;
        }
        else {
            if (n >= this.length || n < 0) return;
            this.currentSlide = n;
        }
    }

    changeCurrent(n) {
        this.calculateCurrent(n);
        let slides = document.querySelectorAll(".slide");
        let dots = document.querySelectorAll(".slider-dot");

        slides.forEach((slide, i) => {
            slide.style.display = (i === this.currentSlide) ? "block" : "none";
        });    

        dots.forEach((dot, i) => {
            i !== this.currentSlide ? dot.classList.remove('active') : dot.classList.add('active');
        });
    }

    autoChange() {
        if (this.auto) {
            if (this.currentSlide === this.length - 1) {
                this.changeCurrent(0);
                
            }
            else {
                this.changeCurrent(this.currentSlide + 1);
            }
        }
    }
}

let s;

document.addEventListener("DOMContentLoaded", () => {
    s = new Slider(3);
    s.changeCurrent(0);
})