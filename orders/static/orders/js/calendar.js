const init = {
  monList: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
  dayList: ['일', '월', '화', '수', '목', '금', '토'],
  today: new Date(),
  monForChange: new Date().getMonth(),
  activeDate: new Date(),
  getFirstDay: (yy, mm) => new Date(yy, mm, 1),
  getLastDay: (yy, mm) => new Date(yy, mm + 1, 0),
  nextMonth: function () {
    let d = new Date();
    d.setDate(1);
    d.setMonth(++this.monForChange);
    this.activeDate = d;
    return d;
  },
  prevMonth: function () {
    let d = new Date();
    d.setDate(1);
    d.setMonth(--this.monForChange);
    this.activeDate = d;
    return d;
  },
  addZero: (num) => (num < 10) ? '0' + num : num,
  activeDTag: null,
  getIndex: function (node) {
    let index = 0;
    while (node = node.previousElementSibling) {
      index++;
    }
    return index;
  }
};

const $calBody = document.querySelector('.cal-body');
const $btnNext = document.querySelector('.btn-cal.next');
const $btnPrev = document.querySelector('.btn-cal.prev');
const today_btn = document.querySelector('.todayBtn');


// function loadDate (date, dayIn) {
//   document.querySelector('.cal-date').textContent = date;
//   document.querySelector('.cal-day').textContent = init.dayList[dayIn];
// }


function loadYYMM (fullDate) {
  let yy = fullDate.getFullYear();
  let mm = fullDate.getMonth();
  let firstDay = init.getFirstDay(yy, mm);
  let lastDay = init.getLastDay(yy, mm);
  let markToday;  // for marking today date
  
  if (mm === init.today.getMonth() && yy === init.today.getFullYear()) {
    markToday = init.today;

    document.querySelector('.cal-month').textContent = init.monList[mm];
    document.querySelector('.cal-year').textContent = `${yy}년`;

    let trtd = '';
    let startCount;
    let countDay = 0;
    for (let i = 0; i < 6; i++) {
      trtd += '<tr>';
      for (let j = 0; j < 7; j++) {
        if (i === 0 && !startCount && j === firstDay.getDay()) {
          startCount = 1;
        }
        if (!startCount) {
          trtd += '<td>'
        } else {
          if (countDay + 1 < markToday.getDate()){
            
              trtd += '<td class="past_day';
              trtd += (markToday && markToday.getDate() === countDay + 1) ? ' today" ' : '"';
              trtd += ` data-year="${yy}" data-date="${countDay + 1}" data-month = "${init.addZero(mm+1)}" >`;
              
          }else{
            
            trtd += '<td class="day';
            trtd += (markToday && markToday.getDate() === countDay + 1) ? ' today" ' : '"';
            trtd += `data-year="${yy}" data-date="${countDay + 1}"  data-month = "${init.addZero(mm+1)}">`;
          }
        }

        trtd += (startCount) ? ++countDay : '';
        
        if (countDay === lastDay.getDate()) { 
          startCount = 0; 
        }
        trtd += '</td>';
      }
      trtd += '</tr>';
    } 
    $calBody.innerHTML = trtd;
  }else{
    document.querySelector('.cal-month').textContent = init.monList[mm];
    document.querySelector('.cal-year').textContent = `${yy}년`;

    let trtd = '';
    let startCount;
    let countDay = 0;
    for (let i = 0; i < 6; i++) {
      trtd += '<tr>';
      for (let j = 0; j < 7; j++) {
        if (i === 0 && !startCount && j === firstDay.getDay()) {
          startCount = 1;
        }
        if (!startCount) {
          trtd += '<td>'
        } else {
          if (yy === init.today.getFullYear() && mm < init.today.getMonth()){
              
              trtd += '<td class="past_day';
              trtd += (markToday && markToday.getDate() === countDay + 1) ? ' today" ' : '"';
              trtd += `data-year="${yy}" data-date="${countDay + 1}" data-month = "${init.addZero(mm+1)}">`;
              
          }else if (yy<init.today.getFullYear()) {
            
              trtd += '<td class="past_day';
              trtd += (markToday && markToday.getDate() === countDay + 1) ? ' today" ' : '"';
              trtd += `data-year="${yy}" data-date="${countDay + 1}"  data-month = "${init.addZero(mm+1)}">`;
              
          }else{
        
              trtd += '<td class="future';
              trtd += (markToday && markToday.getDate() === countDay + 1) ? ' today" ' : '"';
              trtd += `data-year="${yy}" data-date="${countDay + 1}"  data-month = "${init.addZero(mm+1)}">`;
              
          }
        }

        trtd += (startCount) ? ++countDay : '';
        if (countDay === lastDay.getDate()) { 
          startCount = 0; 
        }
        trtd += '</td>';
      }
      trtd += '</tr>';
    }
    $calBody.innerHTML = trtd;} 
  }

 function monForChangeReset(){
    init.monForChange = new Date().getMonth();
  }
// function createNewList (val) {
//   let id = new Date().getTime() + '';
//   let yy = init.activeDate.getFullYear();
//   let mm = init.activeDate.getMonth() + 1;
//   let dd = init.activeDate.getDate();
//   const target = $calBody.querySelector(`.day[data-date="${dd}"]`);

//   let date = yy + '.' + init.addZero(mm) + '.' + init.addZero(dd);

// }

loadYYMM(init.today);
// loadDate(init.today.getDate(), init.today.getDay());
$btnNext.addEventListener('click', () => loadYYMM(init.nextMonth()));
$btnPrev.addEventListener('click', () => loadYYMM(init.prevMonth()));


$calBody.addEventListener('click', (e) => {
  if (e.target.classList.contains('day') || e.target.classList.contains('future')) {
    if (init.activeDTag) {
      init.activeDTag.classList.remove('day-active');
    }
    let day = Number(e.target.textContent);
    // loadDate(day, e.target.cellIndex);
    e.target.classList.add('day-active');
    init.activeDTag = e.target;
    init.activeDate.setDate(day);
    // reloadTodo();
  }
});

today_btn.addEventListener('click', ()=> {
  loadYYMM(init.today);
  monForChangeReset();
  if (init.activeDTag) {
    init.activeDTag = null;
  }
})