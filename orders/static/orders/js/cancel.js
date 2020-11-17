const id = document.getElementById('cancel')
const cancelBg = document.getElementById('cancel_bg')
const exit = document.getElementById('exit')

id.addEventListener('click', () => {
    cancelBg.style.display = 'block'
})

exit.addEventListener('click', ()=> {
    cancelBg.style.display = 'none'
})