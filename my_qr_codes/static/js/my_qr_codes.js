let username = document.getElementById('name');
let logoutButton = document.querySelector('.logout');
let userInfoDiv = document.querySelector('.user-info-div');
let findInput = document.getElementById("finder");
let deleteButton = document.getElementById("delete")
let subscribeButton = document.querySelector(".subscribe")

// findInput.addEventListener("input", () => {
//     InputText = findInput.value
//     console.log(InputText)
//     window.location.reload();
//     findInput.value = InputText
// })

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


deleteButton.addEventListener("click", () => {

    if (deleteButton.classList.contains("accept")) {
        deleteButton.setAttribute("name", "delete")
        deleteButton.setAttribute("type", "submit")
        console.log("ajgoie")
    }

    deleteButton.classList.add("accept")
})


subscribeButton.addEventListener("click", () =>{
    if (subscribeButton.textContent == "desktop"){
        subscribeButton.textContent = "web"
    }
    else{
        subscribeButton.textContent = "desktop"
    }
})