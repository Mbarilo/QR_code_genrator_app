let dateInput = document.querySelector('.card-date-div')
let cardInput = document.querySelector('.card-number-div')


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