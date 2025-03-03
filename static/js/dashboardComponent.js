    document.addEventListener("DOMContentLoaded", function () {
        let toastElList = [].slice.call(document.querySelectorAll('.toast'));
        let toastList = toastElList.map(function (toastEl) {
            return new bootstrap.Toast(toastEl);
        });
        toastList.forEach(toast => toast.show());
    });
    // End Desktop
    // Profile
function toggleSelection(element) {
    element.classList.toggle('selected');
}

function filterInterests() {
    let input = document.querySelector('.search-box').value.toLowerCase();
    let interests = document.querySelectorAll('.interest');

    interests.forEach(interest => {
        let text = interest.textContent.toLowerCase();
        if (text.includes(input)) {
            interest.style.display = "inline-block";
        } else {
            interest.style.display = "none";
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