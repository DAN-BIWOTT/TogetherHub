function enableEditMode() {
    document.getElementById("edit-form").style.display = "block";
    document.querySelector(".profile-details").style.display = "none";
    document.getElementById("occupation-input").value = document.getElementById("occupation-display").innerText;
    document.getElementById("phone-input").value = document.getElementById("phone-display").innerText;
    document.getElementById("location-input").value = document.getElementById("location-display").innerText;
    document.getElementById("membership-input").value = document.getElementById("membership-display").innerText;
    document.getElementById("skills-input").value = document.getElementById("skills-display").innerText;
}

function disableEditMode() {
    document.getElementById("edit-form").style.display = "none";
    document.querySelector(".profile-details").style.display = "block";
}

function saveProfileChanges() {
    document.getElementById("name-display").innerText = document.getElementById("name-input").value;
    document.getElementById("occupation-display").innerText = document.getElementById("occupation-input").value;
    document.getElementById("phone-display").innerText = document.getElementById("phone-input").value;
    document.getElementById("location-display").innerText = document.getElementById("location-input").value;
    document.getElementById("membership-display").innerText = document.getElementById("membership-input").value;
    document.getElementById("skills-display").innerText = document.getElementById("skills-input").value;
    disableEditMode();
}

 // Search interest
 function toggleSelection(element) {
    element.classList.toggle('selected');
}

function filterInterests() {
    let input = document.getElementById('interest-search'); // Get by ID

    if (!input) {
        console.error("Interest search input field not found.");
        return;
    }

    let filterValue = input.value.toLowerCase();
    let interests = document.querySelectorAll('.interest');

    interests.forEach(interest => {
        let text = interest.textContent.toLowerCase();
        interest.style.display = text.includes(filterValue) ? "inline-block" : "none";
    });
}


function saveInterests() {
    let selectedInterests = [];
    document.querySelectorAll('.interest.selected').forEach(el => {
        selectedInterests.push(el.textContent);
    });

    alert("Selected Interests: " + selectedInterests.join(", "));
}