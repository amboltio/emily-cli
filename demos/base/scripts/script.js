const clickMeBtn = document.getElementById('click-me-btn')

clickMeBtn.addEventListener('click', () => {
    alert(`
        You can add click handlers to buttons with
        "btnElement.addEventListener('click', () => { ... })"
    `)
})

