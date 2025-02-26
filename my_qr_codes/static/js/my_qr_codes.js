let username = document.getElementById('name');
let logoutButton = document.querySelector('.logout');
let userInfoDiv = document.querySelector('.user-info-div');
let findInput = document.getElementById("finder");
let deleteButtonsList = document.querySelectorAll(".delete_button");


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
    // if (this.classList.contains("accept")) {
    //     this.getAttribute("id").setAttribute("name", "delete")
    //     this.getAttribute("id").setAttribute("type", "submit")
    //     console.log("ajgoie")
    // }

    // this.getAttribute("id").classList.add("accept")

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
