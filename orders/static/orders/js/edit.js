function radio_Test() {
    let radio_chk1 = document.getElementById('rd1');
    let radio_chk2 = document.getElementById('rd2');
    let vertical_img = document.getElementById('vertical_img');
    let horizon_img = document.getElementById('horizon_img');
    let selected = document.getElementById('selected')

    if (radio_chk1.checked == true) {
        selected.style.backgroundColor = 'black';
    } else {
        vertical_img.src = '/static/Subtraction_3.png'
    }

    if (radio_chk2.checked == true) {
        horizon_img.src = '/static/Group-1.png';
    }else {
        horizon_img.src = '/static/Group_116.png';
    }
}
