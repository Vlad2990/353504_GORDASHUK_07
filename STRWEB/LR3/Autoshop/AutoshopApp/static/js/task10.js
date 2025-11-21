class Cosine {
    constructor() {
        this.eps = 0.0001;
        this.res = 1.0;
        this.term = 1.0;
        this.terms = [this.term];
    }

    calculate(x) {
        x = x % (2 * Math.PI);
        for (let inum = 1; inum < 500; inum++) {
            this.term *= (-1) * x * x / ((2 * inum - 1) * (2 * inum));
            this.res += this.term;
            this.terms.push(this.res);
            if (Math.abs(this.term) < this.eps) break;
        }
        return this.res;
    }
}

let chart = null;

document.addEventListener("DOMContentLoaded", () => {
    const form = document.forms["input-x"];

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const x = Number(form.elements.x.value);
        form.x.classList.remove("error");

        const saveBtn = document.getElementById("save-chart");

        if (!Number.isFinite(x)) {
            form.x.classList.add("error");
            if (chart) chart.destroy();
            saveBtn.style.display = "none";
            return;
        }

        saveBtn.style.display = "block";

        let cos = new Cosine();
        const res = cos.calculate(x);

        document.querySelector("#cell-x").textContent = x;
        document.querySelector("#cell-n").textContent = cos.terms.length;
        document.querySelector("#cell-res").textContent = res;
        document.querySelector("#cell-fres").textContent = Math.cos(x);
        document.querySelector("#cell-eps").textContent = cos.eps;

        const ctx = document.getElementById("chart").getContext("2d");

        if (chart) chart.destroy();
        
        const termsLabels = cos.terms.map((_, i) => i);
        const termsValues = cos.terms;
            
        const trueCos = Array(cos.terms.length).fill(Math.cos(x));

        chart = new Chart(ctx, {
            type: "line",
            data: {
                labels: termsLabels,
                datasets: [
                    {
                        label: "Partial Sum (Taylor Series)",
                        data: termsValues,
                        borderWidth: 2,
                        borderColor: "blue",
                        fill: false,
                        tension: 0.2
                    },
                    {
                        label: "Math.cos(x)",
                        data: trueCos,
                        borderWidth: 2,
                        borderColor: "red",
                        borderDash: [5, 5], 
                        fill: false
                    }
                ]
            },
            options: {
                animations: {
                    numbers: {
                        type: 'number',
                        duration: 2000
                    }
                }
            }
        });
        saveBtn.onclick = function () {
            const canvas = document.getElementById("chart");
            const url = canvas.toDataURL("image/png");

            const a = document.createElement("a");
            a.href = url;
            a.download = "chart.png"; 
            a.click();
        };
    });
});
