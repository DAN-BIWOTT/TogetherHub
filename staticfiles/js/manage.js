

// s is the True or False value of the Approvemember field.
function changeMemberState(userId,s,changeApprovalStateURL) {
    
    fetch(changeApprovalStateURL, {
        method: "POST",
        headers: {
            "X-CSRFToken": getCSRFToken(),  // Get CSRF token from cookies
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ user_id: userId, s:s })  // Correct user_id parameter
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            location.reload();
        } else {
            alert(`Failed to ban user: ${data.message}`);
        }
    })
    .catch(error => console.error("Error:", error));
}
