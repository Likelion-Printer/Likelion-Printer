const id = document.getElementById('cancel');
const cancelBg = document.getElementById('cancel_bg');
const exit = document.getElementById('exit');
const cancel_modal = document.getElementById('cancel_modal')


id.addEventListener('click', () => {
    cancelBg.style.display = 'block'
});

exit.addEventListener('click', ()=> {
    cancelBg.style.display = 'none'

})




// $('html, body').css({'overflow': 'hidden', 'height': '100%'}); // 모달팝업 중 html,body의 scroll을 hidden시킴 
// $('#cancel_modal').on('scroll touchmove mousewheel', function(event) { // 터치무브와 마우스휠 스크롤 방지    
//     event.preventDefault();     
//     event.stopPropagation();     
//     return false; 
// });