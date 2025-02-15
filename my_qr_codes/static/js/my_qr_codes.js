let username = document.getElementById('name');
let logoutButton = document.querySelector('.logout');
let userInfoDiv = document.querySelector('.user-info-div');
let findInput = document.querySelector(".finder");


findInput.addEventListener("keypress", () => {
    InputText = findInput.value
    console.log(InputText)
    // window.location.reload();
    findInput.value += InputText
})

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