function getWeekDay(date) {
  	let days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

  	return days[date.getDay()];
}

function getDiffYears(date1, date2) {
    let years = date2.getFullYear() - date1.getFullYear();

    if (date2.getMonth() < date1.getMonth() || (date2.getMonth() === date1.getMonth() && date2.getDate() < date1.getDate())) {
        years--;
    }

    return years;
}

function askAge(question, yes, no) {
	if (confirm(question)) yes();
	else no();
}

async function saveBirth(formData) {
	const response = await fetch("/profile/update-age/", {
        method: "POST",
        headers: {
            "X-CSRFToken": formData.get("csrfmiddlewaretoken")
        },
        body: formData
    });
}

function noParent() {
	alert("Leave our website");
}

function printBattery(battery) {
	const symbol = battery.charging ? "⚡" : "❌";
	document.querySelector(".battery").textContent = `${Math.floor(battery.level * 100)}%${symbol}`;
}

document.addEventListener("DOMContentLoaded", () => {
	fetch("http://ip-api.com/json/").then(res => res.json()).then(data => {
		document.querySelector(".tz").textContent = data.timezone;
  	});

	navigator.getBattery().then(battery => {
		printBattery(battery);
		battery.addEventListener("levelchange", () => printBattery(battery));
		battery.addEventListener("chargingchange", () => printBattery(battery));
	});
	
    const form = document.querySelector(".date-update");
    form.addEventListener("submit", event => {
        event.preventDefault();
        const formData = new FormData(form);
        const date = new Date(formData.get("age"));
		if (isNaN(date.getTime())) {
    		alert("Incorrect date");
		} 
		else {
		    alert(`You where burn on ${getWeekDay(date)}`);
			const age = getDiffYears(date, new Date());
			if (age < 18) {
				askAge("Did your parents allow it?", () => saveBirth(formData), noParent);
			}
			else {
				saveBirth(formData);
			}
		}
    });
})