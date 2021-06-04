const textEl = document.getElementById('auto-text')
const text = 'Лучше нас не бурит никто...'
let idx = 1
let speed = 100
writeText()
function writeText() {
    textEl.innerText = text.slice(0, idx) 
    idx++

    if (idx > text.length) {
        textEl.innerText = text.slice(0, idx) 
        idx--
    }
    setTimeout(writeText, speed)
}