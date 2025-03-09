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
// 
let selectedInterests = [];

function toggleSelection(element) {
    // Toggle the 'selected' class
    element.classList.toggle('selected');

    // Get the value of the clicked interest
    const interestValue = element.getAttribute('data-value');

    // Add or remove the interest from the selectedInterests array
    if (selectedInterests.includes(interestValue)) {
        selectedInterests = selectedInterests.filter(item => item !== interestValue);
    } else {
        selectedInterests.push(interestValue);
    }

    // Update the hidden input field with the selected interests
    document.getElementById('selected-interests').value = selectedInterests.join(',');
}

// Optional: Filter interests when typing in the search box
function filterInterests() {
    const searchTerm = document.getElementById('interest-search').value.toLowerCase();
    const interestElements = document.querySelectorAll('.interest');

    interestElements.forEach(interest => {
        const label = interest.textContent.toLowerCase();
        if (label.includes(searchTerm)) {
            interest.style.display = 'block';
        } else {
            interest.style.display = 'none';
        }
    });
}



function saveInterests() {
    let selectedInterests = [];
    document.querySelectorAll('.interest.selected').forEach(el => {
        selectedInterests.push(el.textContent);
    });

    alert("Selected Interests: " + selectedInterests.join(", "));
}