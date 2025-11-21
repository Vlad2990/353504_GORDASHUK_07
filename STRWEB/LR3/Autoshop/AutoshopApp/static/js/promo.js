document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".promocode");

    cards.forEach(card => {
        card.addEventListener("mousemove", e => {
            const rect = card.getBoundingClientRect();

            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const normX = x / rect.width;
            const normY = y / rect.height;

            const moveX = (normX - 0.5) * 10; 
            const moveY = (normY - 0.5) * 10;

            card.style.transform = `translate(${moveX}px, ${moveY}px)`;
        });

        card.addEventListener("mouseleave", () => {
            card.style.transform = "translate(0px, 0px)";
        });
    });
});
