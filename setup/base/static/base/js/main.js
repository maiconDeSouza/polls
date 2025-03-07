const form = document.querySelector('main .new-poll form')
const ul = document.querySelector('main .new-poll form ul')
const addButton = document.querySelector('main .new-poll form [type="button"]')

addButton.addEventListener('click', e => {
    const liAll = document.querySelectorAll('main .new-poll form ul li')
    const totalLI = liAll.length + 1
    const li = document.createElement('li')
    const span = document.createElement('span')
    const label = document.createElement('label')
    const input = document.createElement('input')

    label.setAttribute('for', `choice`)
    const spanText = document.createTextNode(`Opção ${totalLI}:`)
    span.appendChild(spanText)
    input.type = "text";
    input.name = "choices";
    input.required = true;
    label.appendChild(span)
    label.appendChild(input)
    li.appendChild(label)
    ul.appendChild(li)
})


form.addEventListener('submit', e => {
    e.preventDefault()

    const inputs = document.querySelectorAll('main .new-poll form input')
    let valid = true

    inputs.forEach(input => {
        if (input.value.trim() === '') {
            valid = false;

        } 
    })

    if (valid) {
        form.submit()
    } else {
        alert('Preencha todos os campos antes de enviar.');
    }
});
