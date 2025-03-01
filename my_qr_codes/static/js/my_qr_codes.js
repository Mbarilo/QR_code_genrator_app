let username = document.getElementById('name');
let logoutButton = document.querySelector('.logout');
let userInfoDiv = document.querySelector('.user-info-div');
let findInput = document.getElementById("finder");
let deleteButtonsList = document.querySelectorAll("#delete")
let subscribeButton = document.querySelector(".subscribe")
let hiddenQrCodes = document.querySelectorAll(".qr-code-element")


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


deleteButtonsList.forEach((element) => {
    console.log(element)
    element.addEventListener("click", () => {
        if (element.classList.contains("accept")) {
            element.setAttribute("name", "delete")
            element.setAttribute("type", "submit")
            console.log("ajgoie")
        }

        element.classList.add("accept")
    })
})

subscribeButton.addEventListener("click", () => {
    if (subscribeButton.textContent == "desktop") {
        subscribeButton.textContent = "web"
    }
    else {
        subscribeButton.textContent = "desktop"
    }
    hiddenQrCodes.forEach((element) => {
        element.classList.toggle("hidden")
    })
})
