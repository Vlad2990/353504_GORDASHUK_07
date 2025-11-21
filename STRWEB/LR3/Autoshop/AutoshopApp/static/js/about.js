document.addEventListener("DOMContentLoaded", () => {
    window.btn = document.querySelector("#addBtn");
    const formContainer = document.querySelector("#form-container");
    const inputContainer = document.getElementById("input-container");

    btn.onclick = function () {
        btn.style.display = "none";
        createForm(formContainer);
    };

    restoreInputs(inputContainer);
});


function createForm(container) {
    const wrapper = document.createElement("div");
    wrapper.classList.add("form-wrapper");

    const form = document.createElement("form");
    const grid = document.createElement("div");
    grid.classList.add("form-grid");

    const fields = [
        { label: "Name:", type: "text", name: "attrName" },
        { label: "Accept:", type: "text", name: "attrAccept", placeholder: "image/*, .pdf" },
        { label: "Multiple:", type: "checkbox", name: "attrMultiple" },
        { label: "Required:", type: "checkbox", name: "attrRequired" },
        { label: "Capture:", type: "text", name: "attrCapture", placeholder: "user, environment" }
    ];

    fields.forEach(field => {
        const label = document.createElement("label");
        label.textContent = field.label;

        const input = document.createElement("input");
        input.type = field.type;
        input.name = field.name;

        if (field.placeholder) input.placeholder = field.placeholder;

        label.appendChild(input);
        grid.appendChild(label);
    });

    const button = document.createElement("button");
    button.type = "submit";
    button.textContent = "Create";
    button.classList.add("form-create-btn");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const formData = new FormData(form);

        const config = {
            id: Date.now(),
            name: formData.get("attrName") || "",
            accept: formData.get("attrAccept") || "",
            multiple: !!formData.get("attrMultiple"),
            required: !!formData.get("attrRequired"),
            capture: formData.get("attrCapture") || ""
        };
        saveInputConfig(config);
        addInputToPage(config);
        wrapper.classList.add("form-wrapper-hidden");
        btn.style.display = "flex";
    });

    form.appendChild(grid);
    form.appendChild(button);

    wrapper.appendChild(form);
    container.appendChild(wrapper);
}

function saveInputConfig(cfg) {
    let saved = JSON.parse(localStorage.getItem("inputs") || "[]");
    saved.push(cfg);
    localStorage.setItem("inputs", JSON.stringify(saved));
}

function removeInputConfig(id) {
    let saved = JSON.parse(localStorage.getItem("inputs") || "[]");
    saved = saved.filter(item => item.id !== id);
    localStorage.setItem("inputs", JSON.stringify(saved));
}


function addInputToPage(cfg) {
    const container = document.getElementById("input-container");

    const row = document.createElement("div");
    row.classList.add("input-row");
    row.dataset.id = cfg.id;

    const input = document.createElement("input");
    input.type = "file";

    if (cfg.name) input.name = cfg.name;
    if (cfg.accept) input.accept = cfg.accept;
    if (cfg.multiple) input.multiple = true;
    if (cfg.required) input.required = true;
    if (cfg.capture) input.setAttribute("capture", cfg.capture);

    const delBtn = document.createElement("button");
    delBtn.textContent = "×";
    delBtn.classList.add("delete-input-btn");

    delBtn.onclick = () => {
        row.remove();
        removeInputConfig(cfg.id);
    };

    row.appendChild(input);
    row.appendChild(delBtn);

    container.appendChild(row);
}

function restoreInputs(container) {
    const saved = JSON.parse(localStorage.getItem("inputs") || "[]");
    saved.forEach(cfg => addInputToPage(cfg));
}
