const cancelBtn = document.querySelector('.cancel-btn');
const cancelModal = document.querySelector('#cancel_modal');
const cancel = document.querySelector('#cancel');
const cancelBg = document.querySelector('#cancel_bg');
const exit = document.querySelector('#exit');
const message = document.querySelector('.message')

function cancelImpossible() {
    cancelModalClear();
    cancelModalMsgCreate();
}

function modalPopup() {
    cancelBg.style.display = 'block'
};

function modalPopdown() {
    cancelBg.style.display = 'none'
};

function cancelModalClear() {
    while (message.hasChildNodes()) {
        message.removeChild(message.firstChild)
    };
};

function cancelModalMsgCreate() {
    message.innerHTML = `
        <div class = "message">
        <span class="impossible_message">주문 취소 불가</span>
        <span class="impossible_message_small">해당 주문에 대한 인쇄가 시작되었으므로<br>주문 취소가 불가합니다.</span>
        </div>` 
    
}

cancelBtn.addEventListener('click', cancelImpossible);
cancel.addEventListener('click', modalPopup);
exit.addEventListener('click', modalPopdown)