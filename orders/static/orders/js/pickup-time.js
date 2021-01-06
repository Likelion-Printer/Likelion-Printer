'use strict'

let pickupTimeTb = document.querySelector('.tb_pickup_time_detail');
let radioChecked;
let radioUncheked;

pickupTimeTb.addEventListener('click', labelChange);


function labelChange(event) {
    let labelToChange = event.target;
    if (!radioChecked) {
        if (labelToChange.matches('label')) {
            radioChecked = labelToChange;
            labelColorChange(labelToChange)
        }
    } else{
        if (labelToChange.matches('label'))
        radioUncheked = radioChecked;
        radioChecked = labelToChange;
        labelColorBack(radioUncheked);
        labelColorChange(labelToChange)
    }

}

function labelColorChange(label) {
    label.style.backgroundColor = 'pink'
}

function labelColorBack(label) {
    label.style.backgroundColor = 'green'
}