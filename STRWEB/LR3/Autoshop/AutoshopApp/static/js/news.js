document.addEventListener("DOMContentLoaded", () => {

    const partA = document.querySelector(".part-a");
    const partB = document.querySelector(".part-b");
    const partC = document.querySelector(".part-c");
    const partD = document.querySelector(".part-d");

    document.addEventListener("scroll", () => {
        const scroll = window.scrollY;

        partA.style.transform = `translateX(${scroll * 1}px)`;
        partB.style.transform = `translateX(${-scroll * 1}px)`;
        partC.style.transform = `translateY(${scroll * 0.2}px)`;
        partD.style.transform = `translate(${-scroll * 1.5}px, ${scroll * 0.8}px)`;
    });

    const items = document.querySelectorAll("#list li");

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            const el = entry.target;

            // Появление
            if (entry.isIntersecting) {
                el.animate(
                    [
                        { opacity: 0, transform: "translateY(20px)" },
                        { opacity: 1, transform: "translateY(0)" }
                    ],
                    {
                        duration: 500,
                        easing: "ease-out",
                        fill: "forwards"
                    }
                );
            }
            // Исчезновение при обратном скролле
            else {
                el.animate(
                    [
                        { opacity: 1, transform: "translateY(0)" },
                        { opacity: 0, transform: "translateY(20px)" }
                    ],
                    {
                        duration: 400,
                        easing: "ease-in",
                        fill: "forwards"
                    }
                );
            }
        });
    }, { threshold: 0.2 });

    items.forEach(item => observer.observe(item));
});