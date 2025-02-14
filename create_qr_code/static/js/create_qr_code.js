let username = document.getElementById('name');
let logoutButton = document.querySelector('.logout');
let userInfoDiv = document.querySelector('.user-info-div');
let logotype = document.getElementById("logo")

username.addEventListener('click', () => {
    if (userInfoDiv.style.opacity == 0) {
        userInfoDiv.style.opacity = 1;
        logoutButton.style.display = 'block';
    } else {
        userInfoDiv.style.opacity = 0;;
        setTimeout(() => {
            logoutButton.style.display = 'none';
        }, 1000);
    }
})

function readURL(input) {
    if (input.files && input.files[0]) {

        let reader = new FileReader();
        reader.onload = function (e) {
            logotype.setAttribute("src", e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}