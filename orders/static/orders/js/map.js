let mapContainer = document.getElementById("map_box"), // 지도를 표시할 div
  mapOption = {
    center: new kakao.maps.LatLng(37.597329, 127.05885), // 지도의 중심좌표 - 한국외대
    level: 4, // 지도의 확대 레벨
  };

let map = new kakao.maps.Map(mapContainer, mapOption);

let marketPosition1 = new kakao.maps.LatLng(37.596805, 127.060177); //집현전
let marketPosition2 = new kakao.maps.LatLng(37.598448, 127.056612); //컴플리트커피
let marketPosition3 = new kakao.maps.LatLng(37.597062, 127.06118); //포컵스

//지도 위 마커(핀)
let marker1 = new kakao.maps.Marker({
  position: marketPosition1,
});
marker1.setMap(map);

let marker2 = new kakao.maps.Marker({
  position: marketPosition2,
});
marker2.setMap(map);

let marker3 = new kakao.maps.Marker({
  position: marketPosition3,
});
marker3.setMap(map);

//인포윈도우 표시 위치입니다
let iwContent1 = '<div class="infowindow">집현전</div>';
iwPosition1 = new kakao.maps.LatLng(37.596805, 127.060177);

let iwContent2 = '<div class="infowindow">컴플릿트커피</div>';
iwPosition2 = new kakao.maps.LatLng(37.598448, 127.056612);

let iwContent3 = '<div class="infowindow">포컵스</div>';
iwPosition3 = new kakao.maps.LatLng(37.597062, 127.06118);

//인포윈도우
let infowindow1 = new kakao.maps.CustomOverlay({
  content: iwContent1,
  position: iwPosition1,
  yAnchor: 0,
  xAnchor: 0.1,
});

let infowindow2 = new kakao.maps.CustomOverlay({
  position: iwPosition2,
  content: iwContent2,
  yAnchor: 0,
  xAnchor: 0.1,
});

let infowindow3 = new kakao.maps.CustomOverlay({
  position: iwPosition3,
  content: iwContent3,
  yAnchor: 0,
  xAnchor: 0.1,
});

let printhouse1 = document.getElementsByClassName("printerHouse")[0];
let printhouse2 = document.getElementsByClassName("printerHouse")[1];
let printhouse3 = document.getElementsByClassName("printerHouse")[2];

//마커 마우스오버 이벤트
kakao.maps.event.addListener(marker1, "mouseover", function () {
  infowindow1.setMap(map);
});
kakao.maps.event.addListener(marker2, "mouseover", function () {
  infowindow2.setMap(map);
});
kakao.maps.event.addListener(marker3, "mouseover", function () {
  infowindow3.setMap(map);
});

//마커 마우스 아웃 이벤트
kakao.maps.event.addListener(marker1, "mouseout", function () {
  if (printhouse1.checked == true) {
    infowindow1.setMap(map);
  } else {
    infowindow1.setMap(null);
  }
});
kakao.maps.event.addListener(marker2, "mouseout", function () {
  if (printhouse2.checked == true) {
    infowindow2.setMap(map);
  } else {
    infowindow2.setMap(null);
  }
});

kakao.maps.event.addListener(marker3, "mouseout", function () {
  if (printhouse3.checked == true) {
    infowindow3.setMap(map);
  } else {
    infowindow3.setMap(null);
  }
});

let labels = document.querySelectorAll(".label");
const CLICKED_CLASS = "clicked";

//마커 클릭 이벤트
function infoToggle() {
  if (printhouse1.checked == true) {
    infowindow1.setMap(map);
    printhouse1.parentElement.style.backgroundColor = "#7558EE1A";
    printhouse1.parentElement.style.border = "thin solid #7558EE";
  } else {
    infowindow1.setMap(null);
    printhouse1.parentElement.style.backgroundColor = "#FAFAFA";
    printhouse1.parentElement.style.border = "none";
  }

  if (printhouse2.checked == true) {
    infowindow2.setMap(map);
    printhouse2.parentElement.style.backgroundColor = "#7558EE1A";
    printhouse2.parentElement.style.border = "thin solid #7558EE";
  } else {
    infowindow2.setMap(null);
    printhouse2.parentElement.style.backgroundColor = " #FAFAFA";
    printhouse2.parentElement.style.border = "none";
  }

  if (printhouse3.checked == true) {
    infowindow3.setMap(map);
    printhouse3.parentElement.style.backgroundColor = "#7558EE1A";
    printhouse3.parentElement.style.border = "thin solid #7558EE";
  } else {
    infowindow3.setMap(null);
    printhouse3.parentElement.style.backgroundColor = " #FAFAFA";
    printhouse3.parentElement.style.border = "none";
  }
}
