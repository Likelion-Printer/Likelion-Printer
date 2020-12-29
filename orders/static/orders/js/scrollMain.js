'use static'

//html 연결 미완료

let windowHeight = window.innerHeight;
let contents = document.querySelector('.guide_content');

function getContentTop() {
    let contentTop = contents.getBoundingClientRect().top;
    return contentTop
}

function animation() {
    window.addEventListener('scroll', ()=>{
        let contentTop = getContentTop();

        if (windowHeight > contentTop){
            console.log(contentTop);
        }
    })  
}

function initAnimation() {
    animation();
}

initAnimation();