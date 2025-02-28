let dateInput = document.querySelector('.card-date-div')
let cardInput = document.querySelector('.card-number-div')
let ccvInput = document.querySelector('.card-ccv-div')


IMask(
    dateInput.querySelector('input'), {
        mask: '00/00'
    }
)
IMask(
    cardInput.querySelector('input'), {
        mask: '0000 0000 0000 0000'
    }
)
IMask(
    ccvInput.querySelector('input'), {
        mask: '000'
    }
)

let monthButton = document.getElementById('month')
let yearButton = document.getElementById('year')
let price = document.getElementById('price')

monthButton.addEventListener('click', () => {
    price.textContent = '5$'
    monthButton.classList.add('active')
    yearButton.classList.remove('active')
})

yearButton.addEventListener('click', () => {
    price.textContent = '48$'
    yearButton.classList.add('active')
    monthButton.classList.remove('active')
})