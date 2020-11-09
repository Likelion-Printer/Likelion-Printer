function radio_Test1() {
    let radio_chk1 = document.getElementById('rd1');
    let radio_chk2 = document.getElementById('rd2');
   
    let vertical_img = document.getElementById('vertical_img');
    let horizon_img = document.getElementById('horizon_img');


    if (radio_chk1.checked == true) {
        vertical_img.src = '/static/garo_clicked.png'
        
    } else {
        vertical_img.src = '/static/garo.png'
    }
    if (radio_chk2.checked == true) {
        horizon_img.src = '/static/sero_clicked.png';
    }else {
        horizon_img.src = '/static/sero.png';
    }
}


function radio_Test2() {
    let radio_chk3 = document.getElementById('rd3');
    let radio_chk4 = document.getElementById('rd4');
    let radio_chk5 = document.getElementById('rd5');

    let one_img = document.getElementById('one_img');
    let two_img = document.getElementById('two_img');
    let four_img = document.getElementById('four_img');

    if (radio_chk3.checked == true) {
        one_img.src = '/static/one_clicked.png'
    } else {
        one_img.src = '/static/one.png'
    }
    if (radio_chk4.checked == true) {
        two_img.src = '/static/two_clicked.png';
    }else {
        two_img.src = '/static/two.png';
    }
    if (radio_chk5.checked == true) {
        four_img.src = '/static/four_clicked.png'
    } else {
        four_img.src = '/static/four.png'
    }
}

function radio_Test3() {
    let radio_chk6 = document.getElementById('rd6');
    let radio_chk7 = document.getElementById('rd7');

    let single_img = document.getElementById('single_img');
    let double_img = document.getElementById('double_img');

    if (radio_chk6.checked == true) {
        single_img.src = '/static/single_clicked.png'
    } else {
        single_img.src = '/static/single.png'
    }
    if (radio_chk7.checked == true) {
        double_img.src = '/static/double_clicked.png';
    }else {
        double_img.src = '/static/double.png';
    }
}

function radio_Test4() {
    let radio_chk8 = document.getElementById('rd8');
    let radio_chk9 = document.getElementById('rd9');

    let black_img = document.getElementById('black_img');
    let color_img = document.getElementById('color_img');

    if (radio_chk8.checked == true) {
        black_img.src = '/static/black_clicked.png'
    } else {
        black_img.src = '/static/black.png'
    }
    if (radio_chk9.checked == true) {
        color_img.src = '/static/color_clicked.png';
    }else {
        color_img.src = '/static/color.png';
    }
}

